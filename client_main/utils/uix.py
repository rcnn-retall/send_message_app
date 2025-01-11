from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.utils import get_color_from_hex
from kivy.graphics import Rectangle, Color, BoxShadow
from kivy.uix.textinput import TextInput
from kivy.metrics import dp


class U_input_text(TextInput):
    def __init__(self,**kwargs):
        super().__init__()
        self.background_color = (1,1,1,0)
        self.font_name="font/msyh.ttc"
        for key, value in kwargs.items():
            self.__setattr__(key,value)
        with self.canvas.before:
            Color(*get_color_from_hex("#b6b6ba"))
            self.rect = Rectangle()
        self.bind(size=self.update_rect, pos=self.update_rect)

    def update_rect(self,widget, value):
        self.rect.size= widget.width, dp(2)
        self.rect.pos = widget.pos



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

class U_clear_color_Button(Button, U_wiget):
    def __init__(self,**kwargs):
        super(U_clear_color_Button, self).__init__()
        for key, value in kwargs.items():
            self.__setattr__(key,value)
        self.background_color = (1,1,1,0)
        with self.canvas.before:
            Color(*get_color_from_hex("#000000"))
            if self.pos_box=="left":
                self.rect = BoxShadow(inset=True, border_radius=[0,0,30,0], pos=(1000,1000), blur_radius=1000)
                self.bold = True
            else:
                self.rect = BoxShadow(inset=True, border_radius=[0,0,0,30], pos=(1000,1000), blur_radius=1000)
                self.color = get_color_from_hex("#ffffff")
                self.bold = False
        self.bind(size= self.update_size, pos=self.update_size)

    def update_size(self,widget, value):
        self.rect.size = widget.size
        if widget.pos_box=="right":
            self.rect.pos = widget.pos
    def on_press(self):
        sm = [i for i in self.parent.children if type(i).__name__ == "ScreenManager"][0]
        for i in self.parent.children:
            if type(i).__name__ == "ScreenManager":
                print(i.__class__.__name__)

            elif i.pos_box==self.pos_box:

                i.rect.pos = (1000,1000)
                sm.current = i.pos_box
                i.color = get_color_from_hex("#000000")
                i.bold = True

            else:
                i.rect.pos = i.pos
                i.color = get_color_from_hex("#ffffff")
                i.bold = False


