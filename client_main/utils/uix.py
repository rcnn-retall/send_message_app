from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.utils import get_color_from_hex


class U_wiget(object):
    def __init__(self):
        self.color = get_color_from_hex("#000000")

class U_label(Label, U_wiget):
    def __init__(self,**kwargs):
        super(U_label, self).__init__()
        for key,value in kwargs.items():
            self.__setattr__(key,value)


class U_button(Button, U_wiget):
    def __init__(self,**kwargs):
        super(U_button, self).__init__()
        for key, value in kwargs.items():
            self.__setattr__(key, value)



