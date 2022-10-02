import functions
import pyodbc
from kivy.app import App
from kivy.graphics import Color, Rectangle
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.clock import Clock

class RootWidget(FloatLayout):

    def __init__(self, **kwargs):
        # make sure we aren't overriding any important functionality
        super(RootWidget, self).__init__(**kwargs)

        # let's add a Widget to this layout
        self.nameInput = TextInput(
            multiline=False,
            readonly=False,
            size_hint=(.9,.1),
            pos_hint={'center_x': .5, 'center_y': .85},
            font_size=40
        )
        self.add_widget(self.nameInput)
        self.reminderInput = TextInput(
            multiline=False,
            readonly=False,
            size_hint=(.9, .1),
            pos_hint={'center_x': .5, 'center_y': .67},
            font_size=40
        )
        self.add_widget(self.reminderInput)
        self.descriptionInput = TextInput(
            multiline=False,
            readonly=False,
            size_hint=(.9, .3),
            pos_hint={'center_x': .5, 'center_y': .38},
            font_size=18
        )
        self.add_widget(self.descriptionInput)
        self.send_button = Button(
            text = "Set Reminder",
            size_hint=(.9, .1),
            pos_hint={'center_x': .5, 'center_y': .13}
        )
        self.add_widget(self.send_button)
        self.send_button.bind(on_press=self.on_button_press)
        self.add_widget(
            Label(
                text="Name:",
                pos_hint={'center_x': .5, 'center_y': .92}
            )
        )
        self.add_widget(
            Label(
                text="Reminder:",
                pos_hint={'center_x': .5, 'center_y': .74}
            )
        )
        self.add_widget(
            Label(
                text="Description:",
                pos_hint={'center_x': .5, 'center_y': .56}
            )
        )
    def on_button_press(self, instance):
        connection = pyodbc.connect('Driver={SQL Server};'
                                    'Server=10.230.146.53,1433;'
                                    'Database=master;'
                                    'UID=root;'
                                    'PWD=password;')
        cursor = connection.cursor()
        functions.addReminder(self.nameInput.text, self.reminderInput.text, self.descriptionInput.text)
        self.send_button.text = "Reminder Added!"
        self.nameInput.text = ''
        self.reminderInput.text = ''
        self.descriptionInput.text = ''
        Clock.schedule_once(self.return_to_normal,1)
    def return_to_normal(self, *args):
        self.send_button.text = "Set Reminder"
class MainApp(App):

    def build(self):
        self.root = root = RootWidget()
        root.bind(size=self._update_rect, pos=self._update_rect)

        with root.canvas.before:
            Color(.5, 0, 0, 1)  # green; colors range from 0-1 not 0-255
            self.rect = Rectangle(size=root.size, pos=root.pos)
        return root

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

if __name__ == "__main__":
    app = MainApp()
    app.run()