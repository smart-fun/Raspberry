#Display 8x8 test MAX7219/7221
# https://github.com/rm-hull/luma.led_matrix
import board
import busio
from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.led_matrix.device import max7219

class Display88:
    
    device = None
    
    def __init__(self):
        serial = spi(port=0, device=0, gpio=noop())
        self.device = max7219(serial, width=16, height=8)
        self.device.contrast(50)

    def drawScore(self, scoreRed, scoreYellow):
        with canvas(self.device) as draw:
            draw.text((1, -1), str(scoreRed), fill="white")
            draw.text((9, -1), str(scoreYellow), fill="white")
 
    def drawImages(self, imageRed, imageYellow):
        with canvas(self.device) as draw:
            if (imageRed != None):
                self.drawImage(draw, imageRed, 0)
            if (imageYellow != None):
                self.drawImage(draw, imageYellow, 8)
 
    def drawImage(self, draw, image, offset):
        for y in range(8):
            for x in range(8):
                point = image[x + (y*8)]
                if point[0] != 0:
                    draw.point((x + offset,y), "white")

    def drawRectangleYellow(self):
        with canvas(self.device) as draw:
            draw.rectangle(((8,0),(15,7)),"white")
            
    def drawRectangleRed(self):
        with canvas(self.device) as draw:
            draw.rectangle(((0,0),(7,7)),"white")
    
    def hide(self):
        self.device.hide()
                    
