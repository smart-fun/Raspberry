import pygame as pg
import pygame_widgets as pw

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

WHITE = (255,255,255)
YELLOW = (220,220,0)
RED = (220,0,0)
GREY = (180,180,180)
BLACK = (0,0,0)

BUTTON_COLOR = (0,0,220)
BUTTON_HOVER_COLOR = (0,200,0)
BUTTON_PRESS_COLOR = (0,100,0)

def createScreen():
    screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.fill(GREY)
    return screen

def displayCircle(screen, message):
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    radius = SCREEN_HEIGHT / 4
    pi = 3.14159
    pg.draw.circle(screen, RED, [x, y], radius, 0, draw_top_right=True, draw_bottom_right=True)
    pg.draw.circle(screen, YELLOW, [x, y], radius, 0, draw_top_left=True , draw_bottom_left=True)
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