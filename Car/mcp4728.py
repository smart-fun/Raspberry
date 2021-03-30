#MCP4728 module: i2c to variable current on 4 channels

import board
import busio
import adafruit_mcp4728
from time import sleep

class MCP4728:
    
    mcp4728 = None

    def init(self):
        try:
            i2c = busio.I2C(board.SCL, board.SDA)
        except:
            print("!!! I2C not activated !!!")
            return
        
        try:
            self.mcp4728 =  adafruit_mcp4728.MCP4728(i2c)
            self.mcp4728.channel_a.value = 32678# int(65535/4) # Voltage = VDD
            self.mcp4728.channel_b.value = 32678# int(65535/2) # VDD/2
            self.mcp4728.channel_c.value = 32678# int(65535/4) # VDD/4
            self.mcp4728.channel_d.value = 32678# 0V
            self.mcp4728.save_settings() # save the current values to the eeprom,making them the default on power up
        except:
            print("!!! MCP4728 SHIELD NOT FOUND !!!")

    def update(self, speed, wheel): #0-100
        if (self.mcp4728 != None):
            value = int(speed * 65535 / 100)
            self.mcp4728.channel_a.value = int(value)
            value = int(wheel * 65535 / 100)
            self.mcp4728.channel_b.value = int(value)
            self.mcp4728.save_settings()

