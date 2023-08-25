import tkinter
import random
import os
from PIL import ImageTk, Image
BOOTL = tkinter.Tk()
BOOTL.state("zoomed")
BOOTL.configure(bg="#093689")
def destroy(root):
    root.destroy()
    call(1)
class innerOperator:
    def innerCall(rootsan: tkinter.Tk):
        rootsan.destroy()
        root = tkinter.Tk()
        root.state("zoomed")
        img = tkinter.PhotoImage(file=r"BGdefault.png")
        img2 = tkinter.PhotoImage(file=r"file-add-line.png")
        panel = tkinter.Label(root, image = img).pack(fill="both", expand="yes")
        addfile = tkinter.Button(image=img2).place(x=10, y=10)
        root.mainloop()
def call(page):
    if page == 1:
        ARE = tkinter.Tk()
        ARE.configure(bg="#093689")
        ARE.state("zoomed")
        tkinter.Label(text="Are you sure?", font=("Arial", 45), bg="#093689", fg="white").place(x=30, y=30)
        tkinter.Button(text="Yes", bg="#093689", fg="white", font=("Arial", 50), command=lambda: innerOperator.innerCall(ARE)).place(x=10, y=150)
        tkinter.Button(text="No", bg="#093689", fg="white", font=("Arial", 50), command=lambda: ARE.destroy()).place(x=500, y=150)
tkinter.Button(text="LINUX_DG_1", bg="#093689", fg="white", font=("Arial", 50), command=lambda: destroy(BOOTL)).place(x=10, y=10)
q = tkinter.Button(text="LINUX_DG_2", bg="#093689", fg="white", font=("Arial", 50), command=lambda: os.startfile("error.vbs")).place(x=10, y=150)
a = tkinter.Button(text="LINUX_DG_3", bg="#093689", fg="white", font=("Arial", 50), command=lambda: os.startfile("error.vbs")).place(x=10, y=300)
r = tkinter.Button(text="LINUX_DG_4", bg="#093689", fg="white", font=("Arial", 50), command=lambda: os.startfile("error.vbs")).place(x=10, y=460)
l = tkinter.Button(text="LINUX_DG_5", bg="#093689", fg="white", font=("Arial", 50), command=lambda: os.startfile("error.vbs")).place(x=10, y=650)
tkinter.Label(text='''Intelligente
DataGarm''', font=("Arial", 50), bg="#093689", fg="white").place(x=1200, y=10)
BOOTL.mainloop()