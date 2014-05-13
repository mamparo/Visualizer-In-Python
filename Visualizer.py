#Visualizer help from 'courageousillumination'
#https://github.com/courageousillumination/visualizer/blob/master/visualizer.py#L36
import pygame as pgame
import numpy as np
import time
import wave 
import array
from random import randint

pgame.mixer.init() #initalizes the mixer element
pgame.init() #initalizes the game screen
lowest = 90000
highest = 0

def pickMusic():
    music = str(raw_input('Enter the name of the song: '))
    return music

def framework(string):
    #loads the music into pygame
    pgame.mixer.music.load(string + '.wav')
    sound_file = wave.open(string + '.wav')
    data = sound_file.readframes(44100*10) #takes the first 10 seconds of the song
    
    print sound_file.getparams()
    stringOfBytes = np.fromstring(data, '<H')
    #'<H' = little endian unsigned short
    #needed to grab the data from the sound

    return stringOfBytes

def highestRange(highest, stringOfBytes):
    #reads into the string of bytes and gathers the highest and lowest elements
    for i in range(0, len(stringOfBytes), 882):
        if (stringOfBytes[i] > highest):
            highest = stringOfBytes[i]
    return highest

def lowestRange(lowest, stringOfBytes):
    #reads into the string of bytes and gathers the highest and lowest elements
    for i in range(0, len(stringOfBytes), 882):
        if (stringOfBytes[i] < lowest):
            lowest = stringOfBytes[i]
    return lowest

