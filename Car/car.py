from time import sleep
#!/usr/bin/python
from controller import *
from mcp4728 import *

displayDebug = True

mcp = MCP4728()
mcp.init()
controller = Controller()
previousSpeed = 0
previousWheel = 0
if not controller.select():
    print("Controller not compatible")
else:
    while True:
        controller.update(displayDebug)
        speed = controller.getSpeed()
        wheel = controller.getWheel()
        update = False

        if (previousSpeed != speed):
            previousSpeed = speed
            print("speed",speed)
            update = True
        if (previousWheel != wheel):
            previousWheel = wheel
            print("wheel",wheel)
            update = True

        if (update):
            mcp.update(speed, wheel)
        
        sleep(0.05)
