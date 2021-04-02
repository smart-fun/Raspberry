# see https://cdn-learn.adafruit.com/downloads/pdf/neopixels-on-raspberry-pi.pdf

import board
import neopixel

class NeoPixel24:
    pixels = None

    def __init__(self):
        self.pixels = neopixel.NeoPixel(board.D10, 24, brightness=0.3, auto_write=False, pixel_order=neopixel.GRB);

    def fillColor(self, color):
        print("neo color", color)
        self.pixels.fill(color)
        self.pixels.show()

    def fillColors(self, col1, col2):
        for i in range(24):
            if (int(i/3) % 2) == 0:
                self.pixels[i] = col1
            else:
                self.pixels[i] = col2
        self.pixels.show()
        
    def rotate(self):
        first = self.pixels[0]
        for i in range(0,23):
            self.pixels[i] = self.pixels[i+1]
        self.pixels[23] = first
        self.pixels.show()