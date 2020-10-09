# Constrained Device Application (Connected Devices)

## Lab Module 03
  - Add functionality to shell implementation of BaseSensorSimTask
  - Create all sensor simulator modules (HumiditySensorSimTask, PressureSensorSimTask, TemperatureSensorSimTask)
  - Add functionality to shell implementation of BaseActuatorSimTask
  - Create all actuator simulator modules (HumidifierActuatorSimTask, HvacActuatorSimTask)
  - Create / edit module - SensorAdapterManager
  - Create / edit module - ActuatorAdapterManager
  - Create / edit module - DeviceDataManage
  - Verify and merge Chapter 03 branch into the primary branch

### Description

What does your implementation do? 
In this lab module, Device Data Manager was made the controller of Sensor, Actuator and System Performance Managers. The main purpose of the implementation is to simulate the actuators and sensors. For this, we introduce few sensors such as Humidity, Pressure and Temperature sensors. Similarly, Humidifier and HVAC actuators. These are derived classed of BaseSensorSimTask and BaseActuatorSimTask where most of the implementation still resides in the parent class. As we need data for simulation, we implement Actuator and Sensor Data modules which are derived classes of BaseIoTData. With this implementation we have Sensors and Actuators simulation with respective data


How does your implementation work?
When the CDA app is run, DeviceDataManager is called to start and stop in the app's start / stop methods. 
 - The startManager method invokes SensorAdapterManager and ActuatorAdaptorManager.
 - Managers have schedulers that runs the jobs. 
 - A SensorAdaptorManager gets minValue and maxValue of humidity, pressure and temperature from SensorDataGenerator. Ex: humidityFloor and humidityCeiling
 - SensorData is formed callig dataGenerator. Ex: humidityData
 - SensorSimTask sets a random value for the SensorData
 - This sensorData is now available at DeviceDataManager for data analysis
 Similarly, ActuatorAdaptorManager is used to generate the data required to simlaute the actuators and the ActuatorSimTask will send the commands to the Actuators



### Code Repository and Branch

URL: https://github.com/NU-CSYE6530-Fall2020/constrained-device-app-kiran-ramesh-s/tree/chapter03

### UML Design Diagram(s)
![CDA](https://github.com/NU-CSYE6530-Fall2020/constrained-device-app-kiran-ramesh-s/blob/chapter03/uml/lab3_CDA.png?raw=true)


### Unit Tests Executed

- All unit tests under part02 except DataUtilTest

### Integration Tests Executed

- SensorAdapterManagerTest
 - ActuatorAdapterManagerTest



EOF.
