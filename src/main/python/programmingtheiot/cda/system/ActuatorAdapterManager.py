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
	def __init__(self, useEmulator: bool = True):
		self.dataMessageListener = None;
		self.useEmulator = useEmulator;
		if(self.useEmulator):
			logging.info("Using Emulators")
			# load the Humidifier actuation emulator
			humidifierModule = __import__('programmingtheiot.cda.emulated.HumidifierEmulatorTask', fromlist = ['HumidifierEmulatorTask'])
			hueClazz = getattr(humidifierModule, 'HumidifierEmulatorTask')
			self.humidifierEmulator = hueClazz()
			# load the HVac actuation emulator
			hvacModule = __import__('programmingtheiot.cda.emulated.HvacEmulatorTask', fromlist = ['HvacEmulatorTask'])
			hvacClazz = getattr(hvacModule, 'HvacEmulatorTask')
			self.hvacEmulator = hvacClazz()
			# load the LED actuation emulator
			LEDModule = __import__('programmingtheiot.cda.emulated.LedDisplayEmulatorTask', fromlist = ['LedDisplayEmulatorTask'])
			ledClazz = getattr(LEDModule, 'LedDisplayEmulatorTask')
			self.ledEmulator = ledClazz()
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
			if(data.actuatorType == 1):
				logging.info("Emulating HVAC Actuator "+str(data.getCommand())+" HVAC VALUE -> "+str(data.getValue()))
				self.hvacEmulator.updateActuator(data);
# 				self.ledEmulator.updateActuator(data);
				return True;
			elif(data.actuatorType == 2):
				logging.info("Emulating HUMIDIFIER Actuator "+str(data.getCommand())+" HUMIDIFIER VALUE -> "+str(data.getValue()))
				self.humidifierEmulator.updateActuator(data);	
				return True
			elif(data.actuatorType == 3):
				logging.info("Emulating LED Actuator "+str(data.getCommand())+" HUMIDIFIER VALUE -> "+str(data.getValue()))
				self.ledEmulator.updateActuator(data);	
				return True
			else:
				return False
				
	def setDataMessageListener(self, listener: IDataMessageListener) -> bool:
		if(self.dataMessageListener== None):
			self.dataMessageListener = listener;
			return True;
		else:
			return False;
