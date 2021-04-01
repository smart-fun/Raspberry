# see https://cdn-learn.adafruit.com/downloads/pdf/neopixels-on-raspberry-pi.pdf

import board
import neopixel
from time import sleep

pixels = neopixel.NeoPixel(board.D10, 24, brightness=0.3, auto_write=False, pixel_order=neopixel.GRB);

for i in range(24):
    r = 0
    g = 0
    b = 0
    if (i < 8):
        r = 255 - (i*30)
        g = i * 30
    elif (i >= 16):
        r = (i-16) * 30
        b = (i-15) * 30
    else:
        g = (i-7) * 30
        b = 255 - ((i-7) * 30)
    
    pixels[i] = (r,g,b)

pixels.show()
sleep(3)


while True:
    
    pixels.fill((0,0,255))
    pixels.show()
    sleep(2)

    pixels.fill((255,0,0))
    pixels.show()
    sleep(2)
