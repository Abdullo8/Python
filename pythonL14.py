from tkinter import *
from tkinter.ttk import *
from time import strftime

window = Tk()
window .title("My first Tkinter windows")

def showTime():
    string = strftime("%H:%M:%S: %p")
    clock.config(text=string)
    clock.after(1000, showTime)

clock = Label(window, font=("Showcard Gothic", 100),
background="white", foreground="grey")
clock.pack()

showTime()
mainloop()