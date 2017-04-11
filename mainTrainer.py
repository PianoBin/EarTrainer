from tkinter import *
from tkinter import ttk

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

