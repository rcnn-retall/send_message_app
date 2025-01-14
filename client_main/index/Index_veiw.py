import requests
from kivy.uix.screenmanager import Screen
from utils.uix import Get_Route_View, U_label,u_but_bg
from kivy.graphics import  Color, BoxShadow, Rectangle
from kivy.graphics.vertex_instructions import RoundedRectangle
from kivy.metrics import dp
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.popup import Popup
from utils import config
from kivy.uix.label import Label
from utils.data import connsqlit3
import json
from kivy.uix.button import Button
from userinfo import Userinfo


name = "Index"


class new_userlist(Screen):
    def __init__(self):
        super().__init__()
        self.size_hint = (None, 1)
        self.width = dp(120)
        self.but_i = u_but_bg(text="创建会话", on_press=self.on_press)

        with self.canvas:
            Color(0, 1, 1)
            self.backgronds = BoxShadow(border_radius=[30,30,0,0],inset=True, spread_radius=[0,0])
        self.add_widget(self.but_i)
        self.bind(size=self.update)
        self.popup = Popup(title="添加用户",size_hint=(.9,.5), pos_hint={"center_x":.5, "center_y":.5})

        body = Screen()
        self.popup.add_widget(body)
        self.input = TextInput(multiline=False, size_hint=(.8, .1), pos_hint={"center_x":.5, "top":.8})
        body.add_widget(self.input)
        body.add_widget(Button(text="创建",on_press=self.on_press_but, size_hint=(.8, .1), pos_hint={"center_x":.5, "top":.6}))
        self.eroor = Label(text="", size_hint=(.8,.1), pos_hint={"center_x":.5, "top":.5}, color=(1,0,0))
        body.add_widget(self.eroor)
    def on_press(self):
        self.popup.open()

    def update(self, widget, size):
        self.backgronds.size =widget.size
    def on_press_but(self, widget):

        islist = [i.but_i.text for i in self.parent.children]
        # print(islist)
        if not self.input.text == "" and self.input.text not in islist :
            pua = {
                "username": self.parent.parent.parent.parent.username,
                "userauth": self.parent.parent.parent.parent.userauth,
                "add_user": self.input.text
            }
            try:
                response = requests.get(config.host_url + config.is_user, data=json.dumps(pua).encode("utf8"))
                if response.status_code == 200:
                    self.parent.add_widget(userlist(self.input.text))
                    self.input.text = ""
                    self.popup.dismiss()
                elif response.status_code == 500:
                    with connsqlit3() as cursor:
                        cursor.execute("delete from login_auth")

                    self.parent.parent.parent.parent.userauth = ""
                    self.parent.parent.parent.parent.username = ""
                    self.popup.dismiss()
                    self.parent.parent.parent.parent.current = Userinfo.name
                else:
                    # self.popup.dismiss()
                    self.eroor.text = json.loads(response.content)["message"]
            except Exception as e:
                self.eroor.text = "服务器断开"

        else:

            self.eroor.text = "用户已存在会话"





class userlist(Screen):
    def __init__(self, username):
        super(userlist, self).__init__()
        self.size_hint = (None, 1)
        self.width = dp(120)
        self.but_i = u_but_bg(text= username, on_press=self.on_press, on_release=self.on_release)

        with self.canvas:
            Color(0, 1, 1)

            self.backgronds = BoxShadow(border_radius=[30,30,0,0],inset=True, spread_radius=[0,0])
        self.add_widget(self.but_i)
        self.bind(size=self.update)
    def on_press(self):
        for i in self.parent.children:
            i.backgronds.spread_radius=[0,0]

        self.backgronds.spread_radius = [4,4]
    def on_release(self):
        self.backgronds.spread_radius = [8,8]
        # print(self.pos)
        self.parent.parent.parent.massae_box.backrounds.spread_radius=[8,8]
        self.parent.parent.parent.massae_box.bcna.size = self.width-dp(18), dp(40)
        # print("滚动位置",self.parent.parent.scroll_x)
        # print("盒子长度",self.parent.parent.width)
        # print("总长度",len(self.parent.children)*self.width)
        # print("控件大小",self.width)
        # print("当前位置",self.x)

        offset = self.parent.parent.scroll_x*((len(self.parent.children)*self.width) - self.parent.parent.width)
        self.parent.parent.parent.massae_box.bcna.pos = self.x+dp(9)-offset,self.parent.parent.parent.massae_box.height-dp(20)

        self.parent.parent.parent.massae_box.pos_i = self.x+dp(9)-offset,self.parent.parent.parent.massae_box.height-dp(20)

    def update(self, widget, size):
        self.backgronds.size =widget.size


