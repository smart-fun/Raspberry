import pygame as pg
import pygame_widgets as pw
from display import *
from enum import IntEnum

class State(IntEnum):
    READY = 1
    PLAYING = 2
    PROPOSING_RED = 3
    PROPOSING_YELLOW = 4

state = State.READY

def startGame():
    global state
    global screen
    global startButton
    state = State.PLAYING
    print("New State", state)
    startButton.hide()
    screen.fill(GREY)
    displayCircle(screen, "PLAYING", True, True)
    
def yellowPress():
    global state
    print("Yellow Press!")
    if (state == State.PLAYING):
        state = State.PROPOSING_YELLOW
        displayCircle(screen, "CORRECT?", True, False)

def redPress():
    print("Red Press!")

pg.init()
screen = createScreen()

displayCircle(screen, "READY?", True, True)

startButton = displayStartButton(screen, lambda: startGame())

running = True
while running:
    events = pg.event.get()
    for event in events:
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.KEYDOWN:
            if (event.unicode == 'y'):
                yellowPress()
            elif (event.unicode == 'r'):
                redPress()
    
    if (state == State.READY):
        startButton.listen(events)
        startButton.draw()
        
    pg.display.update()

pg.quit()
