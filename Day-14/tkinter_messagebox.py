from tkinter import *
from tkinter import messagebox
window=Tk()
window.title('My GUI window')
window.geometry('500x500')


messagebox.showinfo("", "Information")

messagebox.showwarning("showwarning", "Warning")

messagebox.showerror("showerror", "Error")

messagebox.askquestion("askquestion", "Are you sure?")

messagebox.askokcancel("askokcancel", "Want to continue?")

messagebox.askyesno("askyesno", "Find the value?")

messagebox.askretrycancel("askretrycancel", "Try again?")

window.mainloop()