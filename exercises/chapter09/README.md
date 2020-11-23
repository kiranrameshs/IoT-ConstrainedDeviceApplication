# Constrained Device Application (Connected Devices)

## Lab Module 09
  - Create coAP client
  - Implement GET, PUT, POST, DELETE functionalities on CoapClientConnector

### Description

What does your implementation do? 
This implementation is for creating a coApClient on the CDA. The connector creates the url to the coAp server and has methods to generate get,put,post and delete methods.
 

How does your implementation work?
The client connector, when initialized creates the coAP server address and calls the initClient method which will create the coApClient object using the HelperClient class of coApPython3. Then methods are provided to generate get,put,post and delete methods. in these methods, we set the URI, call the methods and wait for the response and these responses are handed by the callback methods. To run the connector, we must first run the coApServer on the GDA and then run the client connector.



### Code Repository and Branch

URL: https://github.com/NU-CSYE6530-Fall2020/constrained-device-app-kiran-ramesh-s/tree/chapter09

### UML Design Diagram(s)
![CDA](https://github.com/NU-CSYE6530-Fall2020/constrained-device-app-kiran-ramesh-s/blob/chapter09/uml/lab9_CDA.png?raw=true)

 
 ### Wireshark PCAP capture Snap(s)

 #### - GET
 ![GET](https://github.com/NU-CSYE6530-Fall2020/constrained-device-app-kiran-ramesh-s/blob/chapter09/pcap/coAP/CDA_Get.PNG?raw=true) 
 #### - GETRESPONSE
 ![GETRESPONSE](https://github.com/NU-CSYE6530-Fall2020/constrained-device-app-kiran-ramesh-s/blob/chapter09/pcap/coAP/CDA_Get_Response.PNG?raw=true) 
 #### - POST
 ![POST](https://github.com/NU-CSYE6530-Fall2020/constrained-device-app-kiran-ramesh-s/blob/chapter09/pcap/coAP/CDA_Post.PNG?raw=true) 
 #### - POSTRESPONSE
 ![POSTRESPONSE](https://github.com/NU-CSYE6530-Fall2020/constrained-device-app-kiran-ramesh-s/blob/chapter09/pcap/coAP/CDA_Post_Response.PNG?raw=true)  
 #### - PUT
 ![PUT](https://github.com/NU-CSYE6530-Fall2020/constrained-device-app-kiran-ramesh-s/blob/chapter09/pcap/coAP/CDA_Put.PNG?raw=true)  
 #### - DELETE
 ![DELETE](https://github.com/NU-CSYE6530-Fall2020/constrained-device-app-kiran-ramesh-s/blob/chapter09/pcap/coAP/CDA_Delete.PNG?raw=true)  
 #### - FULLCAPTURE
 ![FULLCAPTURE](https://github.com/NU-CSYE6530-Fall2020/constrained-device-app-kiran-ramesh-s/blob/chapter09/pcap/coAP/FullCaptureCDA.PNG?raw=true) 
 
 
### Unit Tests Executed

 - NA

### Integration Tests Executed

 -  ./src/test/python/programmingtheiot/part03/integration/connection/coAPClientConnectorTest



EOF.
