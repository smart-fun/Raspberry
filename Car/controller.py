#Controller: pad or wheel controller

#!/usr/bin/python
from devices import selectDevice
from evdev import InputDevice
from mapping import *

class Controller:
    wheel = 50
    speed = 50
    controller = None
    mapping = None
    supportedDevices = ["Microsoft X-Box 360 pad", "Sony Computer Entertainment Wireless Controller"]
    
    def __init__(self):
        wheel = 50

    def select(self):
        device = selectDevice()
        if (device.name not in self.supportedDevices):
            print("device not supported, use", self.supportedDevices)
            return False
        else:
            self.controller = InputDevice(device.path)
            self.mapping = getMapping(device.name)
            print("using", self.controller)
            return True

    def update(self, displayDebug):
        event = self.controller.read_one()
        while(event != None):
            
            key,value = self.mapping.getNormalizedValue(event.code, event.type, event.value)
            if (key != None):
                if (key == "L2"):
                    self.speed = int(50 + (value / 2))
                elif (key == "R2"):
                    self.speed = int(50 - (value / 2))
                elif (key == "L3_H"):
                    self.wheel = int(value)
            
            event = self.controller.read_one()

    def getWheel(self):
        return self.wheel

    def getSpeed(self):
        return self.speed
