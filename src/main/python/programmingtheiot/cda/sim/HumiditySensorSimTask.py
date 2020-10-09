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

class HumiditySensorSimTask(BaseSensorSimTask):
	"""
	Shell representation of class for student implementation.
	
	"""
	
	def __init__(self, dataSet: SensorDataSet=None):
		super(HumiditySensorSimTask, self).__init__(SensorData.HUMIDITY_SENSOR_TYPE, dataSet = dataSet, minVal = SensorDataGenerator.LOW_NORMAL_ENV_HUMIDITY, maxVal = SensorDataGenerator.HI_NORMAL_ENV_HUMIDITY)
	
	def generateTelemetry(self) -> SensorData:
		return super(HumiditySensorSimTask, self).generateTelemetry()
	
	def getTelemetryValue(self) -> float:
		return super(HumiditySensorSimTask, self).getTelemetryValue()
	