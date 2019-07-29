import pandas as pd
from AppFolder import db
import requests 
import json
from AppFolder.config.key import Bearer
from pandas.io.json import json_normalize
from AppFolder.Model.ResultsModel import Agent,LocalityRent,ResultsAAR,ResultsOccupancy,LocalityAgentBedrooms


def reset_db():
    """Drops and Creates fresh database"""
    db.drop_all()
    db.create_all()

def q75(x):
    return x.quantile(0.75)

def setupAirDna():
	Annual = pd.read_csv(r'C:\Users\AlankHoang\Desktop\python\rent\AppFolder\Data\AirDna\Annual1Manpul.csv')
	Monthly = pd.read_csv(r'C:\Users\AlankHoang\Desktop\python\rent\AppFolder\Data\AirDna\MonthlyManpul.csv')
	total_neighborhood=Annual["Neighborhood"].unique().tolist()
	AGrouped = Annual.groupby(["Neighborhood","Bedrooms","Bathrooms"]).agg({
		"Neighborhood": "count",
		"AverageDailyRateNative": ["mean",q75,"median","max"],
		"OccupancyRateLTM":["mean",q75,"median"],
		})
	AGroupedMax = Annual.groupby(["Neighborhood","Bedrooms","Bathrooms"])["HouseAppartment"].agg({
		"AverageDailyRateNative":"max"
		}).reset_index()
	AGroupedGroupedType = Annual.groupby(["Neighborhood","Bedrooms","Bathrooms","HouseAppartment"]).agg({
		"AverageDailyRateNative": ["mean","count"]
		}).reset_index()
	MA = pd.merge(Monthly,Annual[["PropertyID","Bathrooms"]],how="left", on=["PropertyID"])
	MGrouped = MA.groupby(["Neighborhood","Bedrooms","Bathrooms","ReportingMonth"]).agg({
		"RevenueNative": "mean",
		"OccupancyRate":"mean",
		}).reset_index()

	for index, row in AGrouped.iterrows():
		#index = [neigbourhood, bedrooms, bathrooms]
		#print(index[0],index[1],index[2])
		def getValue(df,n):
			if len(df)==0:	
				return 0
			else:
				return df[0][n]

		Aar = ResultsAAR(
			suburb=str(index[0]),
			bedrooms=index[1],
			bathrooms=index[2],
			AAR = row["AverageDailyRateNative"]["mean"],
			numberOfProperty=int(row["Neighborhood"]["count"]),
			AARAppartment  = getValue(AGroupedGroupedType[(AGroupedGroupedType["Neighborhood"]==index[0])&(AGroupedGroupedType["Bedrooms"]==index[1])&
			(AGroupedGroupedType["Bathrooms"]==index[2])&(AGroupedGroupedType["HouseAppartment"]=="Appartment")].values,4),
			NumberAARAppartment  =getValue(AGroupedGroupedType[(AGroupedGroupedType["Neighborhood"]==index[0])&(AGroupedGroupedType["Bedrooms"]==index[1])&
			(AGroupedGroupedType["Bathrooms"]==index[2])&(AGroupedGroupedType["HouseAppartment"]=="Appartment")].values,5),
			AARHouse = getValue(AGroupedGroupedType[(AGroupedGroupedType["Neighborhood"]==index[0])&(AGroupedGroupedType["Bedrooms"]==index[1])&
			(AGroupedGroupedType["Bathrooms"]==index[2])&(AGroupedGroupedType["HouseAppartment"]=="House")].values,4),
			NumberAARHouse  = getValue(AGroupedGroupedType[(AGroupedGroupedType["Neighborhood"]==index[0])&(AGroupedGroupedType["Bedrooms"]==index[1])&
			(AGroupedGroupedType["Bathrooms"]==index[2])&(AGroupedGroupedType["HouseAppartment"]=="House")].values,5),
			AAR75Percentile=row["AverageDailyRateNative"]["q75"],
			AAR50Percentile=row["AverageDailyRateNative"]["median"],
			HighestType = getValue(AGroupedMax[(AGroupedMax["Neighborhood"]==index[0])&(AGroupedMax["Bedrooms"]==index[1])&
			(AGroupedMax["Bathrooms"]==index[2])].values,3),
			AARJanuary = getValue(MGrouped[(MGrouped["Neighborhood"]==index[0])&(MGrouped["Bedrooms"]==index[1])&
			(MGrouped["Bathrooms"]==index[2])&(MGrouped["ReportingMonth"]=="01/01/2018")].values,4),
			AARFebuary = getValue(MGrouped[(MGrouped["Neighborhood"]==index[0])&(MGrouped["Bedrooms"]==index[1])&
			(MGrouped["Bathrooms"]==index[2])&(MGrouped["ReportingMonth"]=="01/02/2018")].values,4),
			AARMarch =getValue(MGrouped[(MGrouped["Neighborhood"]==index[0])&(MGrouped["Bedrooms"]==index[1])&
			(MGrouped["Bathrooms"]==index[2])&(MGrouped["ReportingMonth"]=="01/03/2018")].values,4),
			AARApril =getValue(MGrouped[(MGrouped["Neighborhood"]==index[0])&(MGrouped["Bedrooms"]==index[1])&
			(MGrouped["Bathrooms"]==index[2])&(MGrouped["ReportingMonth"]=="01/04/2018")].values,4),
			AARMay =getValue(MGrouped[(MGrouped["Neighborhood"]==index[0])&(MGrouped["Bedrooms"]==index[1])&
			(MGrouped["Bathrooms"]==index[2])&(MGrouped["ReportingMonth"]=="01/05/2018")].values,4),
			AARJune =getValue(MGrouped[(MGrouped["Neighborhood"]==index[0])&(MGrouped["Bedrooms"]==index[1])&
			(MGrouped["Bathrooms"]==index[2])&(MGrouped["ReportingMonth"]=="01/06/2018")].values,4),
			AARJuly =getValue(MGrouped[(MGrouped["Neighborhood"]==index[0])&(MGrouped["Bedrooms"]==index[1])&
			(MGrouped["Bathrooms"]==index[2])&(MGrouped["ReportingMonth"]=="01/07/2018")].values,4),
			AARAugust=getValue(MGrouped[(MGrouped["Neighborhood"]==index[0])&(MGrouped["Bedrooms"]==index[1])&
			(MGrouped["Bathrooms"]==index[2])&(MGrouped["ReportingMonth"]=="01/08/2018")].values,4),
			AARSeptember =getValue(MGrouped[(MGrouped["Neighborhood"]==index[0])&(MGrouped["Bedrooms"]==index[1])&
			(MGrouped["Bathrooms"]==index[2])&(MGrouped["ReportingMonth"]=="01/09/2018")].values,4),
			AAROctober =getValue(MGrouped[(MGrouped["Neighborhood"]==index[0])&(MGrouped["Bedrooms"]==index[1])&
			(MGrouped["Bathrooms"]==index[2])&(MGrouped["ReportingMonth"]=="01/10/2018")].values,4),
			AARNovember =getValue(MGrouped[(MGrouped["Neighborhood"]==index[0])&(MGrouped["Bedrooms"]==index[1])&
			(MGrouped["Bathrooms"]==index[2])&(MGrouped["ReportingMonth"]=="01/11/2018")].values,4),
			AARDecember =getValue(MGrouped[(MGrouped["Neighborhood"]==index[0])&(MGrouped["Bedrooms"]==index[1])&
			(MGrouped["Bathrooms"]==index[2])&(MGrouped["ReportingMonth"]=="01/12/2018")].values,4)
			)
		ROCC = ResultsOccupancy(
			suburb=str(index[0]),
			bedrooms=index[1],
			bathrooms=index[2],
			AverageOccupancy =row["OccupancyRateLTM"]["mean"],
			AO75Percentile =row["OccupancyRateLTM"]["q75"],
			AO50Percentile=row["OccupancyRateLTM"]["median"],
			AOJanuary = getValue(MGrouped[(MGrouped["Neighborhood"]==index[0])&(MGrouped["Bedrooms"]==index[1])&
			(MGrouped["Bathrooms"]==index[2])&(MGrouped["ReportingMonth"]=="01/01/2018")].values,5),
			AOFebuary = getValue(MGrouped[(MGrouped["Neighborhood"]==index[0])&(MGrouped["Bedrooms"]==index[1])&
			(MGrouped["Bathrooms"]==index[2])&(MGrouped["ReportingMonth"]=="01/02/2018")].values,5),
			AOMarch =getValue(MGrouped[(MGrouped["Neighborhood"]==index[0])&(MGrouped["Bedrooms"]==index[1])&
			(MGrouped["Bathrooms"]==index[2])&(MGrouped["ReportingMonth"]=="01/03/2018")].values,5),
			AOApril =getValue(MGrouped[(MGrouped["Neighborhood"]==index[0])&(MGrouped["Bedrooms"]==index[1])&
			(MGrouped["Bathrooms"]==index[2])&(MGrouped["ReportingMonth"]=="01/04/2018")].values,5),
			AOMay =getValue(MGrouped[(MGrouped["Neighborhood"]==index[0])&(MGrouped["Bedrooms"]==index[1])&
			(MGrouped["Bathrooms"]==index[2])&(MGrouped["ReportingMonth"]=="01/05/2018")].values,5),
			AOJune =getValue(MGrouped[(MGrouped["Neighborhood"]==index[0])&(MGrouped["Bedrooms"]==index[1])&
			(MGrouped["Bathrooms"]==index[2])&(MGrouped["ReportingMonth"]=="01/06/2018")].values,5),
			AOJuly =getValue(MGrouped[(MGrouped["Neighborhood"]==index[0])&(MGrouped["Bedrooms"]==index[1])&
			(MGrouped["Bathrooms"]==index[2])&(MGrouped["ReportingMonth"]=="01/07/2018")].values,5),
			AOAugust=getValue(MGrouped[(MGrouped["Neighborhood"]==index[0])&(MGrouped["Bedrooms"]==index[1])&
			(MGrouped["Bathrooms"]==index[2])&(MGrouped["ReportingMonth"]=="01/08/2018")].values,5),
			AOSeptember =getValue(MGrouped[(MGrouped["Neighborhood"]==index[0])&(MGrouped["Bedrooms"]==index[1])&
			(MGrouped["Bathrooms"]==index[2])&(MGrouped["ReportingMonth"]=="01/09/2018")].values,5),
			AOOctober =getValue(MGrouped[(MGrouped["Neighborhood"]==index[0])&(MGrouped["Bedrooms"]==index[1])&
			(MGrouped["Bathrooms"]==index[2])&(MGrouped["ReportingMonth"]=="01/10/2018")].values,5),
			AONovember =getValue(MGrouped[(MGrouped["Neighborhood"]==index[0])&(MGrouped["Bedrooms"]==index[1])&
			(MGrouped["Bathrooms"]==index[2])&(MGrouped["ReportingMonth"]=="01/11/2018")].values,5),
			AODecember =getValue(MGrouped[(MGrouped["Neighborhood"]==index[0])&(MGrouped["Bedrooms"]==index[1])&
			(MGrouped["Bathrooms"]==index[2])&(MGrouped["ReportingMonth"]=="01/12/2018")].values,5)
			)
		db.session.add(Aar)
		db.session.add(ROCC)
	db.session.commit()

