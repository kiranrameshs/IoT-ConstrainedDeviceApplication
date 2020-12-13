#####
# 
# This class is part of the Programming the Internet of Things project.
# 
# It is provided as a simple shell to guide the student and assist with
# implementation for the Programming the Internet of Things exercises,
# and designed to be modified by the student as needed.
#

import logging
import socket

from coapthon import defines
from coapthon.client.coap import CoAP
from coapthon.client.helperclient import HelperClient
from coapthon.messages.message import Message
from coapthon.messages.request import Request
from coapthon.utils import parse_uri
from coapthon.utils import generate_random_token


from programmingtheiot.common import ConfigUtil
from programmingtheiot.common import ConfigConst

from programmingtheiot.common.IDataMessageListener import IDataMessageListener
from programmingtheiot.common.ResourceNameEnum import ResourceNameEnum

from programmingtheiot.cda.connection.IRequestResponseClient import IRequestResponseClient

class CoapClientConnector(IRequestResponseClient):
	"""
	Shell representation of class for student implementation.
	
	"""
	
	def __init__(self):
		self.config = ConfigUtil.ConfigUtil()
		self.dataMsgListener = None
		self.coapClient = None
		self.host = self.config.getProperty(ConfigConst.COAP_GATEWAY_SERVICE, ConfigConst.HOST_KEY, ConfigConst.DEFAULT_HOST)
		self.port = self.config.getInteger(ConfigConst.COAP_GATEWAY_SERVICE, ConfigConst.PORT_KEY, ConfigConst.DEFAULT_COAP_PORT)
		logging.info('\tCoAP Server Host: ' + self.host)
		logging.info('\tCoAP Server Port: ' + str(self.port))
		self.url = "coap://" + self.host + ":" + str(self.port) + "/"
		try:
			logging.info("Parsing URL: " + self.url)
			self.host, self.port, self.path = parse_uri(self.url)	
			tmpHost = socket.gethostbyname(self.host)
			if tmpHost:
				self.host = tmpHost
				self._initClient()
			else:
				logging.error("Can't resolve host: " + self.host)
		except socket.gaierror:
			logging.info("Failed to resolve host: " + self.host)
	
	'''
	@param : timeout
	output : boolean
	description : Check if the discovery request is successful 
	'''			
	def sendDiscoveryRequest(self, timeout: int = IRequestResponseClient.DEFAULT_TIMEOUT) -> bool:
		logging.info('Discovering remote resources...')
		self.coapClient.get(path = '/.well-known/core', callback = self._onDiscoveryResponse, timeout = timeout)

	'''
	@param : timeout
	output : boolean
	description : Delete the requested source and Check if the delete request is successful 
	'''	
	def sendDeleteRequest(self, resource: ResourceNameEnum, enableCON=False, timeout: int = IRequestResponseClient.DEFAULT_TIMEOUT) -> bool:
		logging.info("DeleteRequest")
		if resource:
			logging.debug("Issuing DELETE with path: " + resource.value)
			request = self.coapClient.mk_request(defines.Codes.DELETE, path = resource.value)
			request.token = generate_random_token(2)
			if not enableCON:
				request.type = defines.Types["NON"]
			self.coapClient.send_request(request = request, callback = self._onDeleteResponse, timeout = timeout)
		else:
			logging.warning("Can't test DELETE - no path or path list provided.")
	'''
	@param : timeout
	output : boolean
	description : Get the requested source and Check if the get request is successful 
	'''	
	def sendGetRequest(self, resource: ResourceNameEnum, enableCON = False, timeout: int = IRequestResponseClient.DEFAULT_TIMEOUT ) -> bool:
		logging.info("Get Request")
		if resource:
			logging.debug("Issuing GET with path: " + resource.value)
			request = self.coapClient.mk_request(defines.Codes.GET, path = resource.value)
			request.token = generate_random_token(2)
	
			if not enableCON:
				request.type = defines.Types["NON"]
		
			self.coapClient.send_request(request = request, callback = self._onGetResponse, timeout = timeout)
		else:
			logging.warning("Can't test GET - no path or path list provided.")

		'''
	@param : timeout
	output : boolean
	description : Post the requested source and Check if the Post request is successful 
	'''	
	def sendPostRequest(self, resource: ResourceNameEnum, payload: str, enableCON=False, timeout: int = IRequestResponseClient.DEFAULT_TIMEOUT) -> bool:
		if resource:
			request = self.coapClient.mk_request(defines.Codes.POST, path = resource.value)
			request.token = generate_random_token(2)
			request.payload = payload
			if not enableCON:
				request.type = defines.Types["NON"]
			self.coapClient.send_request(request = request, callback = self._onPostResponse, timeout = timeout)
		else:
			pass

		'''
	@param : timeout
	output : boolean
	description : Put the requested source and Check if the Put request is successful 
	'''	
	def sendPutRequest(self, resource: ResourceNameEnum, payload: str, enableCON = False, timeout: int = IRequestResponseClient.DEFAULT_TIMEOUT) -> bool:
		if resource:
			request = self.coapClient.mk_request(defines.Codes.PUT, path = resource.value)
			request.token = generate_random_token(2)
			request.payload = payload
			if not enableCON:
				request.type = defines.Types["NON"]
			self.coapClient.send_request(request = request, callback = self._onPutResponse, timeout = timeout)
		else:
			pass

	def setDataMessageListener(self, listener: IDataMessageListener) -> bool:
		self.dataMsgListener = listener
		return True

	'''
	@param : timeout
	output : boolean
	description : Start the observer
	'''	
	def startObserver(self, resource: ResourceNameEnum, ttl: int = IRequestResponseClient.DEFAULT_TTL) -> bool:
		pass

	def stopObserver(self, timeout: int = IRequestResponseClient.DEFAULT_TIMEOUT) -> bool:
		pass
	
	"""
	get the payload and convert to a list of paths
	the following is optional, but provides an easy way to track all the returned resource names
	"""
	def _onDiscoveryResponse(self, response):
		if response:
			logging.info(response.pretty_print())
			self.pathList = response.payload.split(',')
			index = 0
			for path in self.pathList:
				for char in '<\>':
					path = path.replace(char, '')
				self.pathList[index] = path
				logging.info('  Path entry [' + str(index) + ']:' + self.pathList[index])
				index += 1
		else:
			logging.info("No response received.")
	
	'''
	@param : response
	output : N/A
	description : Get Response
	'''	
	def _onGetResponse(self, response):
		logging.info('GET response received.')
		if response:
			logging.info('Token: ' + str(response.token))
			logging.info(str(response.location_path))
			logging.info(str(response.payload))
			resource = None
			if self.dataMsgListener:
				self.dataMsgListener.handleIncomingMessage(resource, str(response.payload))
	'''
	@param : response
	output : N/A
	description : Call back
	'''				
	def _onPutResponse(self,response):
		if response:
			pass

	'''
	@param : response
	output : N/A
	description : Call back
	'''		
	def _onPostResponse(self,response):
		if response:
			pass
	
	'''
	@param : response
	output : N/A
	description : Call back
	'''			
	def _onDeleteResponse(self,response):
		logging.info('DELETE response received.')
		if response:
			logging.info('Token: ' + str(response.token))
			logging.info(str(response.location_path))
			logging.info(str(response.payload))
	
	'''
	@param : response
	output : N/A
	description : Init the co-ap client
	'''	
	def _initClient(self):
		if not self.coapClient:
			self.coapClient = HelperClient(server = (self.host, self.port))
		
	'''
	@param : response
	output : N/A
	description : disconnect the Client 
	'''		
	def disconnectClient(self):
		if(self.coapClient):
			self.coapClient = None
			