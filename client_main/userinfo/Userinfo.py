from kivy.uix.screenmanager import Screen, ScreenManager, NoTransition
from utils.uix import U_button, U_clear_color_Button,U_label,U_input_text
from kivy.uix.button import Button
from kivy.metrics import sp
from kivy.utils import get_color_from_hex


name = "User"

class Register_screen(Screen):
    def __init__(self, **kwargs):
        super(Register_screen, self).__init__(**kwargs)
        self.name = "right"
        self.add_widget(U_label(text="暂时未开发"))

class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.name = "left"
        # self.add_widget(U_label(text="login"))
        self.title  = U_label(text="用户登入", size_hint=(1, .1), font_size="40sp", bold=True, pos_hint={"top":.9})

        self.input_user = U_input_text(
            size_hint=(.8,.075), pos_hint={"center_x": .5, "top":.75}, font_size="31sp",
            multiline=False,hint_text="请输入用户名"
                                       )
        self.input_password = U_input_text(
            size_hint=(.8,.075), pos_hint={"center_x": .5,"top":.6}, font_size="31sp",
            multiline=False,hint_text="请输入密码",password=True,password_mask="*"
        )



        self.add_widget(Button(text="登入", size_hint=(.6, .075), pos_hint={"center_x": .5, "top":.45},font_size="31sp", bold=True,
                               color=get_color_from_hex("#d3bc8e")
                               ,background_normal="static/button.png",background_down="static/button1.png"
                               ))
        self.add_widget(self.title)
        self.add_widget(self.input_user)
        self.add_widget(self.input_password)




class View(Screen):
    def __init__(self, **kwargs):
        super(View, self).__init__(**kwargs)
        self.name = name
        self.add_widget(U_clear_color_Button(text="用户登入", font_size=sp(20), size_hint=(.5,.075), pos_hint={"top":1,"left":1}, pos_box="left"))
        self.add_widget(U_clear_color_Button(text="用户注册", font_size=sp(20), size_hint=(.5,.075),pos_hint={"top":1,"right":1}, pos_box="right"))


        self.sm_body = ScreenManager(transition=NoTransition(), size_hint=(1, .925))
        self.sm_body.add_widget(Register_screen())
        self.sm_body.add_widget(LoginScreen())
        self.add_widget(self.sm_body)

    def on_enter(self, *args):
        self.sm_body.current = "left"




