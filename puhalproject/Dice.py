import tkinter as t
import random

screen = t.Tk()

def roll():
    val = random.randint(1, 6)
    numscreen['text'] = val


button = t.Button(master=screen, text='Roll', width='25', height='10', command=roll)
button.pack()
numscreen = t.Label(master=screen, text='0')
numscreen.pack()

screen.mainloop()