from kivy.core.window import Window
from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button

name = "Index"

class View(Screen):
    def __init__(self, **kwargs):
        super(View, self).__init__(**kwargs)
        self.name = name
        but1 = Button(text="Button 1")

        but1.bind(size=self.update_size)
        self.add_widget(but1)

    def update_size(self, widaget, size):
        print(Window.size)