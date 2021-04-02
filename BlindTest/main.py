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
scoreYellow = 0
scoreRed = 0
startButton = None
yesButton = None
noButton = None

def goToReady():
    global state
    global screen
    global startButton
    global yesButton
    state = State.READY
    screen.fill(GREY)
    displayCircle(screen, "READY?", True, True)
    startButton.show()
    yesButton.hide()
    noButton.hide()
    if ((scoreYellow != 0) or (scoreRed != 0)):
        displayScore(screen, scoreYellow, scoreRed)

def goToPlaying():
    global state
    global screen
    global startButton
    state = State.PLAYING
    print("New State", state)
    startButton.hide()
    screen.fill(GREY)
    displayCircle(screen, "PLAYING", True, True)
    displayScore(screen, scoreYellow, scoreRed)
    
def yellowPress():
    global state
    global yesButton
    global noButton
    print("Yellow Press!")
    if (state == State.PLAYING):
        state = State.PROPOSING_YELLOW
        displayCircle(screen, "CORRECT?", True, False)
        yesButton.show()
        noButton.show()

def redPress():
    global state
    global yesButton
    global noButton
    print("Red Press!")
    if (state == State.PLAYING):
        state = State.PROPOSING_RED
        displayCircle(screen, "CORRECT?", False, True)
        yesButton.show()
        noButton.show()
    
def yesPress():
    global scoreYellow
    global scoreRed
    print("yes")
    if (state == State.PROPOSING_YELLOW):
        scoreYellow += 1
    else:
        scoreRed += 1
    goToReady()
    
def noPress():
    goToReady()

pg.init()
screen = createScreen()

startButton = displayStartButton(screen, lambda: goToPlaying())
yesButton = displayYesButton(screen, lambda: yesPress())
noButton = displayNoButton(screen, lambda: noPress())

goToReady()

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
    
    if (not startButton._hidden):
        startButton.listen(events)
        startButton.draw()

    if (not yesButton._hidden):
        yesButton.listen(events)
        yesButton.draw()

    if (not noButton._hidden):
        noButton.listen(events)
        noButton.draw()

    pg.display.update()

pg.quit()
