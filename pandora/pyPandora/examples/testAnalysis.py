#!/usr/bin/python3

import sys, random
sys.path.append('..')
sys.path.append('../../')
from pyPandora import Simulation, Agent, World, Point2DInt, SimulationRecord, GlobalAgentStats, AgentNum, AgentMean, AgentSum, AgentStdDev, GlobalRasterStats, RasterMean, RasterSum, SizeInt

# data generation

class MyAgent(Agent):
	_value = 0
	def __init__(self, id):
		Agent.__init__( self, id)

	def registerAttributes(self):
		self.registerIntAttribute('value');

	def updateState(self):
		newPosition = Point2DInt(self.position._x + random.randint(-1,1), self.position._y + random.randint(-1,1))
		if self.getWorld().checkPosition(newPosition):
			self.position = newPosition

	def serialize(self):
		self.serializeIntAttribute('value', self._value);

class MyWorld(World):
	def __init__(self, simulation ):
		World.__init__( self, simulation)

	def createRasters(self):		
		self.registerDynamicRaster("test", 1)
		self.getDynamicRaster("test").setInitValues(0, 10, 0)

	def createAgents(self):
		for i in range (0, 10):
			newAgent = MyAgent('id_'+str(i))
			self.addAgent(newAgent)
			newAgent.setRandomPosition()
			newAgent._value = random.randint(0,10)

mySimulation = Simulation(SizeInt(32,32), 10)
myWorld = MyWorld(mySimulation)
myWorld.initialize()
myWorld.run()

# analysis

record = SimulationRecord(1, False)
record.loadHDF5('data/results.h5', True, True)

agentResults = GlobalAgentStats(';')
agentResults.addAnalysis(AgentNum())
agentResults.addAnalysis(AgentMean('x'))
agentResults.addAnalysis(AgentMean('y'))
agentResults.addAnalysis(AgentMean('value'))
agentResults.addAnalysis(AgentSum('value'))
agentResults.applyTo(record, 'agents.csv', 'id')
#agentResults.addAnalysis(AgentHDFtoSHP('shp/agents.shp', -1))

rasterResults = GlobalRasterStats(';')
rasterResults.addAnalysis(RasterMean())
rasterResults.addAnalysis(RasterSum())
rasterResults.applyTo(record, 'resources.csv', 'test')

