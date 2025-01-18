from utils.route_list import get_route
from utils.data import r_connect
from utils.response import eooer_response, response

import json


@get_route("io_message")
class send_rect_massage:
    def GET(self, conn, data):
        # print("这个接口用来接收信息")
        # print(conn, data)
        pua = json.loads(data)
        username = pua["username"]
        message = r_connect.lrange(username+"_l",0, -1)
        message = [i.decode("utf-8") for i in message]
        r_connect.ltrim(username+"_l",1, 0)

        resp = json.dumps({"message": message}).encode("utf-8")

        conn.send(response(resp))
        conn.close()




    def POST(self, conn, data):
        #这个接口用来发送信息

        pud = json.loads(data)
        userauth = pud["userauth"]
        s_username = pud["s_username"]
        d_sername = pud["d_username"]
        message = pud["message"]

        auth_si = r_connect.get(s_username)
        auth_redis = "" if auth_si==() else auth_si.decode()
        if userauth == auth_redis:
            resp = response(json.dumps({"message": "send_ok123"}).encode("utf-8"))
            message = json.dumps({s_username:message})
            print(d_sername+"_l")
            print(message)
            r_connect.lpush(d_sername+"_l", message)
            # r_connect.commit()
            # print(123)
        else:
            # print(456)
            resp = eooer_response(500, json.dumps({"massage":"用户验证失败"}).encode("utf-8"))
        # print(567)
        print(resp)
        conn.send(resp)
        conn.close()

