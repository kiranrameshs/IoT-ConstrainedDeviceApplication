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
	
	"""
	@param : ActuatorData
	description : Call the handleActuation function with command and value
	"""
	def updateActuator(self, data: ActuatorData) -> bool:
		if(data):
			self._handleActuation(data.getCommand(),data.getValue(),data.getStateData());
			self.actuatorData = data;
			self.actuatorData.setStatusCode(data.getStatusCode());
			self.actuatorData.setAsResponse();
			return True
		else:
			return False;
	
	"""
	Simple implementation that invokes activate or deactivate in super class.
	@param cmd The actuation command to process.
	@param stateData The string state data to use in processing the command.
	@return int The status code from the actuation call.
	"""	
	def _handleActuation(self, cmd: int, val: float = 0.0, stateData: str = None) -> int:
		if cmd is ActuatorData.COMMAND_ON:
			self.activateActuator(val)
		elif cmd is ActuatorData.COMMAND_OFF:
			self.deactivateActuator()
		
		return 0
		