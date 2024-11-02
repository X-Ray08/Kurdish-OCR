from tkinter import *
import tkinter as tk
from tkinter import filedialog
import scan
import Wordim
import os

top = tk.Tk()

top.title("Kurdish_OCR")

top.geometry("%dx%d+%d+%d" % (500, 500, 700, 200))
top.configure(background="#152238")

logo = PhotoImage("logo.ico")
top.wm_iconbitmap(logo)
im = PhotoImage('logo.png')

canvas = Canvas(top, width=300, height=300, bg="#152238", bd=0, relief='ridge', highlightthickness=0)
canvas.place(x=120)
img = PhotoImage(file="logo1.png")
canvas.create_image(20, 20, anchor=NW, image=img)

Label(text="Drop Your document", font="verdana 12", bg="#152238", fg="white").place(x=170, y=250)


def UploadAction():
    filename = filedialog.askopenfilename()
    print('Selected doc:', filename)
    base = os.path.basename(filename)
    print('Selected base:', base)
    scan.scandoc(base)


tk.Button(top, text='browse Document', command=UploadAction, font="verdana 12", background="white").place(
    x=173, y=280)

Label(text="Drop Your image", font="verdana 12", bg="#152238", fg="white").place(x=180, y=340)


def UploadAction():
    filename = filedialog.askopenfilename()
    print('Selected image:', filename)
    base = os.path.basename(filename)
    print('Selected base:', base)
    Wordim.imscn(base)


nrmlbutton = tk.Button(top, text='browse image', command=UploadAction, font="verdana 12", background="white")
nrmlbutton.place(x=185, y=370)

mainloop()
