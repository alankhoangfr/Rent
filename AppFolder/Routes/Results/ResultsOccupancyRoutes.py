from AppFolder.Model.ResultsModel import ResultsOccupancy,ResultsOccupancy_schema,ResultsOccupancys_schema
from AppFolder import app,db
from flask import request, jsonify

# Create a occupancy
@app.route('/resultOcc', methods=['POST'])
def add_occupancy():
	suburb = request.json['suburb']
	bedrooms =request.json['bedrooms']
	bathrooms =request.json['bathrooms']
	AverageOccupancy  = request.json['AverageOccupancy']
	AO75Percentile  = request.json['AO75Percentile']
	AO50Percentile  = request.json['AO50Percentile']
	AOJanuary = request.json['AOJanuary']
	AOFebuary = request.json['AOFebuary']
	AOMarch =request.json['AOMarch']
	AOApril = request.json['AOApril']
	AOMay = request.json['AOMay']
	AOJnue = request.json['AOJnue']
	AOJuly = request.json['AOJuly']
	AOAugust = request.json['AOAugust']
	AOSeptember =request.json['AOSeptember']
	AOOctober =request.json['AOOctober']
	AONovember =request.json['AONovember']
	AODecember =request.json['AODecember']
	new_data = ResultsOccupancy(suburb, bedrooms, bathrooms,AverageOccupancy,AO75Percentile,AO50Percentile,
	AOJanuary,AOFebuary,AOMarch,AOApril,AOMay,AOJnue,AOJuly,AOAugust,AOSeptember,AOOctober,AONovember,AODecember)
	db.session.add(new_data)
	db.session.commit()
	return ResultsOccupancy_schema.jsonify(new_data)

# Get occupancy
@app.route('/resultOcc/<id>', methods=['GET'])
def get_occupancy(id):
	occupancy = ResultsOccupancy.query.get(id)
	if occupancy:
		return ResultsOccupancy_schema.jsonify(occupancy)
	else:
		return '<h1>This occupancy does not exist</h1>'

#Get all occupancys
@app.route('/resultOccs', methods=['GET'])
def get_occupancys():
	all_occupancy = ResultsOccupancy.query.all()
	result = ResultsOccupancys_schema.dump(all_occupancy)
	return jsonify(result.data)

# Update a occupancy
@app.route('/resultOcc/<id>', methods=['PUT'])
def update_occupancys(id):
	occupancy = ResultsOccupancy.query.get(id)
	if occupancy:
		localityId = request.json['localityId']
		suburb = request.json['suburb']
		bedrooms =request.json['bedrooms']
		bathrooms =request.json['bathrooms']
		AverageOccupancy  = request.json['AverageOccupancy']
		AO75Percentile  = request.json['AO75Percentile']
		AO50Percentile  = request.json['AO50Percentile']
		AOJanuary = request.json['AOJanuary']
		AOFebuary = request.json['AOFebuary']
		AOMarch =request.json['AOMarch']
		AOApril = request.json['AOApril']
		AOMay = request.json['AOMay']
		AOJnue = request.json['AOJnue']
		AOJuly = request.json['AOJuly']
		AOAugust = request.json['AOAugust']
		AOSeptember =request.json['AOSeptember']
		AOOctober =request.json['AOOctober']
		AONovember =request.json['AONovember']
		AODecember =request.json['AODecember']

		occupancy.occupancyId = occupancyId
		occupancy.suburb = suburb
		occupancy.bedrooms = bedrooms
		occupancy.bathrooms = bathrooms
		occupancy.AverageOccupancy = AverageOccupancy
		occupancy.AO75Percentile = AO75Percentile
		occupancy.AO50Percentile = AO50Percentile
		occupancy.AOJanuary = AOJanuary
		occupancy.AOFebuary = AOFebuary
		occupancy.AOMarch =AOMarch
		occupancy.AOApril = AOApril
		occupancy.AOMay = AOMay
		occupancy.AOJnue = AOJnue
		occupancy.AOJuly = AOJuly
		occupancy.AOAugust = AOAugust
		occupancy.AOSeptember = AOSeptember
		occupancy.AOOctober = AOOctober
		occupancy.AONovember = AONovember
		occupancy.AODecember = AODecember
		db.session.commit()
		return ResultsOccupancy_schema.jsonify(occupancy)
	else:
		return '<h1>This occupancy does not exist</h1>'


# Delete occupancy
@app.route('/resultOcc/<id>', methods=['DELETE'])
def delete_occupancy(id):
	occupancy = ResultsOccupancy.query.get(id)
	if occupancy:
		db.session.delete(occupancy)
		db.session.commit()
		return ResultsOccupancy_schema.jsonify(occupancy)
	else:
		return '<h1>This occupancy does not exist</h1>'
