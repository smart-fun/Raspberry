import pygame as pg
import pygame_widgets as pw
from display import *
from enum import IntEnum
from jukebox import *
from time import sleep

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
jukebox = None
newMusic = True

def goToReady():
    global state
    global screen
    global startButton
    global yesButton
    global newMusic
    global jukebox
    state = State.READY
    screen.fill(GREY)
    displayCircle(screen, "READY?", True, True)
    startButton.show()
    yesButton.hide()
    noButton.hide()
    displayScore(screen, scoreYellow, scoreRed)
    title = jukebox.getTitle()
    displayMusicTitle(screen, title)

def goToPlaying():
    global state
    global screen
    global startButton
    global jukebox
    global newMusic
    global yesButton
    global newMusic
    if newMusic:
        jukebox.stop()
        jukebox.nextMusic()
        jukebox.play()
        newMusic = False
    else:
        jukebox.unpause()
        
    state = State.PLAYING
    print("New State", state)
    startButton.hide()
    yesButton.hide()
    noButton.hide()
    screen.fill(GREY)
    displayCircle(screen, "PLAYING", True, True)
    displayScore(screen, scoreYellow, scoreRed)
    title = jukebox.getTitle()
    displayMusicTitle(screen, title)
    
def yellowPress():
    global state
    global yesButton
    global noButton
    global jukebox
    print("Yellow Press!")
    if (state == State.PLAYING):
        state = State.PROPOSING_YELLOW
        jukebox.pause()
        displayCircle(screen, "CORRECT?", True, False)
        yesButton.show()
        noButton.show()

def redPress():
    global state
    global yesButton
    global noButton
    global jukebox
    print("Red Press!")
    if (state == State.PLAYING):
        state = State.PROPOSING_RED
        jukebox.pause()
        displayCircle(screen, "CORRECT?", False, True)
        yesButton.show()
        noButton.show()
    
def yesPress():
    global scoreYellow
    global scoreRed
    global jukeBox
    global newMusic
    print("yes")
    if (state == State.PROPOSING_YELLOW):
        scoreYellow += 1
    else:
        scoreRed += 1
    jukebox.unpause()
    newMusic = True
    goToReady()
    
def noPress():
    #goToReady()
    goToPlaying()

pg.init()

screen = createScreen()
jukebox = Jukebox()

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
