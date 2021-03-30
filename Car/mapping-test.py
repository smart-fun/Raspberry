from devices import selectDevice
from evdev import InputDevice
from mapping import *

device = selectDevice()
if (device != None):
    controller = InputDevice(device.path)
    mapping = getMapping(device.name)
    if (mapping != None):
        while True:
            event = controller.read_one()
            while(event != None):
                key, values = mapping.fromCodeAndType(event.code, event.type)
                if (key != None):
                    if (key.startswith("L3_") or key.startswith("R3_")):
                        pass
                    else:
                        vmin = values[2]
                        vmax = values[3]
                        value = int((event.value - vmin) / (vmax - vmin) * 100)
                        print(key, value)
                event = controller.read_one()

