#!/usr/bin/env python3

# this will import everything from tkinter 
# and tkk modulers
# from widgets to modules

from tkinter import *
from tkinter.ttk import *

master = Tk()

#setting up the window
width = "1000"
height = "500"

master.geometry(f'{width}x{height}')
master.title("Algorythm")
master.resizable(False, False)

#creating a button + function

def DisplayText():
    text = Label(master, text="Welcome!")
    text.place(x=50, y=50)

btn = Button(master, text="Click Me!", command=DisplayText)

btn.pack(pady=20)

#the main loop
master.mainloop()
