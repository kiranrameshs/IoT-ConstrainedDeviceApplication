import logging
import json

from programmingtheiot.cda.connection.CoapClientConnector import CoapClientConnector
from programmingtheiot.cda.connection.MqttClientConnector import MqttClientConnector

from programmingtheiot.cda.system.ActuatorAdapterManager import ActuatorAdapterManager
from programmingtheiot.cda.system.SensorAdapterManager import SensorAdapterManager
from programmingtheiot.cda.system.SystemPerformanceManager import SystemPerformanceManager

from programmingtheiot.common.IDataMessageListener import IDataMessageListener
from programmingtheiot.common.ResourceNameEnum import ResourceNameEnum
from programmingtheiot.common import ConfigConst
from programmingtheiot.common.ConfigUtil import ConfigUtil

from programmingtheiot.data.DataUtil import DataUtil
from programmingtheiot.data.ActuatorData import ActuatorData
from programmingtheiot.data.SensorData import SensorData
from programmingtheiot.data.SystemPerformanceData import SystemPerformanceData

class DeviceDataManager(IDataMessageListener):
	"""
	Shell representation of class for student implementation.
	
	"""
	enableEmulator = None
	systemPerformanceManager = None
	sensorAdapterManager = None
	actuatorAdapterManager = None
	enableMqtt = None
	enableCoap = None
	configUtil = None
	enableMqttClient = None
	mqttClient = None
	"""
	Initializes sensor,actuator, system performance managers
	
	"""
	def __init__(self, enableMqtt: bool = True, enableCoap: bool = False):
		self.enableMqtt = enableMqtt
		self.enableCoap = enableCoap
		self.configUtil = ConfigUtil()
		self.enableEmulator = self.configUtil.getProperty(ConfigConst.CONSTRAINED_DEVICE, ConfigConst.ENABLE_EMULATOR_KEY, False)
		self.systemPerformanceManager = SystemPerformanceManager()
		self.sensorAdapterManager = SensorAdapterManager()
		self.actuatorAdapterManager = ActuatorAdapterManager()
		self.systemPerformanceManager.setDataMessageListener(self)
		self.sensorAdapterManager.setDataMessageListener(self)
		self.actuatorAdapterManager.setDataMessageListener(self)
		self.enableHandleTempChangeOnDevice = self.configUtil.getBoolean(ConfigConst.CONSTRAINED_DEVICE, ConfigConst.ENABLE_HANDLE_TEMP_CHANGE_ON_DEVICE_KEY)
		self.triggerHvacTempFloor = self.configUtil.getFloat(ConfigConst.CONSTRAINED_DEVICE, ConfigConst.TRIGGER_HVAC_TEMP_FLOOR_KEY);
		self.triggerHvacTempCeiling = self.configUtil.getFloat(ConfigConst.CONSTRAINED_DEVICE, ConfigConst.TRIGGER_HVAC_TEMP_CEILING_KEY);
		if self.enableMqtt is True:
			self.mqttClient = MqttClientConnector()
			self.mqttClient.setDataMessageListener(self)
		if self.enableCoap is True:
			self.coapClient = CoapClientConnector()
	
	"""
	Implementing  IDataMessageListener interface methods
	
	"""		
	def handleActuatorCommandResponse(self, data: ActuatorData) -> bool:
		"""
		Handles Actuator response converts actuator data to json and returns if its successful
		"""
		logging.info("handleActuatorCommandResponse method has been called")
		jsonActuatorData = DataUtil.actuatorDataToJson(data)
		self._handleUpstreamTransmission(ResourceNameEnum.CDA_ACTUATOR_RESPONSE_RESOURCE, jsonActuatorData)
		return True
	
	def handleIncomingMessage(self, resourceEnum: ResourceNameEnum, msg: str) -> bool:
		"""
		Handles json response converts json data to Actuator object and returns if its successful
		"""
		logging.info("handleIncomingMessage method has been called")
		actuatorData = DataUtil.jsonToActuatorData(msg)
		self._handleIncomingDataAnalysis(msg)
		return True
	
	def handleActuatorCommandMessage(self, data: ActuatorData) -> bool:
		logging.info("Processing handleActuatorCommandMessage")
		if data:
			logging.info("Processing actuator command message.")
			
			# TODO: add further validation before sending the command
			self.actuatorAdapterManager.sendActuatorCommand(data)
			return True
		else:
			logging.warning("Received invalid ActuatorData command message. Ignoring.")
			return False
		
	def handleSensorMessage(self, data: SensorData) -> bool:
		"""
		Handles Sensor response converts sensor data to json and returns if its successful
		"""
		logging.info("handleSensorMessage method has been called")
		logging.info(data.name)
		jsonSensorData = DataUtil.sensorDataToJson(self, data)
		logging.info(jsonSensorData)
		self._handleUpstreamTransmission(ResourceNameEnum.CDA_SENSOR_MSG_RESOURCE, jsonSensorData)
		self._handleSensorDataAnalysis(data)
		return True
		
	def handleSystemPerformanceMessage(self, data: SystemPerformanceData) -> bool:
		"""
		Handles SystemPerformance response converts SystemPerformance data to json and returns if its successful
		"""
		logging.info("handleSystemPerformanceMessage method has been called")
		jsonSystemPerformanceData = DataUtil.systemPerformanceDataToJson(data)
		self._handleUpstreamTransmission(ResourceNameEnum.CDA_SYSTEM_PERF_MSG_RESOURCE, jsonSystemPerformanceData)
		return True
	
	
	def startManager(self):
		"""
		Starts Manager
		"""
		logging.info("DeviceDataManager has started!!")
		self.systemPerformanceManager.startManager()
		self.sensorAdapterManager.startManager()
		if self.enableMqtt is True:
			self.mqttClient.connectClient()
			self.mqttClient.subscribeToTopic(ResourceNameEnum.CDA_DISPLAY_CMD_MSG_RESOURCE, 1)
		
	def stopManager(self):
		"""
		Stops Manager
		"""
		self.mqttClient.disconnectClient()
		self.systemPerformanceManager.stopManager()
		self.sensorAdapterManager.stopManager()
		logging.info("DeviceDataManager has stopped!!")
	
	def _is_json(self, myjson):
		"""
		To check is data is valid json
		"""
		try:
			json_object = json.loads(myjson)
		except ValueError as e:
			return False
		return True
	
	def _handleIncomingDataAnalysis(self, msg: str):
		"""
		Call this from handleIncomeMessage() to determine if there's
		any action to take on the message. Steps to take:
		1) Validate msg: Most will be ActuatorData, but you may pass other info as well.
		2) Convert msg: Use DataUtil to convert if appropriate.
		3) Act on msg: Determine what - if any - action is required, and execute.
		"""
		logging.debug("_handleIncomingDataAnalysis method has been called")
		if self._is_json(msg):
			actuatorData = DataUtil.jsonToActuatorData(self, msg)
			self.actuatorAdapterManager.sendActuatorCommand(actuatorData)
			
		
	def _handleSensorDataAnalysis(self, data: SensorData):
		"""
		Call this from handleSensorMessage() to determine if there's
		any action to take on the message. Steps to take:
		1) Check config: Is there a rule or flag that requires immediate processing of data?
		2) Act on data: If # 1 is true, determine what - if any - action is required, and exe cute.
		"""
		logging.debug("_handleSensorDataAnalysis method has been called")
		if self.enableHandleTempChangeOnDevice is True:
			ad = ActuatorData(actuatorType = ActuatorData.HVAC_ACTUATOR_TYPE)
			if data.getSensorType()==3 and (data.getValue() > self.triggerHvacTempCeiling or data.getValue() < self.triggerHvacTempFloor):
				ad.setCommand(ActuatorData.COMMAND_ON)
				ad.setValue(data.getValue())
				self.actuatorAdapterManager.sendActuatorCommand(ad)
			
		
	def _handleUpstreamTransmission(self, resourceName: ResourceNameEnum, msg: str):
		"""
		Call this from handleActuatorCommandResponse(), handlesensorMessage(), and handleSystemPerformanceMessage()
		to determine if the message should be sent upstream. Steps to take:
		1) Check connection: Is there a client connection configured (and valid) to a remote MQTT or CoAP server?
		2) Act on msg: If # 1 is true, send message upstream using one (or both) client connections.
		"""
		logging.debug("_handleUpstreamTransmission method has been called")
		if self.enableMqtt is True:
			logging.debug("_handleUpstreamTransmission mqttClient  publishMessage has been called")
			logging.debug(resourceName.name)
# 			self.mqttClient.subscribeToTopic(resourceName, 1);
# 			logging.debug("subscribed to : "+ resourceName)
			self.mqttClient.publishMessage(resourceName, msg, 1)
		if self.enableCoap is True:
			logging.debug("_handleUpstreamTransmission coapClient  sendPostRequest has been called")
			self.coapClient.sendPostRequest(resourceName, msg, 5)
			
	def handleUpdateResponse(self, resourceEnum: ResourceNameEnum, msg: str) -> bool:
		pass