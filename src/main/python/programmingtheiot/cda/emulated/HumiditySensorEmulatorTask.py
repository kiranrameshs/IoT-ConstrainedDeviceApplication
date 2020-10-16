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

class HumiditySensorEmulatorTask(BaseSensorSimTask):

	def __init__(self, dataSet = None):
		super(HumiditySensorEmulatorTask, self).__init__(SensorData.HUMIDITY_SENSOR_TYPE, minVal = SensorDataGenerator.LOW_NORMAL_ENV_HUMIDITY, maxVal = SensorDataGenerator.HI_NORMAL_ENV_HUMIDITY)
		self.configUtil = ConfigUtil()
		senseHatKey = self.configUtil.getBoolean(ConfigConst.CONSTRAINED_DEVICE, ConfigConst.ENABLE_SENSE_HAT_KEY);
		if(senseHatKey):
			enableEmulation = False;
		else:
			enableEmulation = True;
		self.sh = SenseHAT(emulate = enableEmulation)
		
	'''
	@param : none
	output : SensorData
	description : Use the respective SenseHat API to get the value 
	'''
	def generateTelemetry(self) -> SensorData:
		sensorData = SensorData(sensorType = self.sensorType)
		sensorVal = self.sh.environ.humidity		
		sensorData.setValue(sensorVal)
		self.latestSensorData = sensorData
		return sensorData
