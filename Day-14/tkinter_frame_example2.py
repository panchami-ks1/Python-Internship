from tkinter import *
window=Tk()
window.geometry('500x500')
label1=Label(window,text='Main window')
label1.pack()

frame=Frame(window)
frame.pack()
bottom_frame=Frame(window)
bottom_frame.pack(side=BOTTOM)

red_button=Button(frame,text='Red',fg='red')
red_button.pack(side=LEFT)
blue_button=Button(frame,text='Blue',fg='blue')
blue_button.pack(side=LEFT)
green_button=Button(frame,text='Green',fg='green')
green_button.pack(side=LEFT)

red_button=Button(bottom_frame,text='Red',fg='red')
red_button.pack(side=BOTTOM)
blue_button=Button(bottom_frame,text='Blue',fg='blue')
blue_button.pack(side=BOTTOM)
green_button=Button(bottom_frame,text='Green',fg='green')
green_button.pack(side=BOTTOM)

window.mainloop()

