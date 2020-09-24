# Constrained Device Application (Connected Devices)

## Lab Module 02
  - Create the ConstrainedDeviceApp application in Python
  - Create a new Python module named SystemPerformanceManager with class name SystemPerformanceManager
  - Create an instance of SystemPerformanceManager within ConstrainedDeviceApp and invoke the manager's start / stop methods within the app's start / stop methods
  - Create (edit) a new Python module named BaseSystemUtilTask with class name BaseSystemUtilTask
  - Create a new Python module named SystemCpuUtilTask with class name SystemCpuUtilTask
  - Create a new Python module named SystemMemUtilTask with class name SystemMemUtilTask
  - Create an instance of SystemCpuUtilTask and SystemMemUtilTask within SystemPerformanceManager and use the apscheduler library to run each task at a regular interval
  - Verify and merge Chapter 02 branch into the primary branch

### Description

What does your implementation do? 
In this lab module, SystemPerformanceManager was implemented and connected to the CDA. This module provides the System CPU Utilization values and System Memory Utilization values during runtime. Meanwhile, to verify the implementation, SystemPerformanceManagerTest was updated to run the jobs using BackgroundScheduler class from apscheduler.schedulers.background module

How does your implementation work?
When the CDA app is run, SystemPerformanceManager is called to start and stop in the app's start / stop methods. It has an instance of SystemCpuUtilTask and SystemMemUtilTask which are inherited from BaseSystemUtilTask. This base class has a method getTelemetryValue which calls a template called _getSystemUtil which are implemnted in the child classes. The child classes uses the library psutil and gets the values psutil.cpu_percent() and psutil.virtual_memory().percent 
The SystemPerformanceManagerTest runs the test with poll time of 30 seconds using the jobs called inside the startManager() and stopManager() methods

### Code Repository and Branch

URL: https://github.com/NU-CSYE6530-Fall2020/constrained-device-app-kiran-ramesh-s/tree/chapter02

### UML Design Diagram(s)
![CDA](https://github.com/NU-CSYE6530-Fall2020/constrained-device-app-kiran-ramesh-s/blob/chapter02/uml/lab2_CDA.png?raw=true)


### Unit Tests Executed

- ./common/ConfigUtilTest.
- ./system/SystemCpuUtilTaskTest
- ./system/SystemmemUtilTaskTest

### Integration Tests Executed

- ./app/ConstrainedDeviceAppTest
- ./system/SystemPerformanceManagerTest.

EOF.
