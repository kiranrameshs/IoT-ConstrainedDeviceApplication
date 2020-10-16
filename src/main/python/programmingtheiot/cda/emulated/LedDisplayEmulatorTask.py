#####
# 
# This class is part of the Programming the Internet of Things project.
# 
# It is provided as a simple shell to guide the student and assist with
# implementation for the Programming the Internet of Things exercises,
# and designed to be modified by the student as needed.
#

import logging

import programmingtheiot.common.ConfigConst as ConfigConst

from programmingtheiot.common.ConfigUtil import ConfigUtil
from programmingtheiot.data.ActuatorData import ActuatorData
from programmingtheiot.cda.sim.BaseActuatorSimTask import BaseActuatorSimTask

from pisense import SenseHAT

class LedDisplayEmulatorTask(BaseActuatorSimTask):
	"""
	Shell representation of class for student implementation.
	
	"""
	def __init__(self):
		super(LedDisplayEmulatorTask, self).__init__(actuatorType = ActuatorData.LED_DISPLAY_ACTUATOR_TYPE, simpleName = "LED_Display")
		self.configUtil = ConfigUtil()
		senseHatKey = self.configUtil.getBoolean(ConfigConst.CONSTRAINED_DEVICE, ConfigConst.ENABLE_SENSE_HAT_KEY);
		if(senseHatKey):
			enableEmulation = False;
		else:
			enableEmulation = True;
		self.sh = SenseHAT(emulate = enableEmulation)

	'''
	@param : cmd, val, stateData
	output : none
	description : Display stateData if command is ON else clear display 
	'''
	def _handleActuation(self, cmd: int, val: float = 0.0, stateData: str = None) -> int:
			if cmd == ActuatorData.COMMAND_ON:
				if self.sh.screen:
					# create a message with the value and an 'ON' message, then scroll it across the LED display
					self.sh.screen.scroll_text(stateData);
				else:
					logging.warning("No SenseHAT LED screen instance to update.")
					return -1
			else:
				if self.sh.screen:
					# create a message with an 'OFF' message, then scroll it across the LED display
					self.sh.screen.clear();
				else:
					logging.warning("No SenseHAT LED screen instance to clear / close.")
					return -1
	