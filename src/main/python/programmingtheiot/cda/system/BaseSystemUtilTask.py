#####
# 
# This class is part of the Programming the Internet of Things project.
# 
# It is provided as a simple shell to guide the student and assist with
# implementation for the Programming the Internet of Things exercises,
# and designed to be modified by the student as needed.
#

from programmingtheiot.data.SensorData import SensorData
import logging
class BaseSystemUtilTask():
	"""
	Shell representation of class for student implementation.
	
	"""
	
	def __init__(self):
		self.latestSensorData = None
		
		pass
	
	def generateTelemetry(self) -> SensorData:
		"""
		Get latest sensor data using getsystemUtil methpd from respective derived classes
		@return: Latest Sensor Data
		"""
		self.latestSensorData = SensorData();
		self.latestSensorData.setValue(self._getSystemUtil());
		return self.latestSensorData;
		
	def getTelemetryValue(self) -> float:
		if(self.latestSensorData.getValue()):
			val = self.latestSensorData.getValue();
		else:
			sd = self.generateTelemetry();
			val = sd.getValue();
		return val
	
	def _getSystemUtil(self) -> float:
		"""
		Template method implemented by sub-class.
		
		Retrieve the system utilization value as a float.
		
		@return float
		"""
		pass
		