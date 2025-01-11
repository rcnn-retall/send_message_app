from kivy.config import Config
Config.set("graphics","width", 400)
Config.set("graphics","height", 773)
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, NoTransition
from kivy.core.text import LabelBase
from userinfo import Userinfo
from index import Index_veiw
from kivy.core.window import Window
from kivy.utils import get_color_from_hex
from utils.uix import route_view

LabelBase.register("Roboto", fn_regular="font/msyh.ttc", fn_bold="font/msyhbd.ttc")

class Message_Client_App(App):
    def __init__(self):
        super().__init__()
        self.body = ScreenManager(transition=NoTransition())
        Window.clearcolor = get_color_from_hex('#FFFFFF')

    def build(self):
        return self.body
    def on_start(self):
        for screen_name, screen_view in route_view.items():
            print(screen_name, screen_view)
            self.body.add_widget(screen_view())



Main = Message_Client_App()
Main.run()