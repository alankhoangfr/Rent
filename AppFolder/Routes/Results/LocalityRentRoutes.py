from AppFolder.Model.ResultsModel import LocalityRent,LocalityRent_schema,LocalityRents_schema
from AppFolder import app,db
from flask import request, jsonify


# Create a LocalityRent
@app.route('/localityRent', methods=['POST'])
def add_LocalityRent():
	localityId = request.json['localityId']
	suburb = request.json['suburb']
	bedrooms =request.json['bedrooms']
	bathrooms =request.json['bathrooms']
	numberOfHouses = request.json['numberOfHouses']
	averageRent  = request.json['averageRent']
	averageRent75Percentile  = request.json['averageRent75Percentile']
	averageRent50Percentile  = request.json['averageRent50Percentile']
	new_data = LocalityRent(localityId, suburb, bedrooms, bathrooms,numberOfHouses,averageRent,
		averageRent75Percentile,averageRent50Percentile)
	db.session.add(new_data)
	db.session.commit()
	return LocalityRent_schema.jsonify(new_data)

# Get LocalityRent
@app.route('/localityRent/<id>', methods=['GET'])
def get_LocalityRent(id):
	LR = LocalityRent.query.get(id)
	if LR:
		return LocalityRent_schema.jsonify(LR)
	else:
		return '<h1>This id does not exist</h1>'

#Get all LocalityRents
@app.route('/localityRents', methods=['GET'])
def get_LocalityRents():
	all_LR = LocalityRent.query.all()
	result = LocalityRents_schema.dump(all_LR)
	return jsonify(result.data)

 # Update a LocalityRent
@app.route('/localityRent/<id>', methods=['PUT'])
def update_LocalityRents(id):
	LR = LocalityRent.query.get(id)
	if LR:
		localityId = request.json['localityId']
		suburb = request.json['suburb']
		bedrooms =request.json['bedrooms']
		bathrooms =request.json['bathrooms']
		numberOfHouses = request.json['numberOfHouses']
		averageRent  = request.json['averageRent']
		averageRent75Percentile  = request.json['averageRent75Percentile']
		averageRent50Percentile  = request.json['averageRent50Percentile']
		LR.localityId = localityId
		LR.suburb = suburb
		LR.bedrooms = bedrooms
		LR.bathrooms = bathrooms
		LR.numberOfHouses = numberOfHouses
		LR.averageRent = averageRent
		LR.averageRent75Percentile = averageRent75Percentile
		LR.averageRent50Percentile = averageRent50Percentile
		db.session.commit()
		return ResultsLocalityRent_schema.jsonify(LR)
	else:
		return '<h1>This LocalityRent does not exist</h1>'


# Delete LocalityRent
@app.route('/localityRent/<id>', methods=['DELETE'])
def delete_LocalityRent(id):
	LR = LocalityRent.query.get(id)
	if LR:
		db.session.delete(LR)
		db.session.commit()
		return ResultsLocalityRent_schema.jsonify(LR)
	else:
		return '<h1>This LocalityRent does not exist</h1>'
