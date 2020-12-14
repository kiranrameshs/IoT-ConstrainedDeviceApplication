#####
# 
# This class is part of the Programming the Internet of Things project.
# 
# It is provided as a simple shell to guide the student and assist with
# implementation for the Programming the Internet of Things exercises,
# and designed to be modified by the student as needed.
#

from programmingtheiot.data.BaseIotData import BaseIotData
import programmingtheiot.common.ConfigConst as ConfigConst
class ActuatorData(BaseIotData):
	"""
	Class with attributes, data and methods for Actuator data
	
	"""
	DEFAULT_COMMAND = 0
	COMMAND_OFF = DEFAULT_COMMAND
	COMMAND_ON = 1

	# for now, actuators will be 1..99
	# and displays will be 100..1999
	DEFAULT_ACTUATOR_TYPE = 0
	
	HVAC_ACTUATOR_TYPE = 1
	HUMIDIFIER_ACTUATOR_TYPE = 2
	CAMERA_ACTUATOR_TYPE = 3
	LED_DISPLAY_ACTUATOR_TYPE = 100

	def __init__(self, actuatorType: int = DEFAULT_ACTUATOR_TYPE, name = ConfigConst.NOT_SET, d = None):
		"""
		Constructor.
		
		@param d Defaults to None. The data (dict) to use for setting all parameters.
		It's provided here as a convenience - mostly for testing purposes. The utility
		in DataUtil should be used instead.
		"""
# 		print("name is "+str(name))
		super(ActuatorData, self).__init__(name = name, d = d)
		
		self.isResponse = False
		self.actuatorType = actuatorType
		
		if d:
			self.command = d['command']
			self.stateData = d['stateData']
			self.curValue = d['curValue']
			self.actuatorType = d['actuatorType']
		else:
			self.command = self.DEFAULT_COMMAND
			self.stateData = None
			self.curValue = self.DEFAULT_VAL
			self.actuatorType = actuatorType
	
	def getCommand(self) -> int:
		return self.command;
	
	def getActuatorType(self) -> int:
		return self.actuatorType;
	
	def setActuatorType(self, actuatorType: int):
		self.actuatorType = actuatorType;
	
	def getStateData(self) -> str:
		return self.stateData;
	
	def getValue(self) -> float:
		return self.curValue
	
	def isResponseFlagEnabled(self) -> bool:
		return False
	
	def setCommand(self, command: int):
		self.command = command
	
	def setAsResponse(self):
		pass
		
	def setStateData(self, stateData: str):
		self.stateData = stateData;
	
	def setValue(self, val: float):
		self.curValue = val;
		
	def _handleUpdateData(self, data):
		self.command = data.getCommand();
		self.curValue = data.getValue();
		self.stateData = data.getStateData();
		
		