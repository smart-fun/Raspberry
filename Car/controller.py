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
        breakButton = self.mapping.getBreakButton()
        accelerateButton = self.mapping.getAccelerateButton()
        directionButton = self.mapping.getDirectionButton()
        event = self.controller.read_one()
        while(event != None):
            if (event.code == breakButton[0] and event.type == breakButton[1]):
                vmin = breakButton[2]
                vmax = breakButton[3]
                value = (event.value - vmin) / (vmax - vmin) * 100 # 0-100
                self.speed = int(50 + (value / 2))
            if (event.code == accelerateButton[0] and event.type == accelerateButton[1]):
                vmin = accelerateButton[2]
                vmax = accelerateButton[3]
                value = (event.value - vmin) / (vmax - vmin) * 100 # 0-100
                self.speed = int(50 - (value / 2))
            if (event.code == directionButton[0] and event.type == directionButton[1]):
                vmin = directionButton[2]
                vmax = directionButton[3]
                value = (event.value - vmin) / (vmax - vmin) * 100 # 0-100
                self.wheel = int(value)
                
            if displayDebug:
                print("code", event.code, "type", event.type, "value", event.value)
            event = self.controller.read_one()


    def getWheel(self):
        return self.wheel

    def getSpeed(self):
        return self.speed
