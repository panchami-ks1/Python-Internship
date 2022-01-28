from tkinter import *

# import tkinter.messagebox
# from tkMessageBox import *
import callback as callback

window = Tk()
window.title('My GUI window')
window.geometry('500x500')


def callback():
    label1.config(text='Button clicked')


label1 = Label(window, text='Hello', background='yellow',width=5, height=10)
label1.pack()
label2 = Label(window, text='Hello', background='yellow', fg='green')
label2.pack(fill=BOTH, expand=True)
button1 = Button(window, text='Click me', background='blue', fg='red', command=callback)
button1.pack(ipadx=10, ipady=10, expand=True)

window.mainloop()
