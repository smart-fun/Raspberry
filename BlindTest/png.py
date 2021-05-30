from PIL import Image

class Png:

    pacman = None
    ghost = None
    
    def __init__(self):
        self.pacman = list(Image.open(r"pacman.png").getdata())
        self.ghost = list(Image.open(r"ghost.png").getdata())

    def getPacman(self):
        return self.pacman
        
    def getGhost(self):
        return self.ghost

