import machine
import time
import json
import webserver
import task
import os


class Setup:
    def __init__(self):
        self.data = "data"
        os.makedirs(self.data, exists_ok=True)


class Log:
    def __init__(self, data, location, file_name):
        self.data = data
        self.location = location
        self.file_name = file_name

    def CreateFiel(self):
        self.file_path = os.path.join(self.location, f"{self.file_name}.txt")
        with open(self.file_path, "w") as f:
            f.write(str(self.data))

class TemperatureSystem:
    def __init__(self, pin):
        self.pin = pin
        self.sensor = machine.ADC(self.pin)
        self.conversion = 3.3 / 65535

    def GetTemperature(self, running):
        self.running = running
        while self.running:
            self.raw_value = self.sensor.read_u16()
            self.voltage = self.raw_value * self.conversion
            self.temperature = 27 - (self.voltage -0.706) / 0.001721

            print(f"Temperature: {self.temperature:.2f} ℃")

class OnBoardLEDSystem:
    def __init__(self, pin, delay):
        self.pin = pin
        self.delay = delay
        self.LED = machine.Pin(self.pin, machine.Pin.OUT)
    
    def LED_On(self):
        self.LED.value(1)

    def LED_Off(self):
        self.LED.value(0)

    def blink(self):
        self.LED.value(1)
        time.sleep(self.delay)
        self.LED.value(0)


setup = Setup()
log = Log()

    
