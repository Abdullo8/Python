import requests                # pip3 install requests
import tkinter as tk
from tkinter import Text, END 
from tkinter.ttk import Button

root = tk.Tk()
root.title('Elders speak')


def get_quote():
    r = requests.get("https://api.quotable.io/random")
    data = r.json()
    quote = data['content']
    author = data['author']

    all = quote + author

    text_box.delete(1.0, END)
    text_box.insert(END, all)

text_box = Text(root, width=100, height=20)
get_button = Button(root, text="Get New- Qoute", command=get_quote)

text_box.pack()
get_button.pack()

root.mainloop()