def analysedf(df):
	newDf = df[["propertySummary.id","propertySummary.locationIdentifiers.localityId","propertySummary.attributes.bedrooms","propertySummary.attributes.bathrooms",
	"propertySummary.otmForRentDetail.agency","propertySummary.otmForRentDetail.price","propertySummary.otmForRentDetail.period","propertySummary.propertyType"]] 
	newDf=newDf.rename(columns={"propertySummary.id": "propertyId", "propertySummary.locationIdentifiers.localityId": "localityId","propertySummary.attributes.bedrooms":"Bedrooms",
		"propertySummary.attributes.bathrooms":"Bathrooms","propertySummary.otmForRentDetail.agency":"agency","propertySummary.otmForRentDetail.price":"price",
		"propertySummary.otmForRentDetail.period":"period","propertySummary.propertyType":"propertyType"})
	newDf["HouseAppartment"]=newDf["propertyType"].apply(lambda x: "House" if x=="HOUSE" else ("Commerical" if x =="COMMERCIAL" else "Appartment"))
	newDf["RatioPeriod"]=newDf["period"].apply(lambda x: 1 if x=="W" else (52 if x=="A" else 12/52))
	newDf["WeeklyRent"]=newDf["price"]/newDf["RatioPeriod"]
	#Take out rows that are 1.5 outside the std
	newDf["outliers"] = newDf["WeeklyRent"].apply(lambda x: False if abs(x-newDf["WeeklyRent"].mean())>1.5 * newDf["WeeklyRent"].std() else True)
	newDf=newDf[newDf['Bedrooms'].notnull() & (newDf['outliers'] == True)]
	newDf=newDf.drop(columns=["propertyType","price","RatioPeriod","period","outliers"])
	return newDf



