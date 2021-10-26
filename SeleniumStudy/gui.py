from tkinter import *
from tkinter import messagebox

def Callhello():

   msg = messagebox.showinfo( "Hello Appia","Welcome, please click ad")

root = Tk()

lbl = Label(root, text="이름")
lbl.pack()

txt = Entry(root)
txt.pack()

btn = Button(root, text="OK", command = Callhello)
btn.pack()

root.mainloop()