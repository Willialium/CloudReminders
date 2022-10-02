import functions
import pyodbc
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class MainApp(App):
    def build(self):
        main_layout = BoxLayout(orientation="vertical")
        self.nameInput = TextInput(
            multiline=False, readonly=False, halign="left", font_size=30
        )
        main_layout.add_widget(self.nameInput)
        self.detailsInput = TextInput(
            multiline=True, readonly=False, halign="left", font_size=18
        )
        main_layout.add_widget(self.detailsInput)
        send_button = Button(
            text="Set Reminder", pos_hint={"center_x": 0.5, "center_y": 0.5}
        )
        main_layout.add_widget(send_button)
        send_button.bind(on_press=self.on_button_press)

        return main_layout

    def on_button_press(self, instance):
        connection = pyodbc.connect('Driver={SQL Server};'
                                    'Server=WINDELL-T2U0QEF;'
                                    'Database=mydb;'
                                    'Trusted_Connection=True;')
        cursor = connection.cursor()
        functions.addReminder(self.nameInput.text, self.detailsInput.text)

if __name__ == "__main__":
    app = MainApp()
    app.run()