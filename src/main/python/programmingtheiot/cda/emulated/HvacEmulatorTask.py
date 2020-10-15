#####
# 
# This class is part of the Programming the Internet of Things project.
# 
# It is provided as a simple shell to guide the student and assist with
# implementation for the Programming the Internet of Things exercises,
# and designed to be modified by the student as needed.
#

import logging

from time import sleep

import programmingtheiot.common.ConfigConst as ConfigConst

from programmingtheiot.common.ConfigUtil import ConfigUtil
from programmingtheiot.data.ActuatorData import ActuatorData
from programmingtheiot.cda.sim.BaseActuatorSimTask import BaseActuatorSimTask

from pisense import SenseHAT

class HvacEmulatorTask(BaseActuatorSimTask):
	"""
	Shell representation of class for student implementation.
	
	"""

	def __init__(self):
		super(HvacEmulatorTask, self).__init__(actuatorType = ActuatorData.HVAC_ACTUATOR_TYPE, simpleName = "HVAC")
		senseHatKey = self.configUtil.getBoolean(ConfigConst.CONSTRAINED_DEVICE, ConfigConst.ENABLE_SENSE_HAT_KEY);
		if(senseHatKey):
			enableEmulation = False;
		else:
			enableEmulation = True;
		self.sh = SenseHAT(emulate = enableEmulation)

	def updateActuator(self, data: ActuatorData) -> bool:
		return super(HvacEmulatorTask, self).updateActuator(data);
	