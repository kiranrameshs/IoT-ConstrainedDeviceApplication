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

from programmingtheiot.cda.connection.IPubSubClient import IPubSubClient

from programmingtheiot.data.DataUtil import DataUtil

DEFAULT_QOS = 1

class MqttClientConnector(IPubSubClient):
	"""
	Shell representation of class for student implementation.
	
	"""
	mc = None
	clientID = None
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
		self.dataMsgListener = None
		self.clientID = clientID
		self.config = ConfigUtil.ConfigUtil()
		self.host = self.config.getProperty(ConfigConst.MQTT_GATEWAY_SERVICE, ConfigConst.HOST_KEY, ConfigConst.DEFAULT_HOST)
		self.port = self.config.getInteger(ConfigConst.MQTT_GATEWAY_SERVICE, ConfigConst.PORT_KEY, ConfigConst.DEFAULT_MQTT_PORT)
		self.keepAlive = self.config.getInteger(ConfigConst.MQTT_GATEWAY_SERVICE, ConfigConst.KEEP_ALIVE_KEY, ConfigConst.DEFAULT_KEEP_ALIVE)
		logging.info('\tMQTT Broker Host: ' + self.host)
		logging.info('\tMQTT Broker Port: ' + str(self.port))
		logging.info('\tMQTT Keep Alive:  ' + str(self.keepAlive))

	"""
	connects to client and returns true
	
	"""
	def connectClient(self) -> bool:
		if not self.mc:
			self.mc = mqttClient.Client(client_id = self.clientID, clean_session = True)
			self.mc.on_connect = self.onConnect
			self.mc.on_disconnect = self.onDisconnect
			self.mc.on_message = self.onMessage
			self.mc.on_publish = self.onPublish
			self.mc.on_subscribe = self.onSubscribe
		if not self.mc.is_connected():
			self.mc.connect(self.host, self.port, self.keepAlive)
			self.mc.loop_start()
			return True
		else:
			logging.warn('MQTT client is already connected. Ignoring connect request.')
			return False
	"""
	Disconnects from client 
	
	"""
	def disconnectClient(self) -> bool:
		if self.mc.is_connected():
			self.mc.disconnect()
			self.mc.loop_stop()
		return True
	
	"""
	call back methods to implement functionalities after connect disconnect, on message received etc
	
	"""
	def onConnect(self, client, userdata, flags, rc):
		logging.info('client has successfully connected')
		logging.info('[Callback] Connected to MQTT broker. Result code: ' + str(rc))
		self.mc.subscribe(topic = ResourceNameEnum.CDA_ACTUATOR_CMD_RESOURCE.value, qos = 1)
		self.mc.subscribe(topic = ResourceNameEnum.CDA_ACTUATOR_RESPONSE_RESOURCE.value, qos=1)
		self.mc.message_callback_add(sub = ResourceNameEnum.CDA_ACTUATOR_CMD_RESOURCE.value, callback = self.onActuatorCommandMessage)
		self.mc.message_callback_add(sub = ResourceNameEnum.CDA_ACTUATOR_RESPONSE_RESOURCE.value, callback = self.onActuatorCommandMessage)
		
	"""
	method called when mqtt is disconnected.
	
	"""
	def onDisconnect(self, client, userdata, rc):
		logging.info('client has successfully disconnected')
		
	def onMessage(self, client, userdata, msg):
		logging.info('onMessage has been called')
	
	"""
	method called when a message is published.
	
	"""		
	def onPublish(self, client, userdata, mid):
		logging.info('onPublish has been called with message id : ' + str(mid))
	
	"""
	method called when the client subscribes to a topic.
	
	"""
	def onSubscribe(self, client, userdata, mid, granted_qos):
		logging.info('onSubscribe has been called with message id : ' + str(mid))
	
	"""
	publishes message to client after validation and returns true
	
	"""
	def publishMessage(self, resource: ResourceNameEnum, msg, qos: int = IPubSubClient.DEFAULT_QOS):
		logging.info('publishMessage has been called')
		if not resource:
			return False
		if qos < 0 or qos > 2:
			qos = IPubSubClient.DEFAULT_QOS
		logging.info('Message received is : ' + msg)
		msgInfo  = self.mc.publish(resource.value, msg, qos)
		msgInfo.wait_for_publish()
		return True
	"""
	subscribes to topic and returns true
	
	"""
	def subscribeToTopic(self, resource: ResourceNameEnum, qos: int = IPubSubClient.DEFAULT_QOS):
		logging.info('subscribeToTopic has been called')
		if not resource:
			return False
		if qos < 0 or qos > 2:
			qos = IPubSubClient.DEFAULT_QOS
		self.mc.subscribe(resource.name, qos)
		return True
	
	"""
	Unsubscribes from topic
	
	"""
	def unsubscribeFromTopic(self, resource: ResourceNameEnum):
		self.mc.unsubscribe(resource.name, None)

	"""
	Setter for the data message listener
	
	"""
	def setDataMessageListener(self, listener: IDataMessageListener) -> bool:
		if listener:
			self.dataMsgListener = listener
			return True
		return False

	"""
	Callback method called for Actuator command
	
	"""
	def onActuatorCommandMessage(self, client, userdata, msg):
		logging.info('[Callback] Actuator command message received. Topic: %s.', msg.topic)
		logging.info('outside dataMsgListener')
		if self.dataMsgListener:
			logging.info('inside dataMsgListener')
			try:
				actuatorData = DataUtil().jsonToActuatorData(msg.payload.decode('utf-8'))
				
				self.dataMsgListener.handleActuatorCommandMessage(actuatorData)
			except:
				logging.exception("Failed to convert incoming actuation command payload to ActuatorData: ")