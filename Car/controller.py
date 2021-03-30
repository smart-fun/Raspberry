#Controller: pad or wheel controller

#!/usr/bin/python
from devices import selectDevice
from evdev import InputDevice
from mapping import *
import const

class Controller:
    wheel = 50
    speed = 50
    controller = None
    mapp = None
    supportedDevices = [const.CONTROLLER_XBOX360, const.CONTROLLER_PS4]
    
    def __init__(self):
        wheel = 50

    def select(self):
        device = selectDevice()
        if (device.name not in self.supportedDevices):
            print("device not supported, use", self.supportedDevices)
            return False
        else:
            self.controller = InputDevice(device.path)
            self.mapp = getMapping(device.name)
            print("using", self.controller)
            return True

    def update(self, displayDebug):
        event = self.controller.read_one()
        while(event != None):
            
            key,value = self.mapp.getNormalizedValue(event.code, event.type, event.value)
            if (key != None):
                if (key == const.BTN_L2):
                    self.speed = int(50 + (value / 2))
                elif (key == const.BTN_R2):
                    self.speed = int(50 - (value / 2))
                elif (key == const.BTN_L3_H):
                    self.wheel = int(value)
            
            event = self.controller.read_one()

    def getWheel(self):
        return self.wheel

    def getSpeed(self):
        return self.speed
