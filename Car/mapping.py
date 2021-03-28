
def getMapping(controllerName):
    if controllerName == "Microsoft X-Box 360 pad":
        return XBox360Mapping()
    if controllerName == "Sony Computer Entertainment Wireless Controller":
        return PS4Mapping()

# functions return button code, type, min value, max value
class Mapping:
    def getBreakButton(self):
        pass
    def getAccelerateButton(self):
        pass
    def getDirectionButton(self):
        pass
    
class XBox360Mapping(Mapping):
    def getBreakButton(self):
        return [2,3,0,255]
    def getAccelerateButton(self):
        return [5,3,0,255]
    def getDirectionButton(self):
        return [0,3,-32768,32767]
    
'''
"Microsoft X-Box 360 pad" mapping

0 T3: Left Stick H (-32768 - +32767)
1 T3: Left Stick V (-32768 - +32767)
2 T3: L2 (0-255)
3 T3: Right Stick H (-32768 - +32768)
4 T3: Right Stick V (-32768 - +32768)
5 T3: R2 (0-255)
16 T3: Digital Left/Middle/Right (-1/0/1)
17 T3: Digital Up/Middle/Down (-1/0/1)
304 T3: A (0/1)
305 T3: B (0/1)
307 T3: X (0/1)
308 T3: Y (0/1)
310 T3: L1 (0/1)
311 T3: R1 (0/1)
314 T3: Back (0/1)
315 T3: Start (0/1)
316 T3: XBox (0/1)
'''

class PS4Mapping(Mapping):
    def getBreakButton(self):
        return [2,3,0,255]
    def getAccelerateButton(self):
        return [5,3,0,255]
    def getDirectionButton(self):
        return [0,3,0,255]
    
'''
"Sony Computer Entertainment Wireless Controller" mapping (Pad Ps4)

0 T3: Left Stick H (0 - 255)
1 T3: Left Stick V (0 - 255)
2 T3: L2 (0-255)
3 T3: Right Stick H (0 - 255)
4 T3: Right Stick V (0 - 255)
5 T3: R2 (0-255)
16 T3: Digital Left/Middle/Right (-1/0/1)
17 T3: Digital Up/Middle/Down (-1/0/1)
310 T1: L1
311 T1: R1
304 T1: CROSS
305 T1: CIRCLE
307 T1: TRIANGLE
308 T1: SQUARE
314 T1: SHARE
315 T1: OPTIONS
316 T1: PS
317 T1: THUMB LEFT
318 T1: THUMB RIGHT
'''
