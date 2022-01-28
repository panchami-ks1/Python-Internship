from tkinter import *
window=Tk()
window.geometry('1000x1000')

btn_column=Button(window,text='click me')
btn_column.grid(column=0)
btn_column1=Button(window,text='click me')
btn_column1.grid(column=1)
btn_column2=Button(window,text='click me')
btn_column2.grid(column=2,sticky=S)

window.mainloop()