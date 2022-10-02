import tkinter as tk
from PIL import ImageTk

class Reminder(tk.Canvas):
    def __init__(self, master, name, description, **kw):
        super().__init__(master=master, **kw)
        self.pack(expand=True, fill='both')

