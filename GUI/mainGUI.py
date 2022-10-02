import tkinter as tk
from PIL import ImageTk, Image
from functools import partial
import Cloud.functions as cloud

reminders = []
checks = []

#########################
#### MAKE MAIN FRAME ####
#########################

root = tk.Tk()
frame = tk.Frame(root, borderwidth=0, highlightthickness=0)
nameCanvas = tk.Canvas(frame, bg='#800000', borderwidth=0, highlightthickness=0)
remCanvas = tk.Canvas(frame, bg='#800000', borderwidth=0, highlightthickness=0)
nameBG = ImageTk.PhotoImage(Image.open('name.png'))
remBG = ImageTk.PhotoImage(Image.open('reminder.png'))


def makeFrame():
    root.title('Reminder')
    root.geometry('312x400')

    frame.pack(fill='both', expand=1)


def showReminders(name):
    global reminders
    reminders = cloud.getReminders(name)
    nameCanvas.children.destroy()
    #makeRemCanvas()


def _on_mouse_wheel_name(event):
    nameCanvas.yview_scroll(-1 * int((event.delta / 120)), "units")


def _on_mouse_wheel_rem(event):
    nameCanvas.yview_scroll(-1 * int((event.delta / 120)), "units")


def makeNameCanvas():
    nameCanvas.pack(side='left', fill='both', expand=1)
    scrollbar = tk.Scrollbar(frame, orient='vertical', command=nameCanvas.yview)
    scrollbar.pack(side='right', fill='y')

    nameCanvas.configure(yscrollcommand=scrollbar.set)
    nameCanvas.bind('<Configure>', lambda e: nameCanvas.configure(scrollregion=nameCanvas.bbox('all')))

    nameCanvas.bind_all("<MouseWheel>", _on_mouse_wheel_name)

    names = [i for i in cloud.getNames()]
    for i in range(len(names)):
        nameCanvas.create_image(12, i * 90 + 8, image=nameBG, anchor='nw')
        checks.append(tk.IntVar())
        c = tk.Button(frame, text=names[i][0], bg='white', borderwidth=0, font=('Helvetica 15 bold'),
                      width=22, height=2, command=partial(showReminders, names[i][0]))
        nameCanvas.create_window(156, i * 90 + 20, anchor='n', window=c)


def makeRemCanvas():
    remCanvas.pack(side='left', fill='both', expand=1)
    scrollbar = tk.Scrollbar(frame, orient='vertical', command=remCanvas.yview)
    scrollbar.pack(side='right', fill='y')

    remCanvas.configure(yscrollcommand=scrollbar.set)
    remCanvas.bind('<Configure>', lambda e: remCanvas.configure(scrollregion=remCanvas.bbox('all')))

    remCanvas.bind_all("<MouseWheel>", _on_mouse_wheel_rem)

    for i in range(len(reminders)):
        remCanvas.create_image(12, i * 130 + 10, image=remBG, anchor='nw')
        checks.append(tk.IntVar())
        c = tk.Checkbutton(frame, text=reminders[i][0], bg='white', font=14, variable=checks[i], onvalue=1, offvalue=0)
        remCanvas.create_text(80, i * 130 + 50, text=reminders[i][1], font=9, width=180, anchor='nw')
        remCanvas.create_window(30, i * 130 + 20, anchor='nw', window=c)


################################
#### HANDLE CLOSE PROTOCOLS ####
################################

def checkAction(name):
    print(name)
    cloud.markRead(name)


def onClose():
    for i in range(len(reminders)):
        print(reminders[i][0], checks[i].get())
        if int(checks[i].get()):
            cloud.markRead(reminders[i][0])
    root.destroy()


makeFrame()
makeNameCanvas()
root.protocol("WM_DELETE_WINDOW", onClose)
root.mainloop()
