class Animation:
    OFFSET_NUM_FRAMES = 0
    OFFSET_PNG = 1
    index = 0
    frame = 0
    frames = None
    
    def __init__(self):
        pass

    def frameChanged(self):
        self.frame = self.frame - 1
        if (self.frame < 0):
            self.index = self.index + 1
            if (self.index >= len(self.frames)):
                self.index = 0
            self.frame = self.frames[self.index][self.OFFSET_NUM_FRAMES]
            return True
        return False

    def getCurrentFrame(self):
        return self.frames[self.index][self.OFFSET_PNG]

class LeftAnimation(Animation):
    
    def __init__(self, frame1, frame2):
        super().__init__()
        self.frames = ((50, frame1), (100, frame2), (50, frame1))

class RightAnimation(Animation):
    
    def __init__(self, frame1, frame2):
        super().__init__()
        self.frames = ((100, frame1), (100, frame2))
