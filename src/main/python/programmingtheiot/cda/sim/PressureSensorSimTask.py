#####
# 
# This class is part of the Programming the Internet of Things project.
# 
# It is provided as a simple shell to guide the student and assist with
# implementation for the Programming the Internet of Things exercises,
# and designed to be modified by the student as needed.
#

import logging

from programmingtheiot.cda.sim.BaseSensorSimTask import BaseSensorSimTask
from programmingtheiot.cda.sim.SensorDataGenerator import SensorDataGenerator,\
	SensorDataSet

from programmingtheiot.data.SensorData import SensorData

class PressureSensorSimTask(BaseSensorSimTask):
	"""
	Shell representation of class for student implementation.
	
	"""
	

	def __init__(self, dataSet: SensorDataSet=None):
		super(PressureSensorSimTask, self).__init__(SensorData.PRESSURE_SENSOR_TYPE, dataSet = dataSet, minVal = SensorDataGenerator.LOW_NORMAL_ENV_PRESSURE, maxVal = SensorDataGenerator.HI_NORMAL_ENV_PRESSURE)
	
	def generateTelemetry(self) -> SensorData:
		return super(PressureSensorSimTask, self).generateTelemetry()
	
	def getTelemetryValue(self) -> float:
		return super(PressureSensorSimTask, self).getTelemetryValue()
	