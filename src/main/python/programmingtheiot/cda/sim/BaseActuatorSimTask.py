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

from programmingtheiot.data.ActuatorData import ActuatorData
#from builtins import True

class BaseActuatorSimTask():
	"""
	Shell representation of class for student implementation.
	
	"""
	
	
	def __init__(self, actuatorType: int = ActuatorData.DEFAULT_ACTUATOR_TYPE, simpleName: str = "Actuator"):
		self.actuatorType = actuatorType;
		self.simpleName = simpleName;
		self.actuatorData = ActuatorData();
		
	def activateActuator(self, val: float) -> bool:
		logging.info("ON command sent to actuator "+str(val))
		self.actuatorData.setCommand(ActuatorData.COMMAND_ON);
		
	def deactivateActuator(self) -> bool:
		logging.info("OFF command sent to actuator ")
		self.actuatorData.setCommand(ActuatorData.COMMAND_OFF);
		
	def getLatestActuatorResponse(self) -> ActuatorData:
		return self.actuatorData;
	
	def getSimpleName(self) -> str:
		return self.simpleName;
	
	def updateActuator(self, data: ActuatorData) -> bool:
		if(data):
			if(data.getCommand() == 1):
				self.activateActuator(data.getValue())
			elif(data.getCommand() == 0):
				self.deactivateActuator()
			self.actuatorData = data;
			self.actuatorData.setStatusCode(data.getStatusCode());
			self.actuatorData.setAsResponse();
			return True
		else:
			return False;
		