def barsVisualizer(highest, lowest, stringOfBytes):
    #separates the sample ranges into sections
    rangeOf = highest - lowest
    divisionOf = rangeOf/6
    first = 0
    second = divisionOf + first
    third = second + divisionOf
    fourth = third + divisionOf
    fifth = fourth + divisionOf
    sixth = fifth + divisionOf
    print first, second, third, fourth, fifth, sixth
    
    screen = pgame.display.set_mode([640,480])
    WHITE = (255, 255, 255)
    black = (0,0,0)
    done = False
    tick = time.time()
    arrayStep = 0
    pgame.display.init()#initializes the display element
    pgame.display.set_caption("Visualizer")
    screen.fill(WHITE)
    pgame.mixer.music.play()
    while not done:
        randomNumber = randint(0,4)
        screen.fill(WHITE)
        for event in pgame.event.get():
            if event.type == pgame.QUIT:
                done = True
        if stringOfBytes[arrayStep] <= first:
            pgame.draw.aaline(screen, black, [20, 240], [620, 240], True)
            if(randomNumber == 0):
                pgame.draw.rect(screen, black, [30,240,20,0])
                pgame.draw.rect(screen, black, [60,240,20,0])
                pgame.draw.rect(screen, black, [90,240,20,0])
                pgame.draw.rect(screen, black, [120,240,20,0])
            elif(randomNumber == 1):
                pgame.draw.rect(screen, black, [150,240,20,0])
                pgame.draw.rect(screen, black, [180,240,20,0])
                pgame.draw.rect(screen, black, [210,240,20,0])
                pgame.draw.rect(screen, black, [240,240,20,0])
            elif(randomNumber == 2):
                pgame.draw.rect(screen, black, [270,240,20,0])
                pgame.draw.rect(screen, black, [300,240,20,0])
                pgame.draw.rect(screen, black, [330,240,20,0])
                pgame.draw.rect(screen, black, [360,240,20,0])
            elif(randomNumber == 3):
                pgame.draw.rect(screen, black, [390,240,20,0])
                pgame.draw.rect(screen, black, [420,240,20,0])
                pgame.draw.rect(screen, black, [450,240,20,0])
                pgame.draw.rect(screen, black, [480,240,20,0])
            else:
                pgame.draw.rect(screen, black, [510,240,20,0])
                pgame.draw.rect(screen, black, [540,240,20,0])
                pgame.draw.rect(screen, black, [570,240,20,0])
                pgame.draw.rect(screen, black, [600,240,20,0]) 
        elif first < stringOfBytes[arrayStep] <= second:
            pgame.draw.aaline(screen, black, [20, 240], [620, 240], True)
            if(randomNumber == 0):
                pgame.draw.rect(screen, black, [30,240,20,0])
                pgame.draw.rect(screen, black, [60,240,20,20])
                pgame.draw.rect(screen, black, [90,240,20,20])
                pgame.draw.rect(screen, black, [120,240,20,0])
            elif(randomNumber == 1):
                pgame.draw.rect(screen, black, [150,240,20,0])
                pgame.draw.rect(screen, black, [180,240,20,20])
                pgame.draw.rect(screen, black, [210,240,20,20])
                pgame.draw.rect(screen, black, [240,240,20,0])
            elif(randomNumber == 2):
                pgame.draw.rect(screen, black, [270,240,20,0])
                pgame.draw.rect(screen, black, [300,240,20,20])
                pgame.draw.rect(screen, black, [330,240,20,20])
                pgame.draw.rect(screen, black, [360,240,20,0])
            elif(randomNumber == 3):
                pgame.draw.rect(screen, black, [390,240,20,0])
                pgame.draw.rect(screen, black, [420,240,20,20])
                pgame.draw.rect(screen, black, [450,240,20,20])
                pgame.draw.rect(screen, black, [480,240,20,0])
            else:
                pgame.draw.rect(screen, black, [510,240,20,0])
                pgame.draw.rect(screen, black, [540,240,20,20])
                pgame.draw.rect(screen, black, [570,240,20,20])
                pgame.draw.rect(screen, black, [600,240,20,0]) 
        elif second < stringOfBytes[arrayStep] <= third:
            pgame.draw.aaline(screen, black, [20, 240], [620, 240], True)
            if(randomNumber == 0):
                pgame.draw.rect(screen, black, [30,240,20,20])
                pgame.draw.rect(screen, black, [60,240,20,50])
                pgame.draw.rect(screen, black, [90,240,20,50])
                pgame.draw.rect(screen, black, [120,240,20,20])
            elif(randomNumber == 1):
                pgame.draw.rect(screen, black, [150,240,20,20])
                pgame.draw.rect(screen, black, [180,240,20,50])
                pgame.draw.rect(screen, black, [210,240,20,50])
                pgame.draw.rect(screen, black, [240,240,20,20])
            elif(randomNumber == 2):
                pgame.draw.rect(screen, black, [270,240,20,20])
                pgame.draw.rect(screen, black, [300,240,20,50])
                pgame.draw.rect(screen, black, [330,240,20,50])
                pgame.draw.rect(screen, black, [360,240,20,20])
            elif(randomNumber == 3):
                pgame.draw.rect(screen, black, [390,240,20,20])
                pgame.draw.rect(screen, black, [420,240,20,50])
                pgame.draw.rect(screen, black, [450,240,20,50])
                pgame.draw.rect(screen, black, [480,240,20,20])
            else:
                pgame.draw.rect(screen, black, [510,240,20,20])
                pgame.draw.rect(screen, black, [540,240,20,50])
                pgame.draw.rect(screen, black, [570,240,20,50])
                pgame.draw.rect(screen, black, [600,240,20,20]) 
        elif third < stringOfBytes[arrayStep] <= fourth:
            pgame.draw.aaline(screen, black, [20, 240], [620, 240], True)
            if(randomNumber == 0):
                pgame.draw.rect(screen, black, [30,240,20,50])
                pgame.draw.rect(screen, black, [60,240,20,100])
                pgame.draw.rect(screen, black, [90,240,20,100])
                pgame.draw.rect(screen, black, [120,240,20,50])
            elif(randomNumber == 1):
                pgame.draw.rect(screen, black, [150,240,20,50])
                pgame.draw.rect(screen, black, [180,240,20,100])
                pgame.draw.rect(screen, black, [210,240,20,100])
                pgame.draw.rect(screen, black, [240,240,20,50])
            elif(randomNumber == 2):
                pgame.draw.rect(screen, black, [270,240,20,50])
                pgame.draw.rect(screen, black, [300,240,20,100])
                pgame.draw.rect(screen, black, [330,240,20,100])
                pgame.draw.rect(screen, black, [360,240,20,50])
            elif(randomNumber == 3):
                pgame.draw.rect(screen, black, [390,240,20,50])
                pgame.draw.rect(screen, black, [420,240,20,100])
                pgame.draw.rect(screen, black, [450,240,20,100])
                pgame.draw.rect(screen, black, [480,240,20,50])
            else:
                pgame.draw.rect(screen, black, [510,240,20,50])
                pgame.draw.rect(screen, black, [540,240,20,100])
                pgame.draw.rect(screen, black, [570,240,20,100])
                pgame.draw.rect(screen, black, [600,240,20,50]) 
        elif fourth < stringOfBytes[arrayStep] <= fifth:
            pgame.draw.aaline(screen, black, [20, 240], [620, 240], True)
            if(randomNumber == 0):
                pgame.draw.rect(screen, black, [30,240,20,0])
                pgame.draw.rect(screen, black, [60,240,20,-20])
                pgame.draw.rect(screen, black, [90,240,20,-20])
                pgame.draw.rect(screen, black, [120,240,20,0])
            elif(randomNumber == 1):
                pgame.draw.rect(screen, black, [150,240,20,0])
                pgame.draw.rect(screen, black, [180,240,20,-20])
                pgame.draw.rect(screen, black, [210,240,20,-20])
                pgame.draw.rect(screen, black, [240,240,20,0])
            elif(randomNumber == 2):
                pgame.draw.rect(screen, black, [270,240,20,0])
                pgame.draw.rect(screen, black, [300,240,20,-20])
                pgame.draw.rect(screen, black, [330,240,20,-20])
                pgame.draw.rect(screen, black, [360,240,20,0])
            elif(randomNumber == 3):
                pgame.draw.rect(screen, black, [390,240,20,0])
                pgame.draw.rect(screen, black, [420,240,20,-20])
                pgame.draw.rect(screen, black, [450,240,20,-20])
                pgame.draw.rect(screen, black, [480,240,20,0])
            else:
                pgame.draw.rect(screen, black, [510,240,20,0])
                pgame.draw.rect(screen, black, [540,240,20,-20])
                pgame.draw.rect(screen, black, [570,240,20,-20])
                pgame.draw.rect(screen, black, [600,240,20,0])
        elif fifth < stringOfBytes[arrayStep] <= sixth:
            pgame.draw.aaline(screen, black, [20, 240], [620, 240], True)
            if(randomNumber == 0):
                pgame.draw.rect(screen, black, [30,240,20,-20])
                pgame.draw.rect(screen, black, [60,240,20,-50])
                pgame.draw.rect(screen, black, [90,240,20,-50])
                pgame.draw.rect(screen, black, [120,240,20,-20])
            elif(randomNumber == 1):
                pgame.draw.rect(screen, black, [150,240,20,-20])
                pgame.draw.rect(screen, black, [180,240,20,-50])
                pgame.draw.rect(screen, black, [210,240,20,-50])
                pgame.draw.rect(screen, black, [240,240,20,-20])
            elif(randomNumber == 2):
                pgame.draw.rect(screen, black, [270,240,20,-20])
                pgame.draw.rect(screen, black, [300,240,20,-50])
                pgame.draw.rect(screen, black, [330,240,20,-50])
                pgame.draw.rect(screen, black, [360,240,20,-20])
            elif(randomNumber == 3):
                pgame.draw.rect(screen, black, [390,240,20,-20])
                pgame.draw.rect(screen, black, [420,240,20,-50])
                pgame.draw.rect(screen, black, [450,240,20,-50])
                pgame.draw.rect(screen, black, [480,240,20,-20])
            else:
                pgame.draw.rect(screen, black, [510,240,20,-20])
                pgame.draw.rect(screen, black, [540,240,20,-50])
                pgame.draw.rect(screen, black, [570,240,20,-50])
                pgame.draw.rect(screen, black, [600,240,20,-20])
        else:
            pgame.draw.aaline(screen, black, [20, 240], [620, 240], True)
            if(randomNumber == 0):
                pgame.draw.rect(screen, black, [30,240,20,-50])
                pgame.draw.rect(screen, black, [60,240,20,-100])
                pgame.draw.rect(screen, black, [90,240,20,-100])
                pgame.draw.rect(screen, black, [120,240,20,-50])
            elif(randomNumber == 1):
                pgame.draw.rect(screen, black, [150,240,20,-50])
                pgame.draw.rect(screen, black, [180,240,20,-100])
                pgame.draw.rect(screen, black, [210,240,20,-100])
                pgame.draw.rect(screen, black, [240,240,20,-50])
            elif(randomNumber == 2):
                pgame.draw.rect(screen, black, [270,240,20,-50])
                pgame.draw.rect(screen, black, [300,240,20,-100])
                pgame.draw.rect(screen, black, [330,240,20,-100])
                pgame.draw.rect(screen, black, [360,240,20,-50])
            elif(randomNumber == 3):
                pgame.draw.rect(screen, black, [390,240,20,-50])
                pgame.draw.rect(screen, black, [420,240,20,-100])
                pgame.draw.rect(screen, black, [450,240,20,-100])
                pgame.draw.rect(screen, black, [480,240,20,-50])
            else:
                pgame.draw.rect(screen, black, [510,240,20,-50])
                pgame.draw.rect(screen, black, [540,240,20,-100])
                pgame.draw.rect(screen, black, [570,240,20,-100])
                pgame.draw.rect(screen, black, [600,240,20,-50])
        pgame.display.update()
        time.sleep(0.05)
        arrayStep += 1

    pgame.display.quit()#exits the display
    pgame.quit() #exits the module

