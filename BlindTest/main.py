import pygame as pg
import pygame_widgets as pw
from display import *
from enum import IntEnum
from jukebox import *
from time import sleep
from neopixel24 import *
import RPi.GPIO as GPIO

class State(IntEnum):
    READY = 1
    PLAYING = 2
    PROPOSING_RED = 3
    PROPOSING_YELLOW = 4
    
NEO_YELLOW = (255,255,0)
NEO_RED = (255,0,0)
state = State.READY
scoreYellow = 0
scoreRed = 0
startButton = None
yesButton = None
noButton = None
skipButton = None
incYellowButton = None
decYellowButton = None
incRedButton = None
decRedButton = None
jukebox = None
newMusic = True
neopixel = NeoPixel24()
PinRed = 5
PinYellow = 6

def goToReady():
    global state
    global startButton
    global yesButton
    global skipButton
    global neopixel
    global NEO_YELLOW
    global NEO_RED
    state = State.READY
    startButton.show()
    yesButton.hide()
    noButton.hide()
    skipButton.hide()
    refreshScreen()
    neopixel.fillColors(NEO_YELLOW, NEO_RED)

def goToPlaying():
    global state
    global startButton
    global jukebox
    global newMusic
    global yesButton
    global noButton
    global skipButton
    if newMusic:
        jukebox.stop()
        jukebox.nextMusic()
        jukebox.play()
        newMusic = False
    else:
        jukebox.unpause()
        
    state = State.PLAYING
    startButton.hide()
    yesButton.hide()
    noButton.hide()
    skipButton.show()
    refreshScreen()
    
def yellowPress(channel):
    global state
    global yesButton
    global noButton
    global jukebox
    global neopixel
    global NEO_YELLOW
    global skipButton
    print("Yellow Press!")
    if (state == State.PLAYING):
        state = State.PROPOSING_YELLOW
        neopixel.fillColor(NEO_YELLOW)
        jukebox.pause()
        yesButton.show()
        noButton.show()
        skipButton.hide()
        refreshScreen()

def redPress(channel):
    global state
    global yesButton
    global noButton
    global jukebox
    global neopixel
    global NEO_RED
    global skipButton
    print("Red Press!")
    if (state == State.PLAYING):
        state = State.PROPOSING_RED
        neopixel.fillColor(NEO_RED)
        jukebox.pause()
        yesButton.show()
        noButton.show()
        skipButton.hide()
        refreshScreen()
    
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
    newMusic = True
    goToReady()
    
def noPress():
    global neopixel
    neopixel.fillColors(NEO_YELLOW, NEO_RED)
    goToPlaying()
    
def skipMusic():
    global neopixel
    global jukebox
    global newMusic
    neopixel.fillColors(NEO_YELLOW, NEO_RED)
    jukebox.pause()
    newMusic = True
    goToReady()
    
def incYellow():
    global scoreYellow
    scoreYellow += 1
    refreshScreen()
def decYellow():
    global scoreYellow
    scoreYellow -= 1
    refreshScreen()
def incRed():
    global scoreRed
    scoreRed += 1
    refreshScreen()
def decRed():
    global scoreRed
    scoreRed -= 1
    refreshScreen()
    
def refreshScreen():
    screen.fill(GREY)
    displayScore(screen, scoreYellow, scoreRed)
    displayMusicTitle(screen, jukebox.getTitle())
    if (state == State.PLAYING):
        displayCircle(screen, "PLAYING", True, True)
    elif (state == State.READY):
        displayCircle(screen, "READY?", True, True)
    elif (state == State.PROPOSING_RED):
        displayCircle(screen, "CORRECT?", False, True)
    elif (state == State.PROPOSING_YELLOW):
        displayCircle(screen, "CORRECT?", True, False)

GPIO.setmode(GPIO.BCM)
GPIO.setup(PinYellow, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(PinRed, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(PinYellow, GPIO.RISING, callback=yellowPress, bouncetime=300)
GPIO.add_event_detect(PinRed, GPIO.RISING, callback=redPress, bouncetime=300)

pg.init()

screen = createScreen()
jukebox = Jukebox()

startButton = displayStartButton(screen, lambda: goToPlaying())
yesButton = displayYesButton(screen, lambda: yesPress())
noButton = displayNoButton(screen, lambda: noPress())
incYellowButton = displayIncYellowButton(screen, lambda: incYellow())
decYellowButton = displayDecYellowButton(screen, lambda: decYellow())
incRedButton = displayIncRedButton(screen, lambda: incRed())
decRedButton = displayDecRedButton(screen, lambda: decRed())
skipButton = createSkipButton(screen, lambda: skipMusic())

goToReady()

running = True
neocounter = 0
while running:
    events = pg.event.get()
    for event in events:
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.KEYDOWN:
            if (event.unicode == 'y'):
                yellowPress(None)
            elif (event.unicode == 'r'):
                redPress(None)
    
    if (not startButton._hidden):
        startButton.listen(events)
        startButton.draw()

    if (not yesButton._hidden):
        yesButton.listen(events)
        yesButton.draw()

    if (not noButton._hidden):
        noButton.listen(events)
        noButton.draw()
        
    if (not skipButton._hidden):
        skipButton.listen(events)
        skipButton.draw()
        
    incYellowButton.draw()
    incYellowButton.listen(events)
    decYellowButton.draw()
    decYellowButton.listen(events)
    incRedButton.draw()
    incRedButton.listen(events)
    decRedButton.draw()
    decRedButton.listen(events)
        
    neocounter += 1
    if (neocounter > 50):
        if (state == State.PLAYING):
            neocounter = 0
            neopixel.rotate()

    pg.display.update()
    simulateNeoPixel(screen, neopixel)

neopixel.fillColor((0,0,0))
GPIO.cleanup()
pg.quit()