def setupRPD():
	localityIds = {"Kamabh":16593,"Monash":6973,"Oxley":12021}
	localitydf = {}
	agents = []

	for suburbs in localityIds:
		response = requests.get('https://api-uat.corelogic.asia/sandbox/search/au/property/locality/{}/otmForRent'.format(localityIds[suburbs]), 
			headers={'Authorization':'Bearer ' + Bearer})
		responseJson = response.json()
		df = json_normalize(responseJson["_embedded"]["propertySummaryList"])
		localityPdOringal = analysedf(df)
		numberOfPages=responseJson["page"]['totalPages']		
		for i in range(1,numberOfPages):
			print(i)
			PARAMS = {'page':i} 
			response = requests.get('https://api-uat.corelogic.asia/sandbox/search/au/property/locality/{}/otmForRent'.format(localityIds[suburbs]), 
			headers={'Authorization':'Bearer ' + Bearer}, params = PARAMS)
			responseJson = response.json()
			dfpage = json_normalize(responseJson["_embedded"]["propertySummaryList"])
			localityPage = analysedf(dfpage)
			localityPdOringal.append(localityPd, ignore_index=True)
		#print(localityPdOringal)
		localitydf[localityIds[suburbs]]=localityPdOringal
		agents.extend(localityPdOringal["agency"].unique().tolist())
