import pygame
import os
import random

MUSIC_FOLDER = "/home/pi/Music/"

class Jukebox:
    currentMusic = None
    allMusics = []
    isPaused = False
    
    def __init__(self):
        pygame.mixer.init()
        pygame.mixer.music.set_volume(1.0)
    
    def findAllMusics(self):
        self.allMusics = []
        listdir = os.listdir(MUSIC_FOLDER)
        for name in listdir:
            if name.endswith(".mp3"):
                self.allMusics.append(name)
        
    def nextMusic(self):
        if len(self.allMusics) == 0:
            self.findAllMusics()
        if (self.currentMusic != None):
            pygame.mixer.music.unload()
        size = len(self.allMusics)
        index = random.randint(0, size-1)
        self.currentMusic = self.allMusics[index]
        self.allMusics.remove(self.currentMusic)
        print('Selected Music: "' + self.currentMusic + '", Remaining:', str(size - 1))
        pygame.mixer.music.load(MUSIC_FOLDER + self.currentMusic)

    def stop(self):
        pygame.mixer.music.stop()
        
    def play(self):
        pygame.mixer.music.play()

    def pause(self):
        self.isPaused = True
        pygame.mixer.music.pause()

    def unpause(self):
        if self.isPaused:
            pygame.mixer.music.unpause()
            self.isPaused = False
        else:
            self.play()

    def isPlaying(self):
        return pygame.mixer.music.get_busy()

    def getTitle(self):
        if self.currentMusic != None:
            return self.currentMusic[0:len(self.currentMusic) - 4]
        else:
            return ""
        