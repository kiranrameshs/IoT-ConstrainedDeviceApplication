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

from programmingtheiot.cda.emulated.MotionDetection_SensorData import MotionDetection_SensorData

class CameraSensorEmulatorTask(BaseSensorSimTask):
	"""
	
	
	"""

	def __init__(self, dataSet = None):
		super(CameraSensorEmulatorTask, self).__init__(SensorData.CAMERA_SENSOR_TYPE, minVal = SensorDataGenerator.LOW_NORMAL_CAMERA, maxVal = SensorDataGenerator.HI_NORMAL_CAMERA)
		self.configUtil = ConfigUtil()
		cameraKey = self.configUtil.getBoolean(ConfigConst.CONSTRAINED_DEVICE, ConfigConst.ENABLE_CAMERA_KEY);
		self.cm =  MotionDetection_SensorData()
		
	'''
	@param : SensorData
	output : N/A
	description : generate the telemetry
	'''	
	def generateTelemetry(self) -> SensorData:
		sensorData = SensorData(name = ConfigConst.CAMERA_SENSOR_NAME, sensorType = self.sensorType)
		print("XXXXX Getting Camera sensor value XXXXX")
		sensorVal = self.cm.detect_motion("example.mp4")
		print("XXXXX got Camera sensor value XXXXX")		
		sensorData.setValue(sensorVal)
		self.latestSensorData = sensorData
		return sensorData
