# Constrained Device Application (Connected Devices)

## Lab Module 06
  - Install and configure Mosquitto MQTT Broker for your platform
  - Create module MqttClientConnector
  - Create the callback infrastructure for the MqttClientConnector
  - Create the publish and subscribe methods for MqttClientConnector
  - Connect MqttClientConnector to DeviceDataManager

### Description

What does your implementation do? 
In this lab module, the goal is to implement the MqttClientConnector module and initialize it from the Device Data Manager module. Once the MQTT client integration is complete, the messages are communicated between the CDA and GDA using MQTT broker. The module MqttClientConnector uses the APIs connect, subscribe, publish, unsubscribe, disconnect from the message broker. For CDA, the incoming messages are Actuator data Commands from the GDA and the outgoing messages are sensor Data messages. Once the Actuator command message  is received, it is passed to the Actuator Emulator to be used. When the sensor data is available, the CDA subscribes to the MQTT broker topic, publishes the sensor data.
 
 

How does your implementation work?
When the CDA app is run, DeviceDataManager is called to start and stop in the app's start / stop methods. 
 - The startManager method creates the MQTT client connection and connects to the MQTT broker depending on the configurations 
 -  Once the message is received by the Device Data manager from the broker to the subscribed topic, the actuator command passed to the respective data class to be utilized
 - If the sensor data is available, then the data is published to the subcribed topic
 - Once the StopManager() is triggered, then the client connection to the MQTT broker is disconnected and closed



### Code Repository and Branch

URL: https://github.com/NU-CSYE6530-Fall2020/constrained-device-app-kiran-ramesh-s/tree/chapter06

### UML Design Diagram(s)
![CDA](https://github.com/NU-CSYE6530-Fall2020/constrained-device-app-kiran-ramesh-s/blob/chapter06/uml/lab6_CDA.png?raw=true)

### Wireshark PCAP capture Snap(s)
 #### - CONNECT
 
 #### - CONNACK
 
 #### - PUBLISH
 
 #### - PUBACK
 
 #### - PUBREC
 
 #### - PUBREL
 
 #### - PUBCOMP
 
 #### - SUBSCRIBE
 
 #### - SUBACK
 
 #### - UNSUBSCRIBE
 
 #### - UNSUBACK
 
 #### - PINGREQ
 
 #### - PINGRESP
 
 #### - DISCONNECT
 
### Unit Tests Executed

 - All Unit tests under part01
 - All Unit tests under part02

### Integration Tests Executed

 -  ./src/test/java/programmingtheiot/part03/integration/MqttClientConnectorTest



EOF.
