# Constrained Device Application (Connected Devices)

## Lab Module 05
  - Install and configure Redis for your platform (optional, not used for this course work)
  - JSON encoder implementation in DataUtil
  - Add functionality to BaseSystemUtilTask implementation

### Description

What does your implementation do? 
In this lab module, the goal is to implement the data management utilities. First, the DataUtil module is updated to handle the received JSON payload and convert it to respective data type (Actuator Data, Sensor Data, SystemPerformance Data) and viceversa i.e. these data types back to JSON format for sending the messages out of CDA. In BaseSystemUtilTask, generateTelemetry() is updated to set the latest sensor data value from _getSystemUtil(). So, in the getTelemetryValue(), check if latest sensor data is available else call generateTelemetry()
 
 

How does your implementation work?
When the CDA app is run, DeviceDataManager is called to start and stop in the app's start / stop methods. 
 - The startManager method invokes SensorAdapterManager and ActuatorAdaptorManager.
 - SensorAdaptorManager uses Simulators/Emulators to form SensorData
 - Similarly, ActuatorAdaptorManager is used to generate ActuatorData
 - This sensorData and ActuatorData is now available at DeviceDataManager
 - Data communication between CDA and GDA happens with JSON format. So, functions such as actuatorDataToJson uses json.dumps command to convert data to json format. Similarly, json data is converted to restpective data types using dictionary in Python with keys to find the values and set attributes.



### Code Repository and Branch

URL: https://github.com/NU-CSYE6530-Fall2020/constrained-device-app-kiran-ramesh-s/tree/chapter05

### UML Design Diagram(s)
![CDA](https://github.com/NU-CSYE6530-Fall2020/constrained-device-app-kiran-ramesh-s/blob/chapter05/uml/lab5_CDA.png?raw=true)


### Unit Tests Executed

- DataUtilTest test under part02 unit tests 
- All unit tests under part01 (SystemCpuUtilTaskTest, MemUtilTaskTest, DiskUtilTaskTest)

### Integration Tests Executed
 - ./integration/DataIntegrationTest



EOF.
