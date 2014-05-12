#Visualizer help from 'courageousillumination'
#https://github.com/courageousillumination/visualizer/blob/master/visualizer.py#L36
import pygame as pgame
import numpy as np
import time
import wave 
import array

pgame.mixer.init() #initalizes the mixer element
pgame.init() #initalizes the game screen

#loads the music into pygame
pgame.mixer.music.load('ArchieCutMono.wav')
sound_file = wave.open('ArchieCutMono.wav')
data = sound_file.readframes(44100*15) #takes the first 15 seconds of the song


print sound_file.getparams()
stringOfBytes = np.fromstring(data, '<H')
#'<H' = little endian unsigned short
#needed to grab the data from the sound

lowest = 90000
highest = 0

#reads into the string of bytes and gathers the highest and lowest elements
for i in range(0, len(stringOfBytes), 882):
    print stringOfBytes[i]
    if (stringOfBytes[i] > highest):
        high = stringOfBytes[i]
    if (stringOfBytes[i] < lowest):
        low = stringOfBytes[i]


print 'done'

print low
print high
i=0

#separates the sample ranges into sections
rangeOf = high - low
divisionOf = rangeOf/6
first = 0
second = divisionOf + first
third = second + divisionOf
fourth = third + divisionOf
fifth = fourth + divisionOf
sixth = fifth + divisionOf


print first, second, third, fourth, fifth, sixth

for i in range(0, len(stringOfBytes), 882):

    if stringOfBytes[i] <= first:
        print '0 or less'

    elif first < stringOfBytes[i] <= second:
        print 'first'

    elif second < stringOfBytes[i] <= third:
        print 'second'

    elif third < stringOfBytes[i] <= fourth:
        print 'third'

    elif fourth < stringOfBytes[i] <= fifth:
        print 'fourth'

    elif fifth < stringOfBytes[i] <= sixth:
        print 'fifth'
    else:
        print 'sixth'



print first, second, third, fourth, fifth, sixth

pgame.display.init()#initializes the display element
screen = pgame.display.set_mode([640,480])
pgame.display.set_caption("Visualizer")
WHITE = (255, 255, 255)
black = (0,0,0)
screen.fill(WHITE)
done = False
tick = time.time()
arrayStep = 0
while not done:
    #draws the bars
    pgame.draw.rect(screen, black, [30,240,150,0])
                                   #x,y,width,height
    pgame.draw.rect(screen, black, [180,240,150,0])
    pgame.draw.rect(screen, black, [330,240,150,0])
    screen.fill(WHITE)
    for event in pgame.event.get():
        if event.type == pgame.QUIT:
            done = True
    pgame.draw.aaline(screen, black, [20, 240], [620, 240], True)
    if stringOfBytes[arrayStep] <= first:
        pgame.draw.rect(screen, black, [30,240,150,0])
        pgame.draw.rect(screen, black, [180,240,150,0])
        pgame.draw.rect(screen, black, [330,240,150,0])
    elif first < stringOfBytes[arrayStep] <= second:
        pgame.draw.rect(screen, black, [30,240,150,0])
        pgame.draw.rect(screen, black, [180,240,150,10])
        pgame.draw.rect(screen, black, [330,240,150,0])
    elif second < stringOfBytes[arrayStep] <= third:
        pgame.draw.rect(screen, black, [30,240,150,50])
        pgame.draw.rect(screen, black, [180,240,150,100])
        pgame.draw.rect(screen, black, [330,240,150,50])
    elif third < stringOfBytes[arrayStep] <= fourth:
        pgame.draw.rect(screen, black, [30,240,150,75])
        pgame.draw.rect(screen, black, [180,240,150,200])
        pgame.draw.rect(screen, black, [330,240,150,75])
    elif fourth < stringOfBytes[arrayStep] <= fifth:
        pgame.draw.rect(screen, black, [30,240,150,0])
        pgame.draw.rect(screen, black, [180,240,150,-10])
        pgame.draw.rect(screen, black, [330,240,150,0])
    elif fifth < stringOfBytes[arrayStep] <= sixth:
        pgame.draw.rect(screen, black, [30,240,150,-50])
        pgame.draw.rect(screen, black, [180,240,150,-100])
        pgame.draw.rect(screen, black, [330,240,150,-50])
    else:
        pgame.draw.rect(screen, black, [30,240,150,-75])
        pgame.draw.rect(screen, black, [180,240,150,-200])
        pgame.draw.rect(screen, black, [330,240,150,-75])
    pgame.display.update()
    time.sleep(0.02)
    arrayStep += 1



pgame.display.quit()#exits the display
pgame.quit() #exits the module
