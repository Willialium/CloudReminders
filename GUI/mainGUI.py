import tkinter as tk
from PIL import ImageTk, Image
import pyodbc
import Cloud.functions as cloud


reminders = cloud.getReminders()

root = tk.Tk()
root.title('Reminder')
root.geometry('312x400')

frame = tk.Frame(root, borderwidth=0, highlightthickness=0)
frame.pack(fill='both',expand=1)

canvas = tk.Canvas(frame, bg='#800000', borderwidth=0, highlightthickness=0)
canvas.pack(side='left', fill='both', expand=1)
scrollbar = tk.Scrollbar(frame, orient='vertical', command=canvas.yview)
scrollbar.pack(side='right', fill='y')

canvas.configure(yscrollcommand=scrollbar.set)
canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion = canvas.bbox('all')))
def _on_mouse_wheel(event):
    canvas.yview_scroll(-1 * int((event.delta / 120)), "units")
canvas.bind_all("<MouseWheel>", _on_mouse_wheel)

def checkAction(name):
    cloud.markRead(name)

bg = ImageTk.PhotoImage(Image.open('reminder.png'))
for i in range(len(reminders)):
    canvas.create_image(12, i*130, image=bg, anchor='nw')
    c = tk.Checkbutton(frame, text=reminders[i][0], bg='white', font=14, command=lambda: checkAction(reminders[i][0]))
    canvas.create_text(80, i*130+45, text=reminders[i][1], font=9, width=180, anchor='nw')
    checkCanvas = canvas.create_window(30, i*130 + 20, anchor='nw', window=c)




#frontFrame = tk.Frame(canvas, bg='#800000', borderwidth=0, highlightthickness=0)
#canvas.create_window((0,0), window=frontFrame, anchor='nw')

#bg = ImageTk.PhotoImage(Image.open('reminder.png'))
#for i in range(10):
#    l = tk.Label(frontFrame, image=bg, borderwidth=0, highlightthickness=0).grid(row=i, column=0, pady=10, padx=12)
#    f = tk.Frame(frontFrame, bg='#009000',borderwidth=0).grid(row=i, column=0, pady=10, padx=12)
#    c = tk.Checkbutton(f, text='Check', bg='#FFFFFF', justify='left')



root.mainloop()