#creating a dictionary for all agents and then adding all the agents to the database
	agents = set(agents)
	agentsDict = {}
	for agent in agents:
		agentsDict[agent] =Agent(agentName=agent)
		db.session.add(agentsDict[agent])
	for suburbs in localityIds:
		localityPdOringal = localitydf[localityIds[suburbs]]
		AGroupedId = localityPdOringal.groupby(["localityId","Bedrooms","Bathrooms"]).agg({
		"propertyId": "count",
		"WeeklyRent": ["mean",q75,"median","max"]
		}).reset_index()
		agentsLocality = localityPdOringal.groupby(["localityId","Bedrooms","Bathrooms"]).aggregate(lambda x: x.unique().tolist())["agency"].reset_index()
		AgentsPerLocality = localityPdOringal.groupby(["localityId","Bedrooms","Bathrooms","agency"]).agg({
		"propertyId": "count",
		"WeeklyRent": ["mean",q75,"median"]
		}).reset_index()
		#print(AgentsPerLocality)
		for index, row in AGroupedId.iterrows():
			lr = LocalityRent(localityId=int(row["localityId"]), suburb=suburbs, bedrooms=int(row["Bedrooms"][0]), bathrooms=int(row["Bathrooms"][0])
				, averageRent = row["WeeklyRent"]["mean"], averageRent75Percentile=row["WeeklyRent"]["q75"], averageRent50Percentile=row["WeeklyRent"]["median"]
				, numberOfProperty=row["propertyId"]["count"])
			db.session.add(lr)
			#print(agentsLocality,int(row["localityId"]),int(row["Bedrooms"][0]),int(row["Bathrooms"][0]) )
			agentsInLocality = agentsLocality.loc[(agentsLocality["localityId"]==int(row["localityId"]))&(agentsLocality["Bedrooms"]==int(row["Bedrooms"][0]))
			&(agentsLocality["Bathrooms"]==int(row["Bathrooms"][0]))].values
			for eachAgent in agentsInLocality[0][3]:
				currentAgent = agentsDict[eachAgent]
				lr.agents.append(currentAgent)	
		for index, row in AgentsPerLocality.iterrows():
			lrb = LocalityAgentBedrooms(localityId=int(row["localityId"]), suburb=suburbs, bedrooms=int(row["Bedrooms"][0]), bathrooms=int(row["Bathrooms"][0])
				, agentName = str(row["agency"][0]), averageRent = row["WeeklyRent"]["mean"], averageRent75Percentile=row["WeeklyRent"]["q75"]
				, averageRent50Percentile=row["WeeklyRent"]["median"], numberOfProperty=row["propertyId"]["count"])
			db.session.add(lrb)
	db.session.commit()





	
