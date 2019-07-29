from AppFolder.Model.ResultsModel import ResultsAAR,ResultsAAR_schema,ResultsAARs_schema
from AppFolder import app,db
from flask import request, jsonify


# Create a locality
@app.route('/resultAar', methods=['POST'])
def add_locality():
	suburb = request.json['suburb']
	bedrooms =request.json['bedrooms']
	bathrooms =request.json['bathrooms']
	AAR  = request.json['AAR']
	numberOfHouses = request.json['numberOfHouses']
	AARAppartment  = request.json['AARAppartment']
	NumberAARAppartment = request.json['NumberAARAppartment']
	AARHouse  = request.json['AARHouse']
	NumberAARHouse = request.json['NumberAARHouse']
	AAR75Percentile = request.json['AAR75Percentile']
	AAR50Percentile = request.json['AAR50Percentile']
	HighestType = request.json['HighestType']
	AARJanuary = request.json['AARJanuary']
	AARFebuary = request.json['AARFebuary']
	AARMarch =request.json['AARMarch']
	AARApril = request.json['AARApril']
	AARMay = request.json['AARMay']
	AARJnue = request.json['AARJnue']
	AARJuly = request.json['AARJuly']
	AARAugust = request.json['AARAugust']
	AARSeptember =request.json['AARSeptember']
	AAROctober =request.json['AAROctober']
	AARNovember =request.json['AARNovember']
	AARDecember =request.json['AARDecember']
	new_data = ResultsAAR(suburb, bedrooms, bathrooms,AAR,numberOfHouses,AARAppartment,NumberAARAppartment,AARHouse,NumberAARHouse,AAR75Percentile,AAR50Percentile,
		HighestType,AARJanuary,AARFebuary,AARMarch,AARApril,AARMay,AARJnue,AARJuly,AARAugust,AARSeptember,AAROctober,AARNovember,AARDecember)
	db.session.add(new_data)
	db.session.commit()
	return ResultsAAR_schema.jsonify(new_data)

# Get locality
@app.route('/resultAar/<id>', methods=['GET'])
def get_locality(id):
	locality = ResultsAAR.query.get(id)
	if locality:
		return ResultsAAR_schema.jsonify(locality)
	else:
		return '<h1>This locality does not exist</h1>'

#Get all localitys
@app.route('/resultAars', methods=['GET'])
def get_localitys():
	all_locality = ResultsAAR.query.all()
	result = ResultsAARs_schema.dump(all_locality)
	return jsonify(result.data)

# Update a locality
@app.route('/resultAar/<id>', methods=['PUT'])
def update_localitys(id):
	locality = ResultsAAR.query.get(id)
	if locality:
		suburb = request.json['suburb']
		bedrooms =request.json['bedrooms']
		bathrooms =request.json['bathrooms']
		AAR  = request.json['AAR']
		numberOfHouses = request.json['numberOfHouses']
		AARAppartment  = request.json['AARAppartment']
		NumberAARAppartment = request.json['NumberAARAppartment']
		AARHouse  = request.json['AARHouse']
		NumberAARHouse = request.json['NumberAARHouse']
		AAR75Percentile = request.json['AAR75Percentile']
		AAR50Percentile = request.json['AAR50Percentile']
		HighestType = request.json['HighestType']
		AARJanuary = request.json['AARJanuary']
		AARFebuary = request.json['AARFebuary']
		AARMarch =request.json['AARMarch']
		AARApril = request.json['AARApril']
		AARMay = request.json['AARMay']
		AARJnue = request.json['AARJnue']
		AARJuly = request.json['AARJuly']
		AARAugust = request.json['AARAugust']
		AARSeptember =request.json['AARSeptember']
		AAROctober =request.json['AAROctober']
		AARNovember =request.json['AARNovember']
		AARDecember =request.json['AARDecember']

		locality.suburb = suburb
		locality.bedrooms = bedrooms
		locality.bathrooms = bathrooms
		locality.AAR = AAR
		locality.numberOfHouses = numberOfHouses
		locality.AARAppartment = AARAppartment
		locality.NumberAARAppartment = NumberAARAppartment
		locality.AARHouse = AARHouse
		locality.NumberAARHouse = NumberAARHouse
		locality.AAR75Percentile = AAR75Percentile
		locality.AAR50Percentile = AAR50Percentile
		locality.HighestType = HighestType
		locality.AARJanuary = AARJanuary
		locality.AARFebuary = AARFebuary
		locality.AARMarch = AARMarch
		locality.AARApril = AARApril
		locality.AARMay = AARMay
		locality.AARJnue = AARJnue
		locality.AARJuly = AARJuly
		locality.AARAugust = AARAugust
		locality.AARSeptember = AARSeptember
		locality.AAROctober = AAROctober
		locality.AARNovember = AARNovember
		locality.AARDecember = AARDecember
		db.session.commit()
		return ResultsAAR_schema.jsonify(locality)
	else:
		return '<h1>This locality does not exist</h1>'


# Delete locality
@app.route('/resultAar/<id>', methods=['DELETE'])
def delete_locality(id):
	locality = ResultsAAR.query.get(id)
	if locality:
		db.session.delete(locality)
		db.session.commit()
		return ResultsAAR_schema.jsonify(locality)
	else:
		return '<h1>This locality does not exist</h1>'
