from kivy.uix.screenmanager import Screen
# from kivy.uix.button import Button
from utils.uix import U_button, U_clear_color_Button
from kivy.metrics import sp

name = "User"

class View(Screen):
    def __init__(self, **kwargs):
        super(View, self).__init__(**kwargs)
        self.name = name
        self.add_widget(U_clear_color_Button(text="用户登入", font_size=sp(20), size_hint=(.5,.075), pos_hint={"top":1,"left":1}))
        self.add_widget(U_clear_color_Button(text="用户注册", font_size=sp(20), size_hint=(.5,.075),pos_hint={"top":1,"right":1}))



