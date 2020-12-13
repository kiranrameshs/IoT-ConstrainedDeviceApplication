#####
# 
# This class is part of the Programming the Internet of Things
# project, and is available via the MIT License, which can be
# found in the LICENSE file at the top level of this repository.
# 
# Copyright (c) 2020 by Andrew D. King
# 

from programmingtheiot.data.ActuatorData import ActuatorData
from programmingtheiot.cda.sim.BaseActuatorSimTask import BaseActuatorSimTask
import programmingtheiot.common.ConfigConst as ConfigConst

class HumidifierActuatorSimTask(BaseActuatorSimTask):
	"""
	This is a simple wrapper for an Actuator abstraction - it provides
	a container for the actuator's state, value, name, and status. A
	command variable is also provided to instruct the actuator to
	perform a specific function (in addition to setting a new value
	via the 'val' parameter.
	
	"""

	def __init__(self):
		super(HumidifierActuatorSimTask, self).__init__(actuatorType = ActuatorData.HUMIDIFIER_ACTUATOR_TYPE, simpleName = "HUMIDIFIER", actuatorName = ConfigConst.HUMIDIFIER_ACTUATOR_NAME)
	

	'''
	@param : none
	output : SensorData
	description : activates the actuator
	'''	
	def activateActuator(self, val: float) -> bool:
		super(HumidifierActuatorSimTask, self).activateActuator(val)
		return True
 	
	'''
	@param : none
	output : SensorData
	description : deactivates the actuator
	'''		
	def deactivateActuator(self) -> bool:
		super(HumidifierActuatorSimTask, self).deactivateActuator()
		return True
 		
	'''
	@param : none
	output : SensorData
	description : Update the actuator
	'''	
	def updateActuator(self, data: ActuatorData) -> ActuatorData:
		return super(HumidifierActuatorSimTask, self).updateActuator(data)
