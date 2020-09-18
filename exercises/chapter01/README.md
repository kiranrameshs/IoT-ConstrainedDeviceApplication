# Constrained Device Application (Connected Devices)

## Lab Module 01


### Description

NOTE: Include two full paragraphs describing your implementation approach by answering the questions listed below.

What does your implementation do? 
As part of first assignment, the task was to read Chapter 1 of Programming the Internet of Things, then setup the development environment for the CDA i.e. the Python components. 
First step was to initialise git in the respective folder and clone the the CDA repository. The virtual environment was set and activated in the cloned repository. The dependencies were installed in the virtual env using pip. Then import the project from the folder on to Eclipse IDE. Set the PYTHONPATH and the env path using Pydev. Run the ConstrainedDeviceApp.py from programmingtheiot.cda.app folder
CDA starts successfully as seen from the log prints from the console

How does your implementation work?
When the ConstrainedDeviceApp.py from programmingtheiot.cda.app folder is run, this gets an instance of the ConfigUtil.py which loads the configurations from DEFAULT_CONFIG_FILE_NAME (PiotConfig.props in this case). The CDA starts successfully as seen from the log prints in the console.


### Code Repository and Branch
URL: https://github.com/NU-CSYE6530-Fall2020/constrained-device-app-kiran-ramesh-s/tree/chapter01

### UML Design Diagram(s)

![CDA](https://github.com/NU-CSYE6530-Fall2020/constrained-device-app-kiran-ramesh-s/blob/chapter01/uml/lab1_CDA.png?raw=true)


### Unit Tests Executed
ConfigUtilTest (8/8)

### Integration Tests Executed

ConstrainedDeviceAppTest
SystemPerformanceManagerTest

EOF.
