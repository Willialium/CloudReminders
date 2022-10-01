import tkinter as tk
from tkinter import filedialog, Text
import os

from random import randint

root = tk.Tk()

def randomColor():
    print("Print")

canvas = tk.Canvas(root, height=300, width=400, bg='#263D42')
canvas.pack()

num = tk.IntVar()

c = tk.Checkbutton(root, variable=num, onvalue=1, offvalue=0)
c.pack()

root.mainloop()
