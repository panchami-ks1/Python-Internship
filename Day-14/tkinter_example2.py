
from tkinter import *
from tkinter import messagebox

win= Tk()
win.title("Button Command Example")
win.geometry("600x300")

#Defining a function
def func(args):
   messagebox.showinfo(" ",args)

#Create a button and pass arguments in command as a function name
my_button= Button(win, text= "Close",borderwidth=2, command= lambda : func('see this worked'))
my_button.pack(pady=20)

win.mainloop()