from kivy.uix.screenmanager import Screen, ScreenManager, NoTransition
from pandas.core.interchange.from_dataframe import primitive_column_to_ndarray
from utils.uix import U_button, U_clear_color_Button,U_label,U_input_text,Get_Route_View
from utils.data import connsqlit3
from kivy.uix.label import Label
import requests
from kivy.uix.button import Button
from kivy.metrics import sp
from kivy.utils import get_color_from_hex
import json


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

        self.eooer_show = Label(text="", color=(1,0,0),size_hint=(None, None), pos_hint={"x": .1, "top":.65}, font_size="22sp")
        self.eooer_show.bind(texture_size=self.eooer_show.setter("size"))

        self.input_password = U_input_text(
            size_hint=(.8,.075), pos_hint={"center_x": .5,"top":.6}, font_size="31sp",
            multiline=False,hint_text="请输入密码",password=True,password_mask="*"
        )


        self.add_widget(self.eooer_show)
        self.add_widget(Button(text="登入", size_hint=(.6, .075), pos_hint={"center_x": .5, "top":.45},font_size="31sp", bold=True,
                               color=get_color_from_hex("#d3bc8e")
                               ,background_normal="static/button.png",background_down="static/button1.png", on_press=self.login
                               ))
        self.add_widget(self.title)
        self.add_widget(self.input_user)
        self.add_widget(self.input_password)
    def login(self, widget):
        username = self.input_user.text
        password = self.input_password.text

        pua = json.dumps({"username": username, "password": password})

        login_message = requests.post("http://127.0.0.1:9020/login", data=pua)
        userauth = json.loads(login_message.text)

        if login_message.status_code == 200:
            with connsqlit3() as cursor:
                cursor.execute("delete from login_auth")
                cursor.execute('insert into login_auth(id, userauth) values (1, "%s")'%userauth["userauth"])
        else:
            self.eooer_show.text = userauth["userauth"]






@Get_Route_View(name)
class View(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.add_widget(U_clear_color_Button(text="用户登入", font_size=sp(20), size_hint=(.5,.075), pos_hint={"top":1,"left":1}, pos_box="left"))
        self.add_widget(U_clear_color_Button(text="用户注册", font_size=sp(20), size_hint=(.5,.075),pos_hint={"top":1,"right":1}, pos_box="right"))
        self.sm_body = ScreenManager(transition=NoTransition(), size_hint=(1, .925))
        self.sm_body.add_widget(Register_screen())
        self.sm_body.add_widget(LoginScreen())
        self.add_widget(self.sm_body)

    def on_enter(self, *args):
        self.sm_body.current = "left"




