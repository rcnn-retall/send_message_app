from future.backports.http.client import responses
from utils.route_list import get_route
import json
from utils.response import response,eooer_response
from utils.data import Data_exec,r_connect
import base64
import time


@get_route("login")
class Login_View(object):
    def POST(self, conn, data):




        data  = json.loads(data)

        with Data_exec() as cursor:
            cursor.execute('select * from userinfo where username="%s"' % data['username'])
            exec_message = cursor.fetchone()
            print(exec_message)

        if exec_message:
            username = exec_message[1]
            password = exec_message[-1]
            if username == data['username'] and password == data['password']:
                # key用户名， vlaue 验证字符串
                auth_str = base64.b32encode((str(time.time())+username).encode("utf-8")).decode("utf-8")
                r_connect.setex(username, 10080, auth_str)


                str_i = json.dumps({"userauth": auth_str})
                response_i = response(str_i.encode())


                # print(r_connect.get(username))

            else:
                str_i = json.dumps({"userauth": "密码错误"})
                response_i = eooer_response(402, str_i.encode())



        else:
            str_i = json.dumps({"userauth": "用户不存在"})
            response_i = eooer_response(400,str_i.encode())






        conn.send(response_i)
        conn.close()