class usrname_message(Screen):
    def __init__(self):
        super().__init__()
        self.size_hint = (1, .05)
        self.pos_hint={"top":1}

        self.username = U_label(text="", size_hint=(None, None), pos_hint={"x":.1,"center_y":0.5}, halign="left", valign="center")
        self.username.bind(texture_size=self.update_user)
        with self.canvas:
            Color(0, 1, 1, 1)
            self.box = RoundedRectangle(size=(dp(20),dp(20)), radius=[dp(10),dp(10)])
            self.box_i = BoxShadow(border_radius=[15,15,15,15], inset=True)


        self.add_widget(self.username)

        self.bind(pos=self.update)
    def update(self, widget, pos):
        self.box.pos = dp(5),(widget.height/2)-dp(10)



    def update_user(self, instance, value):
        print(value)
        self.username.size = value
        self.box_i.size = self.username.width + self.username.pos[0], self.height



class User_List_Screen(ScrollView):
    def __init__(self):
        super().__init__()
        self.size_hint = (1, .075)
        self.pos_hint = {"top":.95}
        self.scroll_view = BoxLayout(orientation="horizontal", size_hint=(None, 1))
        self.scroll_view.bind(minimum_width=self.scroll_view.setter("width"))
        self.add_widget(self.scroll_view)
        self.bar_width = 0
        self.pos_i =0
        self.bind(scroll_x = self.scroll_update)


        self.scroll_view.add_widget(new_userlist())
        # for i in range(10):
        #     self.scroll_view.add_widget(userlist(str(i)))
            # self.scroll_view.add_widget(Button(text=str(i), ))
    def scroll_update(self,instance, value):
        offset = (self.scroll_view.width -self.width)*value

        self.parent.massae_box.bcna.pos = self.parent.massae_box.pos_i[0]-offset, self.parent.massae_box.bcna.pos[1]

class message_body(ScrollView):
    def __init__(self):
        super().__init__()

        self.scroll_view = BoxLayout(orientation="vertical", size_hint=(1, None))
        self.scroll_view.bind(minimum_height=self.scroll_view.setter("height"))
        self.add_widget(self.scroll_view)

class Massage_canvas_Screen(Screen):
    def __init__(self):
        super().__init__()
        self.size_hint = (1, .875)
        self.pos_hint = {"top": .875}
        self.mess_scroll = message_body()
        self.add_widget(self.mess_scroll)
        self.pos_i = [0,0]
        with self.canvas:
            Color(0, 1, 1, 1)
            self.backrounds = BoxShadow(blur_radius=20, inset=True)

            Color(1,1,1)
            self.bcna = Rectangle(size=[0,0])

        self.bind(size=self.update)
    def update(self, widget, pos):
        self.backrounds.size = widget.size

@Get_Route_View(name)
class View(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.usrname_message = usrname_message()
        self.add_widget(self.usrname_message )

        self.user_list_screen = User_List_Screen()
        self.add_widget(self.user_list_screen)
        self.massae_box = Massage_canvas_Screen()
        self.add_widget(self.massae_box)



    def on_enter(self):
        self.usrname_message.username.text=self.parent.username
