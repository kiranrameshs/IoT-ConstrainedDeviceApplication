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
import programmingtheiot.common.ConfigConst as ConfigConst
class HumiditySensorSimTask(BaseSensorSimTask):
	"""
	Shell representation of class for student implementation.
	
	"""

	def __init__(self,dataset: SensorDataSet=None):
		super(HumiditySensorSimTask, self).__init__(SensorData.HUMIDITY_SENSOR_TYPE, dataSet = dataset, minVal = SensorDataGenerator.LOW_NORMAL_ENV_HUMIDITY, maxVal = SensorDataGenerator.HI_NORMAL_ENV_HUMIDITY,sensorName = ConfigConst.HUMIDITY_SENSOR_NAME)
	
	"""
	return the value from generateTelemetry() from parent class
	"""
	def generateTelemetry(self) -> SensorData:
		sensorData = SensorData(name = ConfigConst.HUMIDITY_SENSOR_NAME, sensorType = self.sensorType)
		return super(HumiditySensorSimTask, self).generateTelemetry(sensorData)
		
	"""
	return the telemetry value
	"""	
	def getTelemetryValue(self) -> float:
		return super(HumiditySensorSimTask, self).getTelemetryValue()
	