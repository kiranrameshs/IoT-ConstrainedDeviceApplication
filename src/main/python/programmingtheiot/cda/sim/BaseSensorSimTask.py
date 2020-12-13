#####
# 
# This class is part of the Programming the Internet of Things project.
# 
# It is provided as a simple shell to guide the student and assist with
# implementation for the Programming the Internet of Things exercises,
# and designed to be modified by the student as needed.
#

import logging
import random

from programmingtheiot.data.SensorData import SensorData
import programmingtheiot.common.ConfigConst as ConfigConst

class BaseSensorSimTask():
	"""
	Shell representation of class for student implementation.
	"""
	#initialize index and sensorData variables with default
	DEFAULT_MIN_VAL = 0.0
	DEFAULT_MAX_VAL = 1000.0
	dataSet = None
	sensorType = 0
	minVal = 0.0
	maxVal = 0.0
	currentDataIndex=0;
	useRandomizer = True;
	latestSensorData = None;

	def __init__(self, sensorType: int = SensorData.DEFAULT_SENSOR_TYPE, dataSet = None, minVal: float = DEFAULT_MIN_VAL, maxVal: float = DEFAULT_MAX_VAL,
				sensorName = ConfigConst.NOT_SET):
		self.dataSet = dataSet;
		self.sensorType = sensorType;
		self.minVal = minVal
		self.maxVal = maxVal
		self.sensorName = sensorName
	
	'''
	@param : none
	output : SensorData
	description : Initialize the SensorData class and Get random value for sensorData if random flag is enabled
	'''
	def generateTelemetry(self,sensorData:SensorData) -> SensorData:
#		sensorData = SensorData(name = self.sensorName);
#         sensorData.sensorType = self.sensorType;sensorData = SensorData(name = self.sensorName);
# 		sensorData.sensorType = self.sensorType
		if(self.useRandomizer):
			sensorData.setValue(random.uniform(self.minVal, self.maxVal))
		else:
			self.dataSet[self.currentDataIndex]
			#check overflow
			if( self.currentDataIndex+1 <= len(self.dataSet)):
				self.currentDataIndex+=1;
			else:
				self.currentDataIndex = 0;
		self.latestSensorData = sensorData;
		return self.latestSensorData;
	
	'''
	@param : none
	output : sensorData.value
	description :return latest sensorData value else generateTelemetry and then return
	'''
	def getTelemetryValue(self) -> float:
		if(self.latestSensorData != None):
			return self.latestSensorData.getValue();
		else:
			self.generateTelemetry();
			return self.latestSensorData.getValue();
	