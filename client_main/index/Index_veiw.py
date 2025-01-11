from kivy.core.window import Window
from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from utils.uix import Get_Route_View

name = "Index"

@Get_Route_View(name)
class View(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = name
        but1 = Button(text="Button 1")
        but1.bind(size=self.update_size)
        self.add_widget(but1)

    def update_size(self, widaget, size):
        print(Window.size)