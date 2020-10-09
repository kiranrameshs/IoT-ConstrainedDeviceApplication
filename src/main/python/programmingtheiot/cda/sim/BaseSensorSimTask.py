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

class BaseSensorSimTask():
	"""
	Shell representation of class for student implementation.
	
	"""

	DEFAULT_MIN_VAL = 0.0
	DEFAULT_MAX_VAL = 1000.0
	dataSet = None
	sensorType = 0
	minVal = 0.0
	maxVal = 0.0
	#initialize index and sensorData variables with default
	currentDataIndex=0;
	useRandomizer = True;
	latestSensorData = None;

	
	def __init__(self, sensorType: int = SensorData.DEFAULT_SENSOR_TYPE, dataSet = None, minVal: float = DEFAULT_MIN_VAL, maxVal: float = DEFAULT_MAX_VAL):
		self.dataSet = dataSet;
		self.sensorType = sensorType;
		self.minVal = minVal
		self.maxVal = maxVal
		#if(dataSet == None):
			#self.useRandomizer = True;
		#else:
			#self.useRandomizer  = False;
	
	def generateTelemetry(self) -> SensorData:
		#Initialize the SensorData class
		sensorData = SensorData();
		#Set current sensorType
		sensorData.sensorType = self.sensorType;
		
		#Get random value for sensorData if random flag is enabled
		if(self.useRandomizer):
			sensorData.setValue(random.uniform(self.minVal, self.maxVal))
			print("Set random value "+str(sensorData.getValue()))
		else:
			self.dataSet[self.currentDataIndex]
			#check overflow
			if( self.currentDataIndex+1 <= len(self.dataSet)):
				self.currentDataIndex+=1;
			else:
				self.currentDataIndex = 0;
		self.latestSensorData = sensorData;
		return self.latestSensorData;
	
	def getTelemetryValue(self) -> float:
		if(self.latestSensorData != None):
			return self.latestSensorData.getValue();
		else:
			self.generateTelemetry();
			return self.latestSensorData.getValue();
		#pass
	