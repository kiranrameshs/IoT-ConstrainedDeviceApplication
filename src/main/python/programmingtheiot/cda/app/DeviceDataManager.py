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

from programmingtheiot.cda.connection.CoapClientConnector import CoapClientConnector
from programmingtheiot.cda.connection.MqttClientConnector import MqttClientConnector

from programmingtheiot.cda.system.ActuatorAdapterManager import ActuatorAdapterManager
from programmingtheiot.cda.system.SensorAdapterManager import SensorAdapterManager
from programmingtheiot.cda.system.SystemPerformanceManager import SystemPerformanceManager

from programmingtheiot.common.IDataMessageListener import IDataMessageListener
from programmingtheiot.common.ResourceNameEnum import ResourceNameEnum
from programmingtheiot.common import ConfigConst

from programmingtheiot.data.ActuatorData import ActuatorData
from programmingtheiot.data.SensorData import SensorData
from programmingtheiot.data.SystemPerformanceData import SystemPerformanceData
from programmingtheiot.common.ConfigUtil import ConfigUtil
from programmingtheiot.data.DataUtil import DataUtil

class DeviceDataManager(IDataMessageListener):
	"""
	Initialize the Actuator, Sensor, Comm Managers, Data Util
	
	"""
	
	def __init__(self, enableMqtt: bool = True, enableCoap: bool = False):
		self.systemPerformanceManager = SystemPerformanceManager();
		self.systemPerformanceManager.setDataMessageListener(self);
		self.configUtil = ConfigUtil()	
		self.mqttClient = MqttClientConnector();
		self.enableMqtt = enableMqtt;
		self.sensorAdapterManager = SensorAdapterManager();
		self.sensorAdapterManager.setDataMessageListener(self);
		self.actuatorAdapterManager = ActuatorAdapterManager();
		self.actuatorAdapterManager.setDataMessageListener(self);
		self.enableHandleTempChangeOnDevice = self.configUtil.getBoolean(ConfigConst.CONSTRAINED_DEVICE, ConfigConst.ENABLE_HANDLE_TEMP_CHANGE_ON_DEVICE_KEY)
		self.triggerHvacTempFloor = self.configUtil.getFloat(ConfigConst.CONSTRAINED_DEVICE, ConfigConst.TRIGGER_HVAC_TEMP_FLOOR_KEY);
		self.triggerHvacTempCeiling = self.configUtil.getFloat(ConfigConst.CONSTRAINED_DEVICE, ConfigConst.TRIGGER_HVAC_TEMP_CEILING_KEY);
			
	def handleActuatorCommandResponse(self, data: ActuatorData) -> bool:
		logging.info("Handle Actuator Command Response");
		return True;
	
	def handleIncomingMessage(self, resourceEnum: ResourceNameEnum, msg: str) -> bool:
		logging.info("Handle Incoming Message");
		actuatorDataInstance = DataUtil.jsonToActuatorData(msg);
		self._handleIncomingDataAnalysis(msg);
		return True;

	def handleSensorMessage(self, data: SensorData) -> bool:
		logging.info("Handle Sensor Message");
		self.toJSON = DataUtil.sensorDataToJson(data);
		self._handleUpstreamTransmission(ResourceNameEnum.CDA_SENSOR_MSG_RESOURCE,self.toJSON)
		self._handleSensorDataAnalysis(data);
		
		self.mqttClient.connect()
		self.mqttClient.subscribeToTopic(ResourceNameEnum.CDA_SENSOR_MSG_RESOURCE)
		sleep(5)
		
		self.mqttClient.publishMessage(ResourceNameEnum.CDA_SENSOR_MSG_RESOURCE, str(data))
		sleep(5)
		
		self.mqttClient.unsubscribeFromTopic(ResourceNameEnum.CDA_SENSOR_MSG_RESOURCE)
		sleep(5)
		
		
		self.mqttClient.disconnect()
		sleep(5)
		return True;
		
	def handleSystemPerformanceMessage(self, data: SystemPerformanceData) -> bool:
		logging.info("Handle System Performance Message");
		self.toJSON = DataUtil.sensorDataToJson(data);
		self._handleUpstreamTransmission(ResourceNameEnum.CDA_SYSTEM_PERF_MSG_RESOURCE,self.toJSON)
		self._handleSensorDataAnalysis(data);
		self.mqttClient.connect()
		self.mqttClient.subscribeToTopic(ResourceNameEnum.CDA_SYSTEM_PERF_MSG_RESOURCE)
		sleep(5)
		
		self.mqttClient.publishMessage(ResourceNameEnum.CDA_SYSTEM_PERF_MSG_RESOURCE, str(data))
		sleep(5)
		
		self.mqttClient.unsubscribeFromTopic(ResourceNameEnum.CDA_SYSTEM_PERF_MSG_RESOURCE)
		sleep(5)
		
		
		self.mqttClient.disconnect()
		sleep(5)
		return True;
	
	def startManager(self):
		logging.info("Start Manager "+str(self.startManager.__name__))
		self.systemPerformanceManager.startManager();
		self.sensorAdapterManager.startManager();
		if(self.enableMqtt):
			self.mqttClient.connectClient()
		
	def stopManager(self):
		logging.info("Stop Manager "+str(self.stopManager.__name__))
		self.systemPerformanceManager.stopManager();
		self.sensorAdapterManager.stopManager();
		if(self.enableMqtt):
			self.mqttClient.disconnectClient()
		

	def _handleIncomingDataAnalysis(self, msg: str):
		"""
		Call this from handleIncomeMessage() to determine if there's
		any action to take on the message. Steps to take:
		1) Validate msg: Most will be ActuatorData, but you may pass other info as well.
		2) Convert msg: Use DataUtil to convert if appropriate.
		3) Act on msg: Determine what - if any - action is required, and execute.
		"""
		logging.info("Handle Incoming DataAnalysis "+str(msg))
		actuatorData = DataUtil.jsonToActuatorData(msg)
		self.actuatorAdapterManager.sendActuatorCommand(actuatorData)
		
	def _handleSensorDataAnalysis(self, data: SensorData):
		"""
		Call this from handleSensorMessage() to determine if there's
		any action to take on the message. Steps to take:
		1) Check config: Is there a rule or flag that requires immediate processing of data?
		2) Act on data: If # 1 is true, determine what - if any - action is required, and execute.
		"""
		logging.info("Handle Sensor Data Analysis "+str(data));
		if(self.enableHandleTempChangeOnDevice == True):
			actuatorData = ActuatorData(ActuatorData.HVAC_ACTUATOR_TYPE);
			actuatorData.getValue();
			actuatorData.setCommand(ActuatorData.COMMAND_ON);
			self.actuatorAdapterManager.sendActuatorCommand(actuatorData);
		
	def _handleUpstreamTransmission(self, resourceName: ResourceNameEnum, msg: str):
		"""
		Call this from handleActuatorCommandResponse(), handlesensorMessage(), and handleSystemPerformanceMessage()
		to determine if the message should be sent upstream. Steps to take:
		1) Check connection: Is there a client connection configured (and valid) to a remote MQTT or CoAP server?
		2) Act on msg: If # 1 is true, send message upstream using one (or both) client connections.
		"""
		logging.info("Handle Upstream Transmission "+str(msg));
