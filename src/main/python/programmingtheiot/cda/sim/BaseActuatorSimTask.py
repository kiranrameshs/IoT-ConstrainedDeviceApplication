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
import programmingtheiot.common.ConfigConst as ConfigConst

class BaseActuatorSimTask():
	"""
	Shell representation of class for student implementation.
	
	"""
	
	
	def __init__(self, actuatorType: int = ActuatorData.DEFAULT_ACTUATOR_TYPE, simpleName: str = "Actuator", actuatorName = ConfigConst.NOT_SET):
		self.actuatorType = actuatorType;
		self.simpleName = simpleName;
		logging.info(" actuatorName is "+str(actuatorName))
		self.latestActuatorData= ActuatorData(name=actuatorName);
		
	'''
	@param : value
	output : N/A
	description : Activate the actuator
	'''		
	def activateActuator(self, val: float) -> bool:
		logging.info("ON command sent to actuator "+str(val))
		self.latestActuatorData.setCommand(ActuatorData.COMMAND_ON)
		return True
		
	'''
	@param : value
	output : bool
	description : deactivate the actuator
	'''		
	def deactivateActuator(self) -> bool:
		logging.info("OFF command sent to actuator ")
		self.latestActuatorData.setCommand(ActuatorData.COMMAND_OFF)
		return True
	
	'''
	@param : N/A
	output : ActuatorData
	description : get the response
	'''			
	def getLatestActuatorResponse(self) -> ActuatorData:
		return self.latestActuatorData
	
	def getSimpleName(self) -> str:
		return self.simpleName;
	
	"""
	@param : ActuatorData
	description : Call the handleActuation function with command and value
	"""
	def updateActuator(self, data: ActuatorData) -> bool:
		if(data):
			self._handleActuation(data.getCommand(),data.getValue(),data.getStateData());
			self.latestActuatorData = data
			self.latestActuatorData.setStatusCode(data.getStatusCode())
			self.latestActuatorData.setAsResponse()	
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
		