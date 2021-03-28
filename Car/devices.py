# List available devices, and asks the user to choose one

import evdev

def selectDevice():
    devices = [evdev.InputDevice(path) for path in evdev.list_devices()]
    print("Available devices:")
    print("------------------")
    numDevices = len(devices)
    for i in range(numDevices):
        device = devices[i]
        print(i, "-", device.name)

    devNum = int(input("\nChoose a device: "))
    device = devices[devNum]
    return device


#device = selectDevice()
#print("Selected: ", device.name, "-", device.path)
