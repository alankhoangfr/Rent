from AppFolder import db, ma

# Results Annual Revenue

class ResultsAAR(db.Model):
	__tablename__ = 'ResultsAAR'
	localityId = db.Column(db.Integer, primary_key=True)
	suburb = db.Column(db.String(60))
	bedrooms =db.Column(db.Integer, nullable=False)
	bathrooms =db.Column(db.Integer, nullable=False)
	AAR  = db.Column(db.Float)
	numberOfProperty = db.Column(db.Integer)
	AARAppartment  = db.Column(db.Float)
	NumberAARAppartment  = db.Column(db.Integer)
	AARHouse  = db.Column(db.Float)
	NumberAARHouse  = db.Column(db.Integer)	
	AAR75Percentile = db.Column(db.Float)
	AAR50Percentile = db.Column(db.Float)
	HighestType = db.Column(db.String(60))
	AARJanuary = db.Column(db.Float)
	AARFebuary = db.Column(db.Float)
	AARMarch =db.Column(db.Float)
	AARApril = db.Column(db.Float)
	AARMay = db.Column(db.Float)
	AARJune = db.Column(db.Float)
	AARJuly = db.Column(db.Float)
	AARAugust = db.Column(db.Float)
	AARSeptember =db.Column(db.Float)
	AAROctober =db.Column(db.Float)
	AARNovember =db.Column(db.Float)
	AARDecember =db.Column(db.Float)

	def __init__(self,suburb, bedrooms, bathrooms,AAR,numberOfProperty,AARAppartment,NumberAARAppartment,AARHouse,NumberAARHouse,
		AAR75Percentile,AAR50Percentile,HighestType,AARJanuary,AARFebuary,AARMarch,AARApril,AARMay,AARJune,AARJuly,AARAugust,
		AARSeptember,AAROctober,AARNovember,AARDecember):

		self.suburb = suburb
		self.bedrooms = bedrooms
		self.bathrooms = bathrooms
		self.AAR = AAR 
		self.numberOfProperty = numberOfProperty
		self.AARAppartment = AARAppartment
		self.NumberAARAppartment = NumberAARAppartment
		self.AARHouse = AARHouse
		self.NumberAARHouse = NumberAARHouse
		self.AAR75Percentile = AAR75Percentile
		self.AAR50Percentile =AAR50Percentile
		self.HighestType=HighestType
		self.AARJanuary = AARJanuary
		self.AARFebuary = AARFebuary
		self.AARMarch = AARMarch
		self.AARApril = AARApril
		self.AARMay = AARMay
		self.AARJune = AARJune
		self.AARJuly = AARJuly
		self.AARAugust = AARAugust
		self.AARSeptember = AARSeptember
		self.AAROctober = AAROctober
		self.AARNovember = AARNovember
		self.AARDecember = AARDecember

# Results Annual Revenue Schema
class ResultsAARSchema(ma.Schema):
	class Meta:
		fields = ('localityId','suburb', 'bedrooms', 'bathrooms','AAR','numberOfProperty','NumberAARHouse','AARAppartment','AARHouse','NumberAARHouse',
			'AAR75Percentile','AAR50Percentile','HighestType','AARJanuary','AARFebuary','AARMarch','AARApril','AARMay','AARJune',
			'AARJuly','AARAugust','AARSeptember','AAROctober','AARNovember','AARDecember')

# Init schema
ResultsAAR_schema = ResultsAARSchema(strict=True)
ResultsAARs_schema = ResultsAARSchema(many=True, strict=True)


# ResultsOccupancy

class ResultsOccupancy(db.Model):
	__tablename__ = 'ResultsOccupancy'
	localityId = db.Column(db.Integer, primary_key=True)
	suburb = db.Column(db.String(60))
	bedrooms =db.Column(db.Integer, nullable=False)
	bathrooms =db.Column(db.Integer, nullable=False)
	AverageOccupancy  = db.Column(db.Float)
	AO75Percentile = db.Column(db.Float)
	AO50Percentile = db.Column(db.Float)
	AOJanuary = db.Column(db.Float)
	AOFebuary = db.Column(db.Float)
	AOMarch =db.Column(db.Float)
	AOApril = db.Column(db.Float)
	AOMay = db.Column(db.Float)
	AOJune = db.Column(db.Float)
	AOJuly = db.Column(db.Float)
	AOAugust = db.Column(db.Float)
	AOSeptember =db.Column(db.Float)
	AOOctober =db.Column(db.Float)
	AONovember =db.Column(db.Float)
	AODecember =db.Column(db.Float)

	def __init__(self, suburb, bedrooms, bathrooms,AverageOccupancy,AO75Percentile,AO50Percentile,AOJanuary,AOFebuary,AOMarch
		,AOApril,AOMay,AOJune,AOJuly,AOAugust,AOSeptember,AOOctober,AONovember,AODecember):

		self.suburb = suburb
		self.bedrooms = bedrooms
		self.bathrooms = bathrooms
		self.AverageOccupancy = AverageOccupancy
		self.AO75Percentile = AO75Percentile
		self.AO50Percentile =AO50Percentile
		self.AOJanuary = AOJanuary
		self.AOFebuary = AOFebuary
		self.AOMarch = AOMarch
		self.AOApril = AOApril
		self.AOMay = AOMay
		self.AOJune = AOJune
		self.AOJuly = AOJuly
		self.AOAugust = AOAugust
		self.AOSeptember = AOSeptember
		self.AOOctober = AOOctober
		self.AONovember = AONovember
		self.AODecember = AODecember

