# Constrained Device Application (Connected Devices)

## Lab Module 12


### Description
  - Setup connection between GDA and a CDA
  - Implement the handle actuator command function to receive the actuator co9mmand from the GDA and pass it to the right actuator
  - The emulator task fuctionality is also updated to use the right interface to use the received data to pass it to alert the user
  - Implement the functionality of forwarding all the sensor data to GDA based on the poll cycle 

What does your implementation do? 
The goal of this project is to detect illegal intrusion both indoors as well as outdoors and this can be handled setting up ceiling and flooring values accordingly. So the pressure sensor and the temperature sensor continuously reports the sensor data to GDA and GDA decides the data has crossed the threshold meaning the intrusion has taken place and the same is displayed to the end user on the LED (assumed to tbe the actuation action just like an alarm). Also, the data is forwarded to the cloud service and the service also sends an email to the end user notifying about the intrusion.

How does your implementation work?
When the CDA and GDA is running, CDA subscribes to a topic (in this case a display command topic). CDA continuously sends data to the GDA and GDA checks if the values are under the threshold. If the values cross the mentioned threshold, GDA triggers an actuator command with a value and a LED display message on the topic subscribed by the CDa so the CDA receives this message and handles the actuator command, sends it to the respective emulator (in this case LED assuming it to be an alarm) displays a message. Here the implementation also handles only if the sensor data crosses the threshold in a particular direction (greater than a ceiling value or lesser than a floor value) and does not keep sending the actuator command continuously unless the event has occurred in the same direction again. All the communication between the CDA and GDA and cloud services are taking place using the MQTT protocol 




### Code Repository and Branch

URL: https://github.com/NU-CSYE6530-Fall2020/constrained-device-app-kiran-ramesh-s/tree/chapter12

### UML Design Diagram(s)
![CDA](https://github.com/NU-CSYE6530-Fall2020/constrained-device-app-kiran-ramesh-s/blob/chapter12/uml/lab12_CDA.png?raw=true)


 
 
### Unit Tests Executed

 - NA

### Integration Tests Executed

 -Manually run the CDA and GDA application. Keep pressure value greater than the floor value and temperature value greater than the floor value as well. If the values are not crossing the floor values then the actuator command is not published. If the value crosses the floor value then the actuator command is triggered by the GDA with respect to temperature. With respect to  pressure, the same is done by the Ubidots in terms of an email.