
import const

def getMapping(controllerName):
    if controllerName == const.CONTROLLER_XBOX360:
        return XBox360Mapping()
    if controllerName == const.CONTROLLER_PS4:
        return PS4Mapping()
    return None

class Mapping:
    
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
        self.mapping[const.BTN_L1] = [310,1,0,1]
        self.mapping[const.BTN_L2] = [2,3,0,255]
        self.mapping[const.BTN_L3] = [317,1,0,1]
        self.mapping[const.BTN_L3_H] = [0,3,-32768,32767]
        self.mapping[const.BTN_L3_V] = [1,3,-32768,32767]
        self.mapping[const.BTN_R1] = [311,1,0,1]
        self.mapping[const.BTN_R2] = [5,3,0,255]
        self.mapping[const.BTN_R3] = [318,1,0,1]
        self.mapping[const.BTN_R3_H] = [3,3,-32768,32767]
        self.mapping[const.BTN_R3_V] = [4,3,-32768,32767]
        self.mapping[const.BTN_DPAD_H] = [16,3,-1,1]
        self.mapping[const.BTN_DPAD_V] = [17,3,-1,1]
        self.mapping[const.BTN_A] = [304,1,0,1]
        self.mapping[const.BTN_B] = [305,1,0,1]
        self.mapping[const.BTN_C] = [307,1,0,1]
        self.mapping[const.BTN_D] = [308,1,0,1]
        self.mapping[const.BTN_E] = [314,1,0,1]
        self.mapping[const.BTN_F] = [315,1,0,1]
        self.mapping[const.BTN_G] = [316,1,0,1]
    
   
class PS4Mapping(Mapping):
    
    def __init__(self):
        self.mapping[const.BTN_L1] = [310,1,0,1]
        self.mapping[const.BTN_L2] = [2,3,0,255]
        self.mapping[const.BTN_L3] = [317,1,0,1]
        self.mapping[const.BTN_L3_H] = [0,3,0,255]
        self.mapping[const.BTN_L3_V] = [1,3,0,255]
        self.mapping[const.BTN_R1] = [311,1,0,1]
        self.mapping[const.BTN_R2] = [5,3,0,255]
        self.mapping[const.BTN_R3] = [318,1,0,1]
        self.mapping[const.BTN_R3_H] = [3,3,0,255]
        self.mapping[const.BTN_R3_V] = [4,3,0,255]
        self.mapping[const.BTN_DPAD_H] = [16,3,-1,1]
        self.mapping[const.BTN_DPAD_V] = [17,3,-1,1]
        self.mapping[const.BTN_A] = [304,1,0,1]
        self.mapping[const.BTN_B] = [305,1,0,1]
        self.mapping[const.BTN_C] = [308,1,0,1]
        self.mapping[const.BTN_D] = [307,1,0,1]
        self.mapping[const.BTN_E] = [314,1,0,1]
        self.mapping[const.BTN_F] = [315,1,0,1]
        self.mapping[const.BTN_G] = [316,1,0,1]
    
