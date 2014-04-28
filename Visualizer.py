#Visualizer help from 'courageousillumination'
#https://github.com/courageousillumination/visualizer/blob/master/visualizer.py#L36
import pygame as pgame
import numpy as np
import wave 
import array

pgame.mixer.init() #initalizes the mixer element
pgame.init() #initalizes the game screen


pgame.mixer.music.load('ArchieCut.wav')
sound_file = wave.open('ArchieCut.wav')
data = wave.readframes()


print sound_file.getparams()
stringOfBytes = np.fromstring(data, '<H')
#'<H' = little endian unsigned short
#needed to grab the data from the sound
