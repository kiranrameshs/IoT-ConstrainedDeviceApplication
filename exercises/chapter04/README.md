# Constrained Device Application (Connected Devices)

## Lab Module 04
  - Install and configure the SenseHAT emulator and supporting libraries for your platform
  - Create all actuator emulator modules (HumidityEmulatorTask, PressureEmulatorTask, TemperatureEmulatorTask)
  - Add emulator functionality to SensorAdapterManager
  - Add emulator functionality to ActuatorAdapterManager

### Description

What does your implementation do? 
In this lab module, the main agenda is to add the emulator to the CDA app just like the simulator implementation module. The approach of using the emulator is to use it on the bash of Ubuntu on Windows. Now the data of the sensor and the actuator is by using the emulator
System Info:
 - Windows 10
 - Ubuntu 18.04 used on WSL2
 - Xming as server for diplay (emulator GUI)
 - Xlaunch for configuring the display server
 - PyGObject for GTK based GUI
 - Sense HAT emulator
 - PiSense (APIs for Sense HAT)
 
 Issues/Dependencies:
 - export DISPLAY='<serverIP>:0.0'
 - update X0Hosts on server to allow clients IP
 - Update PYTHONPATH as per Lab Module 1
 - Install basic imports to replicate the venv.
 
 

How does your implementation work?
When the CDA app is run, DeviceDataManager is called to start and stop in the app's start / stop methods. 
 - The startManager method invokes SensorAdapterManager and ActuatorAdaptorManager.
 - Managers have schedulers that runs the jobs. 
 - A SensorAdaptorManager checks if useEmulators is true or false. If true, uses the current implementation of getting the data from the emulator else gets minValue and maxValue of humidity, pressure and temperature from SensorDataGenerator
 - SensorData is formed calling humidityEmulator, similarly for pressure and temperature
 - This sensorData is now available at DeviceDataManager for data analysis
 Similarly, ActuatorAdaptorManager is used to generate the data required to simulate/emulate the actuators and the ActuatorSimTask will send the commands to the Actuators



### Code Repository and Branch

URL: https://github.com/NU-CSYE6530-Fall2020/constrained-device-app-kiran-ramesh-s/tree/chapter04

### UML Design Diagram(s)
![CDA](https://github.com/NU-CSYE6530-Fall2020/constrained-device-app-kiran-ramesh-s/blob/chapter04/uml/lab4_CDA.png?raw=true)


### Unit Tests Executed

- All unit tests under part02 except DataUtilTest

### Integration Tests Executed
 - ./emulated/SenseHatEmulatorQuickTest
 - ./emulated/SensorEmulatorManagerTest
 - ./emulated/ActuatorEmulatorManagerTest

 - SensorAdapterManagerTest
 - ActuatorAdapterManagerTest



EOF.
