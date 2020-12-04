#####
# 
# This class is part of the Programming the Internet of Things project.
# 
# It is provided as a simple shell to guide the student and assist with
# implementation for the Programming the Internet of Things exercises,
# and designed to be modified by the student as needed.
#

import logging
import paho.mqtt.client as mqttClient

from programmingtheiot.common import ConfigUtil
from programmingtheiot.common import ConfigConst

from programmingtheiot.common.IDataMessageListener import IDataMessageListener
from programmingtheiot.common.ResourceNameEnum import ResourceNameEnum
from programmingtheiot.data.DataUtil import DataUtil

from programmingtheiot.cda.connection.IPubSubClient import IPubSubClient


DEFAULT_QOS = 1

class MqttClientConnector(IPubSubClient):
	"""
	Shell representation of class for student implementation.
	
	"""

	def __init__(self, clientID: str = None):
		"""
		Default constructor. This will set remote broker information and client connection
		information based on the default configuration file contents.
		
		@param clientID Defaults to None. Can be set by caller. If this is used, it's
		critically important that a unique, non-conflicting name be used so to avoid
		causing the MQTT broker to disconnect any client using the same name. With
		auto-reconnect enabled, this can cause a race condition where each client with
		the same clientID continuously attempts to re-connect, causing the broker to
		disconnect the previous instance.
		"""
		self.config = ConfigUtil.ConfigUtil()
		self.host = self.config.getProperty(ConfigConst.MQTT_GATEWAY_SERVICE, ConfigConst.HOST_KEY, ConfigConst.DEFAULT_HOST)
		self.port = self.config.getInteger(ConfigConst.MQTT_GATEWAY_SERVICE, ConfigConst.PORT_KEY, ConfigConst.DEFAULT_MQTT_PORT)
		self.keepAlive = self.config.getInteger(ConfigConst.MQTT_GATEWAY_SERVICE, ConfigConst.KEEP_ALIVE_KEY, ConfigConst.DEFAULT_KEEP_ALIVE)
		logging.info('\tMQTT Broker Host: ' + self.host)
		logging.info('\tMQTT Broker Port: ' + str(self.port))
		logging.info('\tMQTT Keep Alive:  ' + str(self.keepAlive))
		self.mc = mqttClient.Client(client_id = clientID, clean_session = True)
		self.clientID = clientID;
		self.dataMsgListener = None
		
	def connect(self) -> bool:
		if not self.mc:
			self.mc = mqttClient.Client(client_id = self.clientID, clean_session = True)
			self.mc.on_connect = self.onConnect
			self.mc.on_disconnect = self.onDisconnect
			self.mc.on_message = self.onMessage
			self.mc.on_publish = self.onPublish
			self.mc.on_subscribe = self.onSubscribe
		if not self.mc.is_connected():
# 			logging.info('Not connected to Broker, connecting now ')
			self.mc.connect(self.host, self.port, self.keepAlive)
# 			logging.info(str(self.mcc));
			self.mc.loop_start()
# 			logging.info('Connected to Broker  successfully ')
			return True
		else:
# 			logging.warn('MQTT client is already connected. Ignoring connect request.')
			return False
		
	def disconnect(self) -> bool:
		if self.mc.is_connected():
			self.mc.disconnect()
			self.mc.loop_stop()
			return True
		return True
		
	def onConnect(self, client, userdata, flags, rc):
# 		logging.info("On Connect")
		logging.info('[Callback] Connected to MQTT broker. Result code: ' + str(rc))

		# NOTE: Use the QoS of your choice - '1' is only an example
		self.mqttClient.subscribe(topic = ResourceNameEnum.CDA_ACTUATOR_CMD_RESOURCE.value, qos = 1)
		self.mqttClient.message_callback_add(sub = ResourceNameEnum.CDA_ACTUATOR_CMD_RESOURCE.value, callback = self.onActuatorCommandMessage)
# 		pass
				
	def onDisconnect(self, client, userdata, rc):
# 		logging.info("On Disconnect")
		pass
				
	def onMessage(self, client, userdata, msg):
		logging.info("On Message")
					
	def onPublish(self, client, userdata, mid):
# 		logging.info("Publish "+str(mid));
		pass
			
	def onSubscribe(self, client, userdata, mid, granted_qos):
		logging.info("Subscribe "+str(mid));
			
	def publishMessage(self, resource: ResourceNameEnum, msg, qos: int = IPubSubClient.DEFAULT_QOS):
# 		logging.info("Publish Message")
		if(not ResourceNameEnum):
			return False
		if(qos<0 or qos>2):
			qos = self.DEFAULT_QOS
		if self.mc.is_connected():
			self.mc.publish(str(resource),msg,qos);
# 			logging.info("Publish message successful");
			msgInfo = self.mc.publish(topic = resource.value, payload = msg, qos = qos)
			msgInfo.wait_for_publish()
			return True
		else:
			return False
		
	def subscribeToTopic(self, resource: ResourceNameEnum, qos: int = IPubSubClient.DEFAULT_QOS):
		logging.info("Subscribe Topic")
		if(not ResourceNameEnum):
			return False
		if(qos<0 or qos>2):
			qos = self.DEFAULT_QOS
		if self.mc.is_connected():
			self.mc.subscribe(str(resource),qos);
			logging.info("Subscribe Topic successful");
			return True
		else:
			return False
	
	def unsubscribeFromTopic(self, resource: ResourceNameEnum):
		self.mc.unsubscribe(str(resource));
		logging.info("Unsubscribe succesful");
		return False

	
	def setDataMessageListener(self, listener: IDataMessageListener) -> bool:
		if listener:
			self.dataMsgListener = listener
			return True
		return False
	
	def onActuatorCommandMessage(self, client, userdata, msg):
		logging.info('[Callback] Actuator command message received. Topic: %s.', msg.topic)
		
		if self.dataMsgListener:
			try:
				actuatorData = DataUtil().jsonToActuatorData(msg.payload)
				
				self.dataMsgListener.handleActuatorCommandMessage(actuatorData)
			except:
				logging.exception("Failed to convert incoming actuation command payload to ActuatorData: ")
