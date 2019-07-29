from AppFolder.Model.ResultsModel import LocalityAgent,LocalityAgent_schema,LocalityAgents_schema
from AppFolder import app,db
from flask import request, jsonify

# Create a LocalityAgent
@app.route('/localiltyAgent', methods=['POST'])
def add_LocalityAgent():
	localityId = request.json['localityId']
	agentId = request.json['agentId']
	new_data = LocalityAgent(LocalityAgentId, localityId, agentId)
	db.session.add(new_data)
	db.session.commit()
	return LocalityAgent_schema.jsonify(new_data)

# Get LocalityAgent
@app.route('/localiltyAgent/<id>', methods=['GET'])
def get_LocalityAgent(id):
	LA = LocalityAgent.query.get(id)
	if LA:
		return LocalityAgent_schema.jsonify(LA)
	else:
		return '<h1>This id does not exist</h1>'

#Get all LocalityAgents
@app.route('/localiltyAgents', methods=['GET'])
def get_LocalityAgents():
	all_LA = LocalityAgent.query.all()
	result = LocalityAgents_schema.dump(all_LA)
	return jsonify(result.data)

# Update a LocalityAgent
@app.route('/localiltyAgent/<id>', methods=['PUT'])
def update_LocalityAgents(id):
	LA = LocalityAgent.query.get(id)
	if LA:
		localityId = request.json['localityId']
		agentId = request.json['agentId']

		LA.LocalityAgentId = LocalityAgentId
		LA.agentId = agentId
		
		db.session.commit()
		return ResultsLocalityAgent_schema.jsonify(LocalityAgent)
	else:
		return '<h1>This LocalityAgent does not exist</h1>'


# Delete LocalityAgent
@app.route('/localiltyAgent/<id>', methods=['DELETE'])
def delete_LocalityAgent(id):
	LA = LocalityAgent.query.get(id)
	if LA:
		db.session.delete(LA)
		db.session.commit()
		return ResultsLocalityAgent_schema.jsonify(LA)
	else:
		return '<h1>This LocalityAgent does not exist</h1>'
