import socket
from userinfo.login import Login_View
from utils.route_list import route
from utils.response import response,eooer_response
import json
import threading
from utils.data import Data_exec
with Data_exec() as cursor:
    cursor.execute("CREATE TABLE IF NOT EXISTS UserInfo(id int NOT NULL AUTO_INCREMENT PRIMARY KEY, username CHAR(20) NOT NULL, password CHAR(20) NOT NULL)")


route_i ={}
for view_name, view in route.items():
    route_i[view_name] = view()



# print(route_i)
class Send_Message_Server(socket.socket):
    def __init__(self, family=-1, type=-1, proto=-1, fileno=None, host=None, port=None, count=None):
        super(Send_Message_Server, self).__init__(family=family, type=type, proto=proto, fileno=fileno)
        self.bind((host, port))
        self.listen(count)
    def run(self):
        while True:
            conn, host_port = self.accept()
            pud = conn.recv(1024).decode("utf-8")
            threading.Thread(target=self.route_allot, args=(conn,pud), daemon=True).start()

    def route_allot(self, conn,pud):

        pud_i = pud.split("\r\n")

        method = pud_i[0].split(" ")[0]
        path = pud_i[0].split(" ")[1][1:]
        data = pud_i[-1]

        print(pud_i)
        # print(method,path,data)
        if path in route_i:
            try:
                getattr(route_i[path], method)(conn, data)
            except Exception as e:
                error = json.dumps({"message":str(e)}).encode()
                conn.send(eooer_response(504,error))
                conn.close()
        else:
            error = json.dumps({"message": "未找到页面"}).encode()
            response_i = eooer_response(404, error)
            conn.send(response_i)
            conn.close()


server = Send_Message_Server(socket.AF_INET, socket.SOCK_STREAM, host='127.0.0.1', port=9020, count=5)
server.run()