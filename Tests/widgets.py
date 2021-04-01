#pip3 install pygame_widgets
#sudo apt install libsdl2-ttf-2.0-0
import pygame as pg
import pygame_widgets as pw
from display import *
# creating screen
pg.init()

#screen = pg.display.set_mode((800, 600))
screen = createScreen()

displayCircle(screen, "READY?")

running = True

startButton = displayStartButton(screen, lambda: print('Yopla'))

while running:
    events = pg.event.get()
    for event in events:
        if event.type == pg.QUIT:
            running = False
    startButton.listen(events)
    startButton.draw()
    pg.display.update()

pg.quit()
