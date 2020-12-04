#####
# 
# This class is part of the Programming the Internet of Things project.
# 
# It is provided as a simple shell to guide the student and assist with
# implementation for the Programming the Internet of Things exercises,
# and designed to be modified by the student as needed.
#
import json
from json import JSONEncoder

from programmingtheiot.data.ActuatorData import ActuatorData
from programmingtheiot.data.SensorData import SensorData
from programmingtheiot.data.SystemPerformanceData import SystemPerformanceData

class DataUtil():
	"""
	Methods to convert Actuator, Sensor, SystemPerformance data to JSON and viceversa
	
	"""

	def __init__(self, encodeToUtf8 = False):
		pass
 
	def actuatorDataToJson(self, actuatorData):
		jsonData = json.dumps(actuatorData, indent = 4, cls = JsonDataEncoder, ensure_ascii = True)
		return jsonData
	
	def sensorDataToJson(self, data):
		jsonData = json.dumps(data, indent = 4, cls = JsonDataEncoder, ensure_ascii = True)
		return jsonData

	def systemPerformanceDataToJson(self, sysPerfData):
		jsonData = json.dumps(sysPerfData, indent = 4, cls = JsonDataEncoder, ensure_ascii = True)
		return jsonData
	
	def jsonToActuatorData(self, jsonData):
		print("Value is "+str(jsonData));
		jsonData = jsonData.replace("\'", "\"").replace('False','false').replace('True', 'true')
		adDict = json.loads(jsonData);
		ad = ActuatorData()
		mvDict = vars(ad)
		
		for key in adDict:
			if key in mvDict:
				setattr(ad, key, adDict[key])
		return ad;
	
	def jsonToSensorData(self, jsonData):
		print("Sensor Value is "+str(jsonData));
		jsonData = jsonData.replace("\'", "\"").replace('False','false').replace('True', 'true')
		sdDict = json.loads(jsonData);
		sd = SensorData()
		mvDict = vars(sd)
		
		for key in sdDict:
			if key in mvDict:
				setattr(sd, key, sdDict[key])
		return sd;
	
	def jsonToSystemPerformanceData(self, jsonData):
		jsonData = jsonData.replace("\'", "\"").replace('False','false').replace('True', 'true')
		spdDict = json.loads(jsonData);
		spd = SystemPerformanceData()
		mvDict = vars(spd)
		
		for key in spdDict:
			if key in mvDict:
				setattr(spd, key, spdDict[key])
		return spd;
	
class JsonDataEncoder(JSONEncoder):
	"""
	Convenience class to facilitate JSON encoding of an object that
	can be converted to a dict.
	
	"""
	def default(self, o):
		return o.__dict__
	