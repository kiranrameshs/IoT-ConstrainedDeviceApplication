#####
# 
# This class is part of the Programming the Internet of Things project.
# 
# It is provided as a simple shell to guide the student and assist with
# implementation for the Programming the Internet of Things exercises,
# and designed to be modified by the student as needed.
#

import logging

from programmingtheiot.common.IDataMessageListener import IDataMessageListener

from programmingtheiot.data.ActuatorData import ActuatorData
from programmingtheiot.cda.sim.HumidifierActuatorSimTask import HumidifierActuatorSimTask
from programmingtheiot.cda.sim.HvacActuatorSimTask import HvacActuatorSimTask

class ActuatorAdapterManager(object):
	"""
	Shell representation of class for student implementation.
	
	"""
	
	def __init__(self, useEmulator: bool = False):
		self.dataMessageListener = None;
		self.useEmulator = useEmulator;
		
		if(self.useEmulator):
			logging.info("Using Emulators")
		else:
			logging.info("Using Simulators")
			#initialize the actuators
			self.humidifierActautor = HumidifierActuatorSimTask()
			self.hvacActuator = HvacActuatorSimTask()

	def sendActuatorCommand(self, data: ActuatorData) -> bool:
		
		if(self.useEmulator != True):
			if(data.actuatorType == 1):
				logging.info("Simulating HVAC Actuator "+str(data.getCommand())+" HVAC VALUE -> "+str(data.getValue()))
				self.hvacActuator.updateActuator(data);
				return True;
			elif(data.actuatorType == 2):
				logging.info("Simulating HUMIDIFIER Actuator "+str(data.getCommand())+" HUMIDIFIER VALUE -> "+str(data.getValue()))
				self.humidifierActautor.updateActuator(data);	
				return True
			else:
				False
		else:
			pass;
				
	def setDataMessageListener(self, listener: IDataMessageListener) -> bool:
		if(self.dataMessageListener== None):
			self.dataMessageListener = listener;
			return True;
		else:
			return False;