def setupAirDnaRoutes():
	Annual = pd.read_csv(r'C:\Users\AlankHoang\Desktop\python\rent\AppFolder\Data\AirDna\Annual1Manpul.csv')
	Monthly = pd.read_csv(r'C:\Users\AlankHoang\Desktop\python\rent\AppFolder\Data\AirDna\MonthlyManpul.csv')
	total_neighborhood=Annual["Neighborhood"].unique().tolist()
	AGrouped = Annual.groupby(["Neighborhood","Bedrooms","Bathrooms"]).agg({
		"Neighborhood": "count",
		"AverageDailyRateNative": ["mean",q75,"median","max"],
		"OccupancyRateLTM":["mean",q75,"median"],
		})
	AGroupedMax = Annual.groupby(["Neighborhood","Bedrooms","Bathrooms"])["HouseAppartment"].agg({
		"AverageDailyRateNative":"max"
		}).reset_index()
	AGroupedGroupedType = Annual.groupby(["Neighborhood","Bedrooms","Bathrooms","HouseAppartment"]).agg({
		"AverageDailyRateNative": ["mean","count"]
		}).reset_index()
	MA = pd.merge(Monthly,Annual[["PropertyID","Bathrooms"]],how="left", on=["PropertyID"])
	MGrouped = MA.groupby(["Neighborhood","Bedrooms","Bathrooms","ReportingMonth"]).agg({
		"RevenueNative": "mean",
		"OccupancyRate":"mean",
		}).reset_index()

	for index, row in AGrouped.iterrows():
		#index = [neigbourhood, bedrooms, bathrooms]
		print(index[0],index[1],index[2])

		def getValue(df,n):
			if len(df)==0:	
				return 0
			else:
				return df[0][n]

		AARResult = {}
		OCCResult = {}

		AARResult["suburb"]=str(index[0])
		AARResult["bedrooms"]=index[1]
		AARResult["bathrooms"]=index[2]
		AARResult["AAR"] = row["AverageDailyRateNative"]["mean"]
		AARResult["numberOfProperty"]=int(row["Neighborhood"]["count"])
		AARResult["AARAppartment"]  = getValue(AGroupedGroupedType[(AGroupedGroupedType["Neighborhood"]==index[0])&(AGroupedGroupedType["Bedrooms"]==index[1])&
		(AGroupedGroupedType["Bathrooms"]==index[2])&(AGroupedGroupedType["HouseAppartment"]=="Appartment")].values,4)
		AARResult["NumberAARAppartment"]  =getValue(AGroupedGroupedType[(AGroupedGroupedType["Neighborhood"]==index[0])&(AGroupedGroupedType["Bedrooms"]==index[1])&
		(AGroupedGroupedType["Bathrooms"]==index[2])&(AGroupedGroupedType["HouseAppartment"]=="Appartment")].values,5)
		AARResult["AARHouse"]  = getValue(AGroupedGroupedType[(AGroupedGroupedType["Neighborhood"]==index[0])&(AGroupedGroupedType["Bedrooms"]==index[1])&
		(AGroupedGroupedType["Bathrooms"]==index[2])&(AGroupedGroupedType["HouseAppartment"]=="House")].values,4)
		AARResult["NumberAARHouse"]  = getValue(AGroupedGroupedType[(AGroupedGroupedType["Neighborhood"]==index[0])&(AGroupedGroupedType["Bedrooms"]==index[1])&
		(AGroupedGroupedType["Bathrooms"]==index[2])&(AGroupedGroupedType["HouseAppartment"]=="House")].values,5)
		AARResult["AAR75Percentile"]=row["AverageDailyRateNative"]["q75"]
		AARResult["AAR50Percentile"]=row["AverageDailyRateNative"]["median"]
		AARResult["HighestType"] = getValue(AGroupedMax[(AGroupedMax["Neighborhood"]==index[0])&(AGroupedMax["Bedrooms"]==index[1])&
		(AGroupedMax["Bathrooms"]==index[2])].values,3)
		AARResult["AARJanuary"] = getValue(MGrouped[(MGrouped["Neighborhood"]==index[0])&(MGrouped["Bedrooms"]==index[1])&
		(MGrouped["Bathrooms"]==index[2])&(MGrouped["ReportingMonth"]=="01/01/2018")].values,4)
		AARResult["AARFebuary"] = getValue(MGrouped[(MGrouped["Neighborhood"]==index[0])&(MGrouped["Bedrooms"]==index[1])&
		(MGrouped["Bathrooms"]==index[2])&(MGrouped["ReportingMonth"]=="01/02/2018")].values,4)
		AARResult["AARMarch"] =getValue(MGrouped[(MGrouped["Neighborhood"]==index[0])&(MGrouped["Bedrooms"]==index[1])&
		(MGrouped["Bathrooms"]==index[2])&(MGrouped["ReportingMonth"]=="01/03/2018")].values,4)
		AARResult["AARApril"] =getValue(MGrouped[(MGrouped["Neighborhood"]==index[0])&(MGrouped["Bedrooms"]==index[1])&
		(MGrouped["Bathrooms"]==index[2])&(MGrouped["ReportingMonth"]=="01/04/2018")].values,4)
		AARResult["AARMay"] =getValue(MGrouped[(MGrouped["Neighborhood"]==index[0])&(MGrouped["Bedrooms"]==index[1])&
		(MGrouped["Bathrooms"]==index[2])&(MGrouped["ReportingMonth"]=="01/05/2018")].values,4)
		AARResult["AARJune"] =getValue(MGrouped[(MGrouped["Neighborhood"]==index[0])&(MGrouped["Bedrooms"]==index[1])&
		(MGrouped["Bathrooms"]==index[2])&(MGrouped["ReportingMonth"]=="01/06/2018")].values,4)
		AARResult["AARJuly"] =getValue(MGrouped[(MGrouped["Neighborhood"]==index[0])&(MGrouped["Bedrooms"]==index[1])&
		(MGrouped["Bathrooms"]==index[2])&(MGrouped["ReportingMonth"]=="01/07/2018")].values,4)
		AARResult["AARAugust"]=getValue(MGrouped[(MGrouped["Neighborhood"]==index[0])&(MGrouped["Bedrooms"]==index[1])&
		(MGrouped["Bathrooms"]==index[2])&(MGrouped["ReportingMonth"]=="01/08/2018")].values,4)
		AARResult["AARSeptember"] =getValue(MGrouped[(MGrouped["Neighborhood"]==index[0])&(MGrouped["Bedrooms"]==index[1])&
		(MGrouped["Bathrooms"]==index[2])&(MGrouped["ReportingMonth"]=="01/09/2018")].values,4)
		AARResult["AAROctober"] =getValue(MGrouped[(MGrouped["Neighborhood"]==index[0])&(MGrouped["Bedrooms"]==index[1])&
		(MGrouped["Bathrooms"]==index[2])&(MGrouped["ReportingMonth"]=="01/10/2018")].values,4)
		AARResult["AARNovember"] =getValue(MGrouped[(MGrouped["Neighborhood"]==index[0])&(MGrouped["Bedrooms"]==index[1])&
		(MGrouped["Bathrooms"]==index[2])&(MGrouped["ReportingMonth"]=="01/11/2018")].values,4)
		AARResult["AARDecember"] =getValue(MGrouped[(MGrouped["Neighborhood"]==index[0])&(MGrouped["Bedrooms"]==index[1])&
		(MGrouped["Bathrooms"]==index[2])&(MGrouped["ReportingMonth"]=="01/12/2018")].values,4)
		
		OCCResult["suburb"]=str(index[0])
		OCCResult["bedrooms"]=index[1]
		OCCResult["bathrooms"]=index[2]
		OCCResult["AverageOccupancy"] =row["OccupancyRateLTM"]["mean"]
		OCCResult["AO75Percentile"] =row["OccupancyRateLTM"]["q75"]
		OCCResult["AO50Percentile"]=row["OccupancyRateLTM"]["median"]
		OCCResult["AOJanuary"] = getValue(MGrouped[(MGrouped["Neighborhood"]==index[0])&(MGrouped["Bedrooms"]==index[1])&
		(MGrouped["Bathrooms"]==index[2])&(MGrouped["ReportingMonth"]=="01/01/2018")].values,5)
		OCCResult["AOFebuary"] = getValue(MGrouped[(MGrouped["Neighborhood"]==index[0])&(MGrouped["Bedrooms"]==index[1])&
		(MGrouped["Bathrooms"]==index[2])&(MGrouped["ReportingMonth"]=="01/02/2018")].values,5)
		OCCResult["AOMarch"] =getValue(MGrouped[(MGrouped["Neighborhood"]==index[0])&(MGrouped["Bedrooms"]==index[1])&
		(MGrouped["Bathrooms"]==index[2])&(MGrouped["ReportingMonth"]=="01/03/2018")].values,5)
		OCCResult["AOApril"] =getValue(MGrouped[(MGrouped["Neighborhood"]==index[0])&(MGrouped["Bedrooms"]==index[1])&
		(MGrouped["Bathrooms"]==index[2])&(MGrouped["ReportingMonth"]=="01/04/2018")].values,5)
		OCCResult["AOMay"] =getValue(MGrouped[(MGrouped["Neighborhood"]==index[0])&(MGrouped["Bedrooms"]==index[1])&
		(MGrouped["Bathrooms"]==index[2])&(MGrouped["ReportingMonth"]=="01/05/2018")].values,5)
		OCCResult["AOJune"] =getValue(MGrouped[(MGrouped["Neighborhood"]==index[0])&(MGrouped["Bedrooms"]==index[1])&
		(MGrouped["Bathrooms"]==index[2])&(MGrouped["ReportingMonth"]=="01/06/2018")].values,5)
		OCCResult["AOJuly"] =getValue(MGrouped[(MGrouped["Neighborhood"]==index[0])&(MGrouped["Bedrooms"]==index[1])&
		(MGrouped["Bathrooms"]==index[2])&(MGrouped["ReportingMonth"]=="01/07/2018")].values,5)
		OCCResult["AOAugust"]=getValue(MGrouped[(MGrouped["Neighborhood"]==index[0])&(MGrouped["Bedrooms"]==index[1])&
		(MGrouped["Bathrooms"]==index[2])&(MGrouped["ReportingMonth"]=="01/08/2018")].values,5)
		OCCResult["AOSeptember"] =getValue(MGrouped[(MGrouped["Neighborhood"]==index[0])&(MGrouped["Bedrooms"]==index[1])&
		(MGrouped["Bathrooms"]==index[2])&(MGrouped["ReportingMonth"]=="01/09/2018")].values,5)
		OCCResult["AOOctober"] =getValue(MGrouped[(MGrouped["Neighborhood"]==index[0])&(MGrouped["Bedrooms"]==index[1])&
		(MGrouped["Bathrooms"]==index[2])&(MGrouped["ReportingMonth"]=="01/10/2018")].values,5)
		OCCResult["AONovember"] =getValue(MGrouped[(MGrouped["Neighborhood"]==index[0])&(MGrouped["Bedrooms"]==index[1])&
		(MGrouped["Bathrooms"]==index[2])&(MGrouped["ReportingMonth"]=="01/11/2018")].values,5)
		OCCResult["AODecember"] =getValue(MGrouped[(MGrouped["Neighborhood"]==index[0])&(MGrouped["Bedrooms"]==index[1])&
		(MGrouped["Bathrooms"]==index[2])&(MGrouped["ReportingMonth"]=="01/12/2018")].values,5)

		AARResultJSON = json.dumps(AARResult)
		OCCResultJSON = json.dumps(OCCResult)
		API_ENDPOINTAAR = "http://localhost:5000/resultAar"
		API_ENDPOINTOCC = "http://localhost:5000/resultOcc"
		headers = {'Content-type': 'application/json'}
		r = requests.post(url = API_ENDPOINTAAR, data = AARResultJSON, headers=headers) 
		r = requests.post(url = API_ENDPOINTOCC, data = OCCResultJSON, headers=headers) 
