from PIL import Image

class Png:

    pacman = None
    pacman2 = None
    ghost = None
    ghost2 = None
    sun = None
    sun2 = None
    heart = None
    heart2 = None
    unicorn = None
    cat = None
    
    def __init__(self):
        self.pacman = list(Image.open(r"pacman.png").getdata())
        self.pacman2 = list(Image.open(r"pacman2.png").getdata())
        self.ghost = list(Image.open(r"ghost.png").getdata())
        self.ghost2 = list(Image.open(r"ghost2.png").getdata())
        self.sun = list(Image.open(r"sun.png").getdata())
        self.sun2 = list(Image.open(r"sun2.png").getdata())
        self.heart = list(Image.open(r"heart.png").getdata())
        self.heart2 = list(Image.open(r"heart2.png").getdata())
        self.unicorn = list(Image.open(r"unicorn.png").getdata())
        self.cat = list(Image.open(r"cat.png").getdata())

    def getPacman(self):
        return self.pacman

    def getPacman2(self):
        return self.pacman2

    def getGhost(self):
        return self.ghost
    
    def getGhost2(self):
        return self.ghost2
    
    def getSun(self):
        return self.sun

    def getSun2(self):
        return self.sun2

    def getHeart(self):
        return self.heart
    
    def getHeart2(self):
        return self.heart2

    def getUnicorn(self):
        return self.unicorn
    
    def getCat(self):
        return self.cat