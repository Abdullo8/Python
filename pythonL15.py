from tkinter import *

top = Tk()
top.title("My password experiment")
top.geometry("400x300")
top.configure(background="grey")
# name _____________
user_name = Label(top, text="Name").place(x=60, y=80)
# pasword__________________
user_password = Label(top, text="Password").place(x=60, y=110)
# | button |
Button(top, text="Submit").place(x=60, y=150)

user_name_input_area = Entry(top).place(x=100, y=80)
user_password_input_area = Entry(top).place(x=120, y=110)

top.mainloop()