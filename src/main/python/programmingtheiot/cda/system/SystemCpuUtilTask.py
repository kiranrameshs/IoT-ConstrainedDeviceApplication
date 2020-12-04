#####
# 
# This class is part of the Programming the Internet of Things project.
# 
# It is provided as a simple shell to guide the student and assist with
# implementation for the Programming the Internet of Things exercises,
# and designed to be modified by the student as needed.
#

import logging
import psutil
import programmingtheiot.common.ConfigConst as ConfigConst
from programmingtheiot.cda.system.BaseSystemUtilTask import BaseSystemUtilTask

class SystemCpuUtilTask(BaseSystemUtilTask):
	"""
	Shell representation of class for student implementation.
	
	"""

	def __init__(self):
		super(SystemCpuUtilTask, self).__init__(sensorName = ConfigConst.CPU_UTIL_NAME)
		#Assign the imported psutil library
		self.perfMgr = psutil
		pass
	
	def _getSystemUtil(self) -> float:
		return psutil.cpu_percent()
	
	def _getTelemetry(self) -> float:
		#Call CPU Util Percent from Perf Manager
		cpuUtilPct = self.perfMgr.cpu_percent()
		logging.info("CPU Utilization Data collected, CPU Utilization is "+str(cpuUtilPct))
		#pass
		