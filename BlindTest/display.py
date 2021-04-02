import pygame as pg
import pygame_widgets as pw

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

WHITE = (255,255,255)
YELLOW = (220,220,0)
RED = (220,0,0)
GREY = (180,180,180)
BLACK = (0,0,0)
GREEN = (0,200,0)

BUTTON_COLOR = (0,0,220)
BUTTON_HOVER_COLOR = GREEN
BUTTON_PRESS_COLOR = (0,100,0)

def createScreen():
    screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.fill(GREY)
    return screen

def displayCircle(screen, message, yellow, red):
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    radius = SCREEN_HEIGHT / 4
    pi = 3.14159
    if (yellow and red):
        pg.draw.circle(screen, RED, [x, y], radius, 0, draw_top_right=True, draw_bottom_right=True)
        pg.draw.circle(screen, YELLOW, [x, y], radius, 0, draw_top_left=True , draw_bottom_left=True)
    elif yellow:
        pg.draw.circle(screen, YELLOW, [x, y], radius, 0)
    elif red:
        pg.draw.circle(screen, RED, [x, y], radius, 0)
    font = pg.font.SysFont(None, 60)
    text = font.render(message, True, BLACK)
    textRect = text.get_rect()
    textRect.centerx = screen.get_rect().centerx
    textRect.centery = screen.get_rect().centery
    screen.blit(text,textRect)

def displayStartButton(screen, callback):
    width = 200
    height = 50
    x = (SCREEN_WIDTH - width) / 2
    y = SCREEN_HEIGHT * 0.8
    button = pw.Button(
        screen, x, y, width, height, text='START',
        fontSize=50,
        margin=10,
        textColour=(255,255,255),
        inactiveColour=BUTTON_COLOR,
        hoverColour=BUTTON_HOVER_COLOR,
        pressedColour=BUTTON_PRESS_COLOR,
        radius=10,
        onClick=callback
     )
    return button

def displayYesButton(screen, callback):
    width = 200
    height = 50
    x = (SCREEN_WIDTH * 0.45) - width
    y = SCREEN_HEIGHT * 0.8
    button = pw.Button(
        screen, x, y, width, height, text='YES',
        fontSize=50,
        margin=10,
        textColour=(255,255,255),
        inactiveColour=BUTTON_COLOR,
        hoverColour=BUTTON_HOVER_COLOR,
        pressedColour=BUTTON_PRESS_COLOR,
        radius=10,
        onClick=callback
     )
    return button

def displayNoButton(screen, callback):
    width = 200
    height = 50
    x = (SCREEN_WIDTH * 0.55)
    y = SCREEN_HEIGHT * 0.8
    button = pw.Button(
        screen, x, y, width, height, text='NO',
        fontSize=50,
        margin=10,
        textColour=(255,255,255),
        inactiveColour=BUTTON_COLOR,
        hoverColour=BUTTON_HOVER_COLOR,
        pressedColour=BUTTON_PRESS_COLOR,
        radius=10,
        onClick=callback
     )
    return button

def displayScore(screen, yellow, red):
    font = pg.font.SysFont(None, 100)
    
    text = font.render(str(yellow), True, YELLOW)
    textRect = text.get_rect()
    textRect.centerx = SCREEN_WIDTH * 0.17
    textRect.centery = screen.get_rect().centery
    screen.blit(text,textRect)
    
    text = font.render(str(red), True, RED)
    textRect = text.get_rect()
    textRect.centerx = SCREEN_WIDTH * (1 - 0.17)
    textRect.centery = screen.get_rect().centery
    screen.blit(text,textRect)

def displayMusicTitle(screen, title):
    font = pg.font.SysFont(None, 30)
    text = font.render(str(title), True, BLACK)
    textRect = text.get_rect()
    textRect.centerx = SCREEN_WIDTH * 0.5
    textRect.centery = SCREEN_HEIGHT * 0.1
    screen.blit(text,textRect)
    
