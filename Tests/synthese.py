# Synthèse vocale
# see https://lab-allen.fr/ateliers/robot-roulant/synthese-vocale-sur-raspberry-pi/
# sudo apt-get install espeak-ng

from time import sleep
from espeakng import ESpeakNG

def sayYellowTeam():
    speaker.say("équipe jaune")
    sleep(2)

def sayRedTeam():
    speaker.say("équipe rouge")
    sleep(2)
    
def sayScore(yellow, red):
    if (yellow == red):
        text = str(yellow) + " partout"
        speaker.say(text)
    elif (yellow > red):
        text = str(yellow) + " a " + str(red) + " pour les jaunes"
        speaker.say(text)
    else:
        text = str(red) + " a " + str(yellow) + " pour les rouges"
        speaker.say(text)
    sleep(3)

def sayFound():
    speaker.say("bravo ! c'est la bonne réponse !")
    sleep(3)

def sayNotFound():
    speaker.say("et non !")
    sleep(2)

speaker = ESpeakNG(voice='fr')
#sayYellowTeam()
#sayRedTeam()
sayScore(3, 3)
sayFound()
sayScore(4, 5)
sayNotFound()
sayScore(6, 2)


#speaker.say("Salut les copains !", sync=True)
#speaker.pitch = 80
#speaker.speed = 200
#speaker.say("Bienvenue dans Blind Test !", sync=True)
#print(speaker.voices)

