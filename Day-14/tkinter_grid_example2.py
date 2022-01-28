from tkinter import*

window=Tk()
window.title('My GUI Window')
window.geometry('500x500')

label1=Label(window,text='First')
label1.grid(row=0,column=0,sticky=W,pady=2)
label2=Label(window,text='Second')
label2.grid(row=1,column=0,sticky=W,pady=2)

e1=Entry(window)
e2=Entry(window)
e1.grid(row=0,column=1,pady=2)
e2.grid(row=1,column=1,pady=2)

c1=Checkbutton(window,text='Agree')
c1.grid(row=2,column=0,sticky=W,columnspan=2)
# button widget
b1 = Button(window, text="Zoom in")
b2 = Button(window, text="Zoom out")

# arranging button widgets
b1.grid(row=3, column=2, sticky=N)
b2.grid(row=3, column=3, sticky=E)

window.mainloop()