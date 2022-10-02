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
canvas = tk.Canvas(frame, bg='#800000', borderwidth=0, highlightthickness=0)
nameBG = ImageTk.PhotoImage(Image.open('name.png'))
remBG = ImageTk.PhotoImage(Image.open('reminder.png'))
noCheck = ImageTk.PhotoImage(Image.open('CheckOff.png').resize((15,15)))
yesCheck = ImageTk.PhotoImage(Image.open('CheckOn.png').resize((15,15)))


def makeFrame():
    root.title('Reminder')
    root.geometry('312x400')

    frame.pack(fill='both', expand=1)


def showReminders(name):
    global reminders
    print(name)
    reminders = cloud.getReminders(name)
    canvas.delete('all')
    makeRemCanvas()


def _on_mouse_wheel_name(event):
    canvas.yview_scroll(-1 * int((event.delta / 120)), "units")


def _on_mouse_wheel_rem(event):
    canvas.yview_scroll(-1 * int((event.delta / 120)), "units")


def makeNameCanvas():
    canvas.pack(side='left', fill='both', expand=1)
    scrollbar = tk.Scrollbar(frame, orient='vertical', command=canvas.yview)
    scrollbar.pack(side='right', fill='y')

    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox('all')))

    canvas.bind_all("<MouseWheel>", _on_mouse_wheel_name)

    names = [i for i in cloud.getNames()]
    for i in range(len(names)):
        canvas.create_image(12, i * 90 + 8, image=nameBG, anchor='nw')
        checks.append(tk.IntVar())
        c = tk.Button(frame, text=names[i][0], bg='white', borderwidth=0, font=('Helvetica 15 bold'),
                      width=22, height=2, command=partial(showReminders, names[i][0]))
        canvas.create_window(156, i * 90 + 20, anchor='n', window=c)


def makeRemCanvas():
    for i in range(len(reminders)):
        canvas.create_image(12, i * 130 + 10, image=remBG, anchor='nw')
        checks.append(tk.IntVar())
        c = tk.Checkbutton(frame, bg='white', variable=checks[i], borderwidth=0,
                           image=noCheck, selectimage=yesCheck, onvalue=1, offvalue=0, indicatoron=False)
        canvas.create_text(55, i * 130 + 22, text=reminders[i][0], font=("Helvetica",14,'bold'), width=180, anchor='nw')
        canvas.create_text(80, i * 130 + 50, text=reminders[i][1], font=5, width=180, anchor='nw')
        canvas.create_window(30, i * 130 + 20, anchor='nw', window=c)


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
