# Constrained Device Application (Connected Devices)

## Lab Module 10
  - Test the performance of MQTT using all three QoS levels
  - Test the performance of CoAP using both CON and NON messages
  - Update IDataMessageListener and DeviceDataManager to handle incoming ActuatorData commands
  - Update MqttClientConnector to subscribe to ActuatorData command messages from the GDA
  - Update DeviceDataManager to send sensor and system performance messages to the GDA
  - Update sensor and actuator data containers to set the appropriate device name
  - Update simulator and emulator tasks to set the appropriate SensorData and ActuatorData name

### Description

What does your implementation do? 
First, we test the performance for each of the QoS levels: QoS 0, QoS 1, and QoS 2 with MAX_TEST_RUNS = 10000 by disabling unnecessary logging
 - How long was the connect / disconnect?
 - For the QoS tests, include the percentage difference between each QoS level, with QoS 0 tests as the baseline. QOS1 -22& and QOS2 +50% 
 - Which ran fastest? QOS0
 - Which ran slowest? QOS2
 
 This implementation is mainly abuot handling both upstream and downstream messages of CDA such as sensor, sysperf for upstream and actuatorData to actuatorcommand as downstream. Supports sending Actuator Data to GDA and subscribe to actuator data topics to receive and handle incoming subscription messages for actuator command messages from GDA. 
 Similarly, handle sensor data and system performance data and send it to GDA using MQTT/CoAP. Update configConst such that each actuator and sensor message will have appropriate device names.
 


How does your implementation work?
DeviceDataManager handles the ActuatorData received from GDA and sends it as an ActuatorCommand from the ActuatorAdapterManager. 
MQTT Client Connector handles incoming subscribed messages by converting it to actuatorData from JSON. Similarly, sensor values are compared to  floor and ceiling values configured in PiotConfig.props and are converted to JSON and sent to GDA using _handleUpstreamTransmission
For sensor and actuator data containers to get appropriate device names, they are added as configuration in ConfigConst and data classes, emulated and simulated classes all recieve this as an argument in the constructor of their respective classes and is used in generateTelemetry()




### Code Repository and Branch

URL: https://github.com/NU-CSYE6530-Fall2020/constrained-device-app-kiran-ramesh-s/tree/chapter10

### UML Design Diagram(s)
![CDA](https://github.com/NU-CSYE6530-Fall2020/constrained-device-app-kiran-ramesh-s/blob/chapter10/uml/lab10_CDA.png?raw=true)

 
 ### Performance test Snap(s)

 #### - CoAP
 ![CoAP](https://github.com/NU-CSYE6530-Fall2020/constrained-device-app-kiran-ramesh-s/blob/chapter10/pcap/CoAPTest.PNG?raw=true) 
 #### - MQTT
 ![MQTT](https://github.com/NU-CSYE6530-Fall2020/constrained-device-app-kiran-ramesh-s/blob/chapter10/pcap/MQTTTest.PNG?raw=true) 
 
 
### Unit Tests Executed

 - NA

### Integration Tests Executed

 -  ./src/test/python/programmingtheiot/part03/integration/connection/coAPClientConnectorTest
 - DeviceDataManagerCallbackTest
 - DeviceDataManagerWithCommsTest 
 - HVAC, Humidifier, LED Emulator task tests
 - Humidity, Temp, Pressure Sim task tests

### Performance test
 - ./src/test/python/programmingtheiot/part03/integration/connection

EOF.
