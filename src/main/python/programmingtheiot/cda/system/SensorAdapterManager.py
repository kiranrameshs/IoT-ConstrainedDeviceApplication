#####
# 
# This class is part of the Programming the Internet of Things project.
# 
# It is provided as a simple shell to guide the student and assist with
# implementation for the Programming the Internet of Things exercises,
# and designed to be modified by the student as needed.
#

import logging

from apscheduler.schedulers.background import BackgroundScheduler

from programmingtheiot.common.IDataMessageListener import IDataMessageListener
from programmingtheiot.common import ConfigConst

from programmingtheiot.cda.sim.TemperatureSensorSimTask import TemperatureSensorSimTask
from programmingtheiot.cda.sim.HumiditySensorSimTask import HumiditySensorSimTask
from programmingtheiot.cda.sim.SensorDataGenerator import SensorDataGenerator
from programmingtheiot.common.ConfigUtil import ConfigUtil
from programmingtheiot.cda.sim.PressureSensorSimTask import PressureSensorSimTask

from math import fabs

class SensorAdapterManager(object):
	"""
	Initialize the data based on Emulators/simulators
	"""
	def __init__(self, useEmulator: bool = True, pollRate: int = 20, allowConfigOverride: bool = True):
		self.dataMessageListener = None;
		self.useEmulator = useEmulator;
		self.pollRate = pollRate;
		self.scheduler = BackgroundScheduler()
		self.scheduler.add_job(self.handleTelemetry, 'interval', seconds = self.pollRate)
		if(self.useEmulator):
			logging.info("Using Emulators")
			humidityModule = __import__('programmingtheiot.cda.emulated.HumiditySensorEmulatorTask', fromlist = ['HumiditySensorEmulatorTask'])
			heClazz = getattr(humidityModule, 'HumiditySensorEmulatorTask')
			self.humidityEmulator = heClazz()
			tempModule = __import__('programmingtheiot.cda.emulated.TemperatureSensorEmulatorTask', fromlist = ['TemperatureSensorEmulatorTask'])
			tempClazz = getattr(tempModule, 'TemperatureSensorEmulatorTask')
			self.tempEmulator = tempClazz()
			pressureModule = __import__('programmingtheiot.cda.emulated.PressureSensorEmulatorTask', fromlist = ['PressureSensorEmulatorTask'])
			pClazz = getattr(pressureModule, 'PressureSensorEmulatorTask')
			self.pressureEmulator = pClazz()
			cameraModule = __import__('programmingtheiot.cda.emulated.CameraSensorEmulatorTask', fromlist = ['CameraSensorEmulatorTask'])
			camClazz = getattr(cameraModule, 'CameraSensorEmulatorTask')
			self.cameraEmulator = camClazz()
		else:
			logging.info("Using Simulators")
			self.dataGenerator = SensorDataGenerator()
			configUtil = ConfigUtil()
			humidityFloor = configUtil.getFloat(ConfigConst.CONSTRAINED_DEVICE, ConfigConst.HUMIDITY_SIM_FLOOR_KEY, SensorDataGenerator.LOW_NORMAL_ENV_HUMIDITY)
			humidityCeiling = configUtil.getFloat(ConfigConst.CONSTRAINED_DEVICE, ConfigConst.HUMIDITY_SIM_CEILING_KEY, SensorDataGenerator.HI_NORMAL_ENV_HUMIDITY)
			pressureFloor = configUtil.getFloat(ConfigConst.CONSTRAINED_DEVICE, ConfigConst.PRESSURE_SIM_FLOOR_KEY, SensorDataGenerator.LOW_NORMAL_ENV_PRESSURE)
			pressureCeiling = configUtil.getFloat(ConfigConst.CONSTRAINED_DEVICE, ConfigConst.PRESSURE_SIM_CEILING_KEY, SensorDataGenerator.HI_NORMAL_ENV_PRESSURE)
			temperatureFloor = configUtil.getFloat(ConfigConst.CONSTRAINED_DEVICE, ConfigConst.TEMP_SIM_FLOOR_KEY, SensorDataGenerator.LOW_NORMAL_INDOOR_TEMP)
			temperatureCeiling = configUtil.getFloat(ConfigConst.CONSTRAINED_DEVICE, ConfigConst.TEMP_SIM_CEILING_KEY, SensorDataGenerator.HI_NORMAL_INDOOR_TEMP)
			humidityData = self.dataGenerator.generateDailyEnvironmentHumidityDataSet(minValue = humidityFloor, maxValue = humidityCeiling, useSeconds = False);
			pressureData = self.dataGenerator.generateDailyEnvironmentPressureDataSet(minValue = pressureFloor, maxValue = pressureCeiling, useSeconds = False);
			temperatureData = self.dataGenerator.generateDailyIndoorTemperatureDataSet(minValue = temperatureFloor, maxValue = temperatureCeiling, useSeconds = False);
			self.humiditySenorSimTask = HumiditySensorSimTask(dataSet=humidityData);
			self.pressureSenorSimTask = PressureSensorSimTask(dataSet=pressureData);
			self.temperatureSenorSimTask = TemperatureSensorSimTask(dataSet=temperatureData);
			
	def handleTelemetry(self):
		if(self.useEmulator == True):
			humiditySensorData = self.humidityEmulator.generateTelemetry()
			pressureSensorData = self.pressureEmulator.generateTelemetry()
			temperatureSensorData =  self.tempEmulator.generateTelemetry()
			cameraSensorData = self.cameraEmulator.generateTelemetry()
			self.dataMessageListener.handleSensorMessage(humiditySensorData)
			self.dataMessageListener.handleSensorMessage(pressureSensorData)
			self.dataMessageListener.handleSensorMessage(temperatureSensorData)
			self.dataMessageListener.handleSensorMessage(cameraSensorData)
		else:
			humiditySensorData = self.humiditySenorSimTask.generateTelemetry()
			pressureSensorData = self.pressureSenorSimTask.generateTelemetry()
			temperatureSensorData =  self.temperatureSenorSimTask.generateTelemetry()
			self.dataMessageListener.handleSensorMessage(humiditySensorData)
			self.dataMessageListener.handleSensorMessage(pressureSensorData)
			self.dataMessageListener.handleSensorMessage(temperatureSensorData)
		
	def setDataMessageListener(self, listener: IDataMessageListener) -> bool:
		if(self.dataMessageListener== None):
			self.dataMessageListener = listener;
			return True;
		else:
			return False;
	
	def startManager(self):
		self.scheduler.start()
		
	def stopManager(self):
		self.scheduler.shutdown()
