
def getMapping(controllerName):
    if controllerName == "Microsoft X-Box 360 pad":
        return XBox360Mapping()
    if controllerName == "Sony Computer Entertainment Wireless Controller":
        return PS4Mapping()

class Mapping:
    
    BTN_L1 = "L1"
    BTN_L2 = "L2"
    BTN_L3 = "L3"
    BTN_L3_H = "L3_H"
    BTN_L3_V = "L3_V"
    BTN_R1 = "R1"
    BTN_R2 = "R2"
    BTN_R3 = "R3"
    BTN_R3_H = "R3_H"
    BTN_R3_V = "R3_V"
    BTN_DPAD_H = "DPAD_H"
    BTN_DPAD_V = "DPAD_V"
    BTN_A = "A"
    BTN_B = "B"
    BTN_C = "C"
    BTN_D = "D"
    BTN_E = "E"
    BTN_F = "F"
    BTN_G = "G"
    mapping = {}
    
    def fromCodeAndType(self, evCode, evType): #returns key, values
        for key in self.mapping.keys():
            c = self.mapping[key][0]
            t = self.mapping[key][1]
            if (self.mapping[key][0] == evCode) and (self.mapping[key][1] == evType):
                return key, self.mapping[key]
        return None, None
    
    def getNormalizedValue(self, evCode, evType, evValue):
        key, values = self.fromCodeAndType(evCode, evType)
        if (key == None):
            return None, None
        else:
            vmin = values[2]
            vmax = values[3]
            value = int((evValue - vmin) / (vmax - vmin) * 100)
            return key, value
   
    
class XBox360Mapping(Mapping):
    
    def __init__(self):
        self.mapping[self.BTN_L1] = [310,1,0,1]
        self.mapping[self.BTN_L2] = [2,3,0,255]
        self.mapping[self.BTN_L3] = [317,1,0,1]
        self.mapping[self.BTN_L3_H] = [0,3,-32768,32767]
        self.mapping[self.BTN_L3_V] = [1,3,-32768,32767]
        self.mapping[self.BTN_R1] = [311,1,0,1]
        self.mapping[self.BTN_R2] = [5,3,0,255]
        self.mapping[self.BTN_R3] = [318,1,0,1]
        self.mapping[self.BTN_R3_H] = [3,3,-32768,32767]
        self.mapping[self.BTN_R3_V] = [4,3,-32768,32767]
        self.mapping[self.BTN_DPAD_H] = [16,3,-1,1]
        self.mapping[self.BTN_DPAD_V] = [17,3,-1,1]
        self.mapping[self.BTN_A] = [304,1,0,1]
        self.mapping[self.BTN_B] = [305,1,0,1]
        self.mapping[self.BTN_C] = [307,1,0,1]
        self.mapping[self.BTN_D] = [308,1,0,1]
        self.mapping[self.BTN_E] = [314,1,0,1]
        self.mapping[self.BTN_F] = [315,1,0,1]
        self.mapping[self.BTN_G] = [316,1,0,1]
    
    def getBreakButton(self):
        return [2,3,0,255]
    def getAccelerateButton(self):
        return [5,3,0,255]
    def getDirectionButton(self):
        return [0,3,-32768,32767]
    
class PS4Mapping(Mapping):
    
    def __init__(self):
        self.mapping[self.BTN_L1] = [310,1,0,1]
        self.mapping[self.BTN_L2] = [2,3,0,255]
        self.mapping[self.BTN_L3] = [317,1,0,1]
        self.mapping[self.BTN_L3_H] = [0,3,0,255]
        self.mapping[self.BTN_L3_V] = [1,3,0,255]
        self.mapping[self.BTN_R1] = [311,1,0,1]
        self.mapping[self.BTN_R2] = [5,3,0,255]
        self.mapping[self.BTN_R3] = [318,1,0,1]
        self.mapping[self.BTN_R3_H] = [3,3,0,255]
        self.mapping[self.BTN_R3_V] = [4,3,0,255]
        self.mapping[self.BTN_DPAD_H] = [16,3,-1,1]
        self.mapping[self.BTN_DPAD_V] = [17,3,-1,1]
        self.mapping[self.BTN_A] = [304,1,0,1]
        self.mapping[self.BTN_B] = [305,1,0,1]
        self.mapping[self.BTN_C] = [308,1,0,1]
        self.mapping[self.BTN_D] = [307,1,0,1]
        self.mapping[self.BTN_E] = [314,1,0,1]
        self.mapping[self.BTN_F] = [315,1,0,1]
        self.mapping[self.BTN_G] = [316,1,0,1]
    
