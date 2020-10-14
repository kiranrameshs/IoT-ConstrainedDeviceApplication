#####
# 
# This class is part of the Programming the Internet of Things project.
# 
# It is provided as a simple shell to guide the student and assist with
# implementation for the Programming the Internet of Things exercises,
# and designed to be modified by the student as needed.
#

from programmingtheiot.data.SensorData import SensorData

import programmingtheiot.common.ConfigConst as ConfigConst

from programmingtheiot.common.ConfigUtil import ConfigUtil
from programmingtheiot.cda.sim.BaseSensorSimTask import BaseSensorSimTask
from programmingtheiot.cda.sim.SensorDataGenerator import SensorDataGenerator

from pisense import SenseHAT

class PressureSensorEmulatorTask(BaseSensorSimTask):
	"""
	Shell representation of class for student implementation.
	
	"""

	def __init__(self, dataSet = None):
		super(PressureSensorEmulatorTask, self).__init__(SensorData.PRESSURE_SENSOR_TYPE, minVal = SensorDataGenerator.LOW_NORMAL_ENV_PRESSURE, maxVal = SensorDataGenerator.HI_NORMAL_ENV_PRESSURE)
		self.sh = SenseHAT(emulate = True);
		
	def generateTelemetry(self) -> SensorData:
		sensorData = SensorData(sensorType = self.sensorType)
		sensorVal = self.sh.environ.pressure		
		sensorData.setValue(sensorVal)
		self.latestSensorData = sensorData

		return sensorData
