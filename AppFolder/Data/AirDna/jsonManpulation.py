import json

with open('otmRentals.json') as json_file:
	data = json.load(json_file)
	finalJson = []
	for p in data["_embedded"]["propertySummaryList"]:
		try:
			p["propertySummary"]["attributes"]["lockUpGarages"]
			bathrooms = p["propertySummary"]["attributes"]["bathrooms"]
		except:
			bathrooms = 0
		try:
			p["propertySummary"]["attributes"]["bedrooms"]
			bedrooms = p["propertySummary"]["attributes"]["bedrooms"]
		except:
			bedrooms = 0
		try:
			p["propertySummary"]["attributes"]["lockUpGarages"]
			garage = p["propertySummary"]["attributes"]["lockUpGarages"]
		except:
			garage = 0
		try:
			p["propertySummary"]["attributes"]["carSpaces"]
			carSpaces = p["propertySummary"]["attributes"]["carSpaces"]
		except:
			carSpaces = 0
		try:
			p["propertySummary"]["attributes"]["isCalculatedLandArea"]
			isCalculatedLandArea = p["propertySummary"]["attributes"]["isCalculatedLandArea"]
		except:
			isCalculatedLandArea = 0
		try:
			p["propertySummary"]["attributes"]["landArea"]
			landArea = p["propertySummary"]["attributes"]["landArea"]
		except:
			landArea = 0
		try:
			p["propertySummary"]["otmForRentDetail"]["agency"]
			agency = p["propertySummary"]["otmForRentDetail"]["agency"]
		except:
			agency = "There are no agency"
		try:
			p["propertySummary"]["otmForRentDetail"]["agent"]
			agent = p["propertySummary"]["otmForRentDetail"]["agent"]
		except:
			agent = "There are no agents"
		try:
			p["propertySummary"]["otmForRentDetail"]["date"]
			date = p["propertySummary"]["otmForRentDetail"]["date"]
		except:
			date = "There is no date"
		try:
			p["propertySummary"]["otmForRentDetail"]["isActiveCampaign"]
			isActiveCampaign = p["propertySummary"]["otmForRentDetail"]["isActiveCampaign"]
		except:
			isActiveCampaign = "no active campaign"
		try:
			p["propertySummary"]["otmForRentDetail"]["period"]
			period = p["propertySummary"]["otmForRentDetail"]["period"]
		except:
			period = "No period"
		try:
			p["propertySummary"]["otmForRentDetail"]["price"]
			price = p["propertySummary"]["otmForRentDetail"]["price"]
		except:
			price = 0
		try:
			p["propertySummary"]["otmForRentDetail"]["priceDescription"]
			priceDescription = p["propertySummary"]["otmForRentDetail"]["priceDescription"]
		except:
			priceDescription = "No price Description"
		each = {
			"id": p["propertySummary"]["id"],
			"bathrooms": bathrooms,
			"bedrooms": bedrooms,
			"carSpaces": carSpaces,
			"landArea": landArea,
			"lockUpGarages": garage,
			"latitude":round(p["propertySummary"]["coordinate"]["latitude"],4),
			"longitude":round(p["propertySummary"]["coordinate"]["longitude"],4),
			"councilAreaId": p["propertySummary"]["locationIdentifiers"]["councilAreaId"],
			"localityId": p["propertySummary"]["locationIdentifiers"]["localityId"],
			"postCodeId": p["propertySummary"]["locationIdentifiers"]["postCodeId"],
			"streetId": p["propertySummary"]["locationIdentifiers"]["streetId"],
			"propertySubType": p["propertySummary"]["propertySubType"],
			"propertySubTypeShort": p["propertySummary"]["propertySubTypeShort"],
			"propertyType": p["propertySummary"]["propertyType"],
			"agency": agency,
			"date": date,
			"isActiveCampaign": isActiveCampaign,
			"period": period,
			"price": price,
			"priceDescription": priceDescription
		}
		finalJson.append(each)

with open('otmRentalsManpulate.json', 'w') as f:
	json.dump(finalJson, f)