#Controller: pad or wheel controller

#!/usr/bin/python
from devices import selectDevice
from evdev import InputDevice
from mapping import *
import const

class Controller:
    wheel = 50    # Centered
    speed = 50    # Stopped
    controller = None
    mapping = None
    supportedDevices = [const.CONTROLLER_XBOX360, const.CONTROLLER_PS4]
    # Button Binding:
    BUTTON_BREAK = const.BTN_L2
    BUTTON_ACCELERATE = const.BTN_R2
    BUTTON_DIRECTION = const.BTN_L3_H

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
                if (key == self.BUTTON_BREAK):
                    self.speed = int(50 + (value / 2))
                elif (key == self.BUTTON_ACCELERATE):
                    self.speed = int(50 - (value / 2))
                elif (key == self.BUTTON_DIRECTION):
                    self.wheel = int(value)
            
            event = self.controller.read_one()

    def getWheel(self):
        return self.wheel

    def getSpeed(self):
        return self.speed