# ResultsOccupancy Schema
class ResultsOccupancySchema(ma.Schema):
	class Meta:
		fields = ('localityId', 'bedrooms', 'bathrooms','suburb','AverageOccupancy',
			'AO75Percentile','AO50Percentile','AOJanuary','AOFebuary','AOMarch','AOApril','AOMay','AOJune','AOJuly',
			'AOAugust','AOSeptember','AOOctober','AONovember','AODecember')

# Init schema
ResultsOccupancy_schema = ResultsOccupancySchema(strict=True)
ResultsOccupancys_schema = ResultsOccupancySchema(many=True, strict=True)


#LocalityAgent


association_table = db.Table('LocalityAgent',
    db.Column('localityId', db.Integer, db.ForeignKey('LocalityRent.localityId')),
    db.Column('agentId', db.Integer, db.ForeignKey('Agent.agentId'))
)


# ResultsRent

class LocalityRent(db.Model):
	__tablename__ = 'LocalityRent'
	LocalityRentId = db.Column(db.Integer, primary_key=True)
	localityId = db.Column(db.Integer)
	suburb = db.Column(db.String(60))
	bedrooms =db.Column(db.Integer, nullable=False)
	bathrooms =db.Column(db.Integer, nullable=False)
	averageRent =db.Column(db.Float)
	averageRent75Percentile = db.Column(db.Float)
	averageRent50Percentile = db.Column(db.Float)
	numberOfProperty = db.Column(db.Integer)
	agents = db.relationship("Agent",secondary="LocalityAgent", backref="LocalityRent",lazy ="select")


	def __init__(self, localityId, suburb, bedrooms, bathrooms,averageRent,averageRent75Percentile,averageRent50Percentile,numberOfProperty):
		self.localityId = localityId
		self.suburb = suburb
		self.bedrooms = bedrooms
		self.bathrooms = bathrooms
		self.averageRent  = averageRent
		self.averageRent75Percentile = averageRent75Percentile
		self.averageRent50Percentile =averageRent50Percentile
		self.numberOfProperty = numberOfProperty

# ResultsOccupancy Schema
class LocalityRentSchema(ma.Schema):
	class Meta:
		fields = ('LocalityRentId,''localityId', 'suburb', 'bedrooms', 'bathrooms','averageRent','averageRent75Percentile','averageRent50Percentile','numberOfProperty')

# Init schema
LocalityRent_schema = LocalityRentSchema(strict=True)
LocalityRents_schema = LocalityRentSchema(many=True, strict=True)



#ResultAgentNumber

class Agent(db.Model):
	__tablename__ = 'Agent'
	agentId = db.Column(db.Integer, primary_key=True)
	agentName = db.Column(db.String(60))
	

	def __init__(self, agentName):
		self.agentName = agentName

# ResultsOccupancy Schema
class AgentSchema(ma.Schema):
	class Meta:
		fields = ('agentId', 'agentName')

# Init schema
Agent_schema = AgentSchema(strict=True)
Agents_schema = AgentSchema(many=True, strict=True)


class LocalityAgentBedrooms(db.Model):
	__tablename__="LocalityAgentBedrooms"
	LocalityAgentBedroomsId = db.Column(db.Integer, primary_key=True)
	localityId = db.Column(db.Integer)
	suburb = db.Column(db.String(60))
	bedrooms =db.Column(db.Integer, nullable=False)
	bathrooms =db.Column(db.Integer, nullable=False)
	agentName = db.Column(db.String(60))
	averageRent =db.Column(db.Float)
	averageRent75Percentile = db.Column(db.Float)
	averageRent50Percentile = db.Column(db.Float)
	numberOfProperty = db.Column(db.Integer)
	
	def __init__(self, localityId, suburb, bedrooms, bathrooms,agentName,averageRent,averageRent75Percentile,averageRent50Percentile,numberOfProperty):
		self.localityId = localityId
		self.suburb = suburb
		self.bedrooms = bedrooms
		self.bathrooms = bathrooms
		self.agentName=agentName
		self.averageRent  = averageRent
		self.averageRent75Percentile = averageRent75Percentile
		self.averageRent50Percentile =averageRent50Percentile
		self.numberOfProperty = numberOfProperty

# ResultsOccupancy Schema
class LocalityAgentBedroomsSchema(ma.Schema):
	class Meta:
		fields = ('LocalityRentId,''localityId', 'suburb', 'bedrooms', 'bathrooms','agentName','averageRent','averageRent75Percentile','averageRent50Percentile','numberOfProperty')

# Init schema
LocalityAgentBedrooms_schema = LocalityAgentBedroomsSchema(strict=True)
LocalityAgentBedroomss_schema = LocalityAgentBedroomsSchema(many=True, strict=True)