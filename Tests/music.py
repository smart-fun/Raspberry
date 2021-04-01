import pygame
from time import sleep
import os
import random

MUSIC_FOLDER = "/home/pi/Downloads/"

listdir = os.listdir(MUSIC_FOLDER)
#print(listdir)
mp3s=[]
for name in listdir:
    if name.endswith(".mp3"):
        print(name)
        mp3s.append(name)

size = len(mp3s)
print("size:", size)
index = random.randint(0, size-1)
mp3 = mp3s[index]
print("Playing" , mp3)

pygame.mixer.init()
pygame.mixer.music.load(MUSIC_FOLDER + mp3)
pygame.mixer.music.set_volume(1.0)

pygame.mixer.music.play()

while pygame.mixer.music.get_busy() == True:
    pass

'''    sleep(0.1)
    pygame.mixer.music.pause()
    sleep(0.1)
    pygame.mixer.music.unpause()
'''