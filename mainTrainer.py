from tkinter import *
from tkinter import ttk
from pydub import AudioSegment

def unpackSounds(sounds): #open wav files
    soundList = sounds
    fileStem = "39148__jobro__piano-ff-0"
    fileEnd = ".wav"
    fileName = ""
    for i in range(1, 88):
        if i < 10:
            fileName = fileStem + "0" + i + fileEnd
        else:
            fileName = fileStem + i + fileEnd
        soundList.append(AudioSegment_from_wav(fileName))
    return soundList

root = Tk()
root.title("Ear Training")
s.theme_use('aqua')
mainframe = ttk.Frame(root, padding="3 3 12 12") #Frame widget
mainframe.grid(column = 0, row = 0, sticky = (N, W, E, S)) #orient
mainframe.columnconfigure(0, weight = 1) #if resized, fit
mainframe.rowconfigure(0, weight = 1) #if resized, fit

score = StringVar()
lives = StringVar()
bottomNote = StringVar()
topscore = StringVar()
lives = StringVar()
bottomNote = StringVar()
topNote = StringVar()

sounds = []
soundsFull = unpackSounds(sounds)