def colorVisualizer(highest, lowest, stringOfBytes):
    #separates the sample ranges into sections
    rangeOf = highest - lowest
    divisionOf = rangeOf/6
    first = 0
    second = divisionOf + first
    third = second + divisionOf
    fourth = third + divisionOf
    fifth = fourth + divisionOf
    sixth = fifth + divisionOf
    print first, second, third, fourth, fifth, sixth
    
    screen = pgame.display.set_mode([640,480])
    pgame.display.init()#initializes the display element
    pgame.display.set_caption("Visualizer")
    screen.fill(WHITE)
    pgame.mixer.music.play()

    for i in range(0, len(stringOfBytes), 882):
        screen.fill(WHITE)
        if stringOfBytes[i] <= first:
            pgame.draw.circle(screen, (255, 255, 255), (320,240), 100)
        elif first < stringOfBytes[i] <= second:
            pgame.draw.circle(screen, (220, 220, 20), (320,240), 110)
        elif second < stringOfBytes[i] <= third:
            pgame.draw.circle(screen, (190, 90, 190), (320,240), 120)
        elif third < stringOfBytes[i] <= fourth:
            pgame.draw.circle(screen, (250, 150, 150), (320,240), 130)
        elif fourth < stringOfBytes[i] <= fifth:
            pgame.draw.circle(screen, (120, 200, 120), (320,240), 140)
        elif fifth < stringOfBytes[i] <= sixth:
            pgame.draw.circle(screen, (90, 90, 210), (320,240), 150)
        else:
            pgame.draw.circle(screen, (240, 50, 50), (320,240), 160)
        pgame.display.update()
        time.sleep(0.02)

    pgame.display.quit()#exits the display
    pgame.quit() #exits the module


def main():
    music = pickMusic()
    stringBytes = framework(music)
    highRange = highestRange(highest, stringBytes)
    lowRange = lowestRange(lowest, stringBytes)
    colorVisualizer(highRange, lowRange, stringBytes)
    #barsVisualizer(highRange, lowRange, stringBytes)


    
