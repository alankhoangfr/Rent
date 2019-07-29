from AppFolder.Model.ResultsModel import Agent,Agent_schema,Agents_schema
from AppFolder import app,db
from flask import request, jsonify

# Create a Agent
@app.route('/agent', methods=['POST'])
def add_Agent():
	agentId = request.json['agentId']
	agentName = request.json['agentName']
	new_data = Agent(agentId, agentName)
	db.session.add(new_data)
	db.session.commit()
	return Agent_schema.jsonify(new_data)

# Get Agent
@app.route('/agent/<id>', methods=['GET'])
def get_Agent(id):
	Agent = Agent.query.get(id)
	if Agent:
		return Agent_schema.jsonify(Agent)
	else:
		return '<h1>This agent does not exist</h1>'

#Get all Agents
@app.route('/agents', methods=['GET'])
def get_Agents():
	all_Agent = Agent.query.all()
	result = Agents_schema.dump(all_Agent)
	return jsonify(result.data)

 # Update a Agent
@app.route('/agent/<id>', methods=['PUT'])
def update_Agents(id):
	Agent = Agent.query.get(id)
	if Agent:
		agentId = request.json['agentId']
		agentName = request.json['agentName']
		Agent.AgentId = AgentId
		Agent.agentName = agentName
		db.session.commit()
		return ResultsAgent_schema.jsonify(Agent)
	else:
		return '<h1>This Agent does not exist</h1>'


# Delete Agent
@app.route('/agent/<id>', methods=['DELETE'])
def delete_Agent(id):
	Agent = Agent.query.get(id)
	if Agent:
		db.session.delete(Agent)
		db.session.commit()
		return ResultsAgent_schema.jsonify(Agent)
	else:
		return '<h1>This Agent does not exist</h1>'
