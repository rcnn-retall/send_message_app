from future.backports.http.client import responses
from utils.route_list import get_route
import json
from utils.response import response

@get_route("login")
class Login_View(object):

    def GET(self, conn, data):
        str_i = "python服务器"

        # return
        response_i = response(str_i.encode())
        # print(response_i)
        conn.send(response_i)
        conn.close()

    def POST(self, conn, data):
        str_i = json.dumps({"userauth":"123"})


        # return
        print(data)
        response_i = response(str_i.encode())
        # print(response_i)
        conn.send(response_i)
        conn.close()

