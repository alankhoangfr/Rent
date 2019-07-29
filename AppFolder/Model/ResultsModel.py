from AppFolder import db, ma

# Results Annual Revenue

class ResultsAAR(db.Model):
	__tablename__ = 'ResultsAAR'
	localityId = db.Column(db.Integer, primary_key=True)
	suburb = db.Column(db.String(60))
	bedrooms =db.Column(db.Integer, nullable=False)
	bathrooms =db.Column(db.Integer, nullable=False)
	AAR  = db.Column(db.Float)
	numberOfHouses = db.Column(db.Integer)
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
	AARJnue = db.Column(db.Float)
	AARJuly = db.Column(db.Float)
	AARAugust = db.Column(db.Float)
	AARSeptember =db.Column(db.Float)
	AAROctober =db.Column(db.Float)
	AARNovember =db.Column(db.Float)
	AARDecember =db.Column(db.Float)

	def __init__(self,suburb, bedrooms, bathrooms,AAR,numberOfHouses,AARAppartment,NumberAARAppartment,AARHouse,NumberAARHouse,
		AAR75Percentile,AAR50Percentile,HighestType,AARJanuary,AARFebuary,AARMarch,AARApril,AARMay,AARJnue,AARJuly,AARAugust,
		AARSeptember,AAROctober,AARNovember,AARDecember):

		self.suburb = suburb
		self.bedrooms = bedrooms
		self.bathrooms = bathrooms
		self.AAR = AAR 
		self.numberOfHouses = numberOfHouses
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
		self.AARJnue = AARJnue
		self.AARJuly = AARJuly
		self.AARAugust = AARAugust
		self.AARSeptember = AARSeptember
		self.AAROctober = AAROctober
		self.AARNovember = AARNovember
		self.AARDecember = AARDecember

# Results Annual Revenue Schema
class ResultsAARSchema(ma.Schema):
	class Meta:
		fields = ('localityId','suburb', 'bedrooms', 'bathrooms','AAR','numberOfHouses','NumberAARHouse','AARAppartment','AARHouse','NumberAARHouse',
			'AAR75Percentile','AAR50Percentile','HighestType','AARJanuary','AARFebuary','AARMarch','AARApril','AARMay','AARJnue',
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
	AOJnue = db.Column(db.Float)
	AOJuly = db.Column(db.Float)
	AOAugust = db.Column(db.Float)
	AOSeptember =db.Column(db.Float)
	AOOctober =db.Column(db.Float)
	AONovember =db.Column(db.Float)
	AODecember =db.Column(db.Float)

	def __init__(self, suburb, bedrooms, bathrooms,AverageOccupancy,AO75Percentile,AO50Percentile,AOJanuary,AOFebuary,AOMarch
		,AOApril,AOMay,AOJnue,AOJuly,AOAugust,AOSeptember,AOOctober,AONovember,AODecember):

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
		self.AOJnue = AOJnue
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
			'AO75Percentile','AO50Percentile','AOJanuary','AOFebuary','AOMarch','AOApril','AOMay','AOJnue','AOJuly',
			'AOAugust','AOSeptember','AOOctober','AONovember','AODecember')

# Init schema
ResultsOccupancy_schema = ResultsOccupancySchema(strict=True)
ResultsOccupancys_schema = ResultsOccupancySchema(many=True, strict=True)


#LocalityAgent


class LocalityAgent(db.Model):
	__tablename__ = 'LocalityAgent'
	localityId = db.Column(db.Integer,db.ForeignKey('LocalityRent.localityId'), primary_key=True)
	agentId = db.Column(db.Integer,db.ForeignKey('Agent.agentId'), primary_key=True)
	localityRent = db.relationship("LocalityRent",back_populates="agents")
	agent = db.relationship("Agent",back_populates = "localityRents")

	def __init__(self,LocalityAgentId, localityId, agentId):
		self.LocalityAgentId = LocalityAgentId
		self.localityId = localityId
		self.agentId = agentId

# Agent Schema
class LocalityAgentSchema(ma.Schema):
	class Meta:
		fields = ('LocalityAgentId', 'localityId', 'agentId')

# Init schema
LocalityAgent_schema = LocalityAgentSchema(strict=True)
LocalityAgents_schema = LocalityAgentSchema(many=True, strict=True)



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
	numberOfHouses = db.Column(db.Integer)
	agents = db.relationship("LocalityAgent",back_populates="localityRent")


	def __init__(self, localityId, suburb, bedrooms, bathrooms,averageRent,averageRent75Percentile,averageRent50Percentile,numberOfHouses):
		self.localityId = localityId
		self.suburb = suburb
		self.bedrooms = bedrooms
		self.bathrooms = bathrooms
		self.averageRent  = averageRent
		self.averageRent75Percentile = averageRent75Percentile
		self.averageRent50Percentile =averageRent50Percentile
		self.numberOfHouses = numberOfHouses

# ResultsOccupancy Schema
class LocalityRentSchema(ma.Schema):
	class Meta:
		fields = ('LocalityRentId,''localityId', 'suburb', 'bedrooms', 'bathrooms','averageRent','averageRent75Percentile','averageRent50Percentile','numberOfHouses')

# Init schema
LocalityRent_schema = LocalityRentSchema(strict=True)
LocalityRents_schema = LocalityRentSchema(many=True, strict=True)



#ResultAgentNumber

class Agent(db.Model):
	__tablename__ = 'Agent'
	agentId = db.Column(db.Integer, primary_key=True)
	agentName = db.Column(db.String(60))
	localityRents = db.relationship("LocalityAgent",back_populates="agent")


	def __init__(self, agentName):
		self.agentName = agentName

# ResultsOccupancy Schema
class AgentSchema(ma.Schema):
	class Meta:
		fields = ('agentId', 'agentName')

# Init schema
Agent_schema = AgentSchema(strict=True)
Agents_schema = AgentSchema(many=True, strict=True)
