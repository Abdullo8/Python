# import tkinter as tk

# window = tk.Tk()
 
# label = tk.Label(text= "Python рулит!",
# bg="black", fg="white", width=20, height=20)

# label.pack() 
# window.mainloop()

# ________________________________________________________________________

# import tkinter as tk

# window = tk.Tk()
 
# button = tk.Button(
#     text="Нажми на меня!",
#     width=25,
#     height=5,
#     bg="black ",
#     fg="white"
# )

# button.pack() 
# window.mainloop()


import tkinter as tk

window = tk.Tk()
label = tk.Label(
    text="имя",
    width=5,
    height=3,
)
entry = tk.Entry()

label.pack()

entry.pack()

window.mainloop()