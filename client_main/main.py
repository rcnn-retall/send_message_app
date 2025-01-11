from kivy.config import Config
Config.set("graphics","width", 400)
Config.set("graphics","height", 773)
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, NoTransition
from kivy.core.text import LabelBase
from index import Index_veiw
from userinfo import Userinfo
from kivy.core.window import Window
from kivy.utils import get_color_from_hex


route_view = {
    Index_veiw.name : Index_veiw.View(),
    Userinfo.name : Userinfo.View(),
              }



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
            self.body.add_widget(screen_view)


        self.body.current = Userinfo.name


Main = Message_Client_App()
Main.run()