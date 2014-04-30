#Visualizer help from 'courageousillumination'
#https://github.com/courageousillumination/visualizer/blob/master/visualizer.py#L36
import pygame as pgame
import numpy as np
import wave 
import array

pgame.mixer.init() #initalizes the mixer element
pgame.init() #initalizes the game screen


pgame.mixer.music.load('ArchieCutMono.wav')
sound_file = wave.open('ArchieCutMono.wav')
data = sound_file.readframes(44100*15)


print sound_file.getparams()
stringOfBytes = np.fromstring(data, '<H')
#'<H' = little endian unsigned short
#needed to grab the data from the sound

lowest = 900000
highest = 0

for i in range(0, len(stringOfBytes), 882):
    print stringOfBytes[i/882]
    if lowest > stringOfBytes[i/882]:
        lowest = stringOfBytes[i/882]
    if highest < stringOfBytes[i/882]:
        highest = stringOfBytes[i/882]

print  "Lowest = ", lowest
print "Highest = ", highest
