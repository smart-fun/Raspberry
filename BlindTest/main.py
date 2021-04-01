import pygame as pg
import pygame_widgets as pw
from display import *

pg.init()
screen = createScreen()

displayCircle(screen, "READY?")

running = True

startButton = displayStartButton(screen, lambda: print('Start!'))

while running:
    events = pg.event.get()
    for event in events:
        if event.type == pg.QUIT:
            running = False
    startButton.listen(events)
    startButton.draw()
    pg.display.update()

pg.quit()
