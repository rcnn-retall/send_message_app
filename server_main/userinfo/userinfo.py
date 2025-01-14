import json
from utils.route_list import get_route
from utils.data import r_connect, Data_exec
from utils.response import response,eooer_response

@get_route("is_user")
class View():
    def GET(self,conn, data):
        # print(conn)
        pua  = json.loads(data)
        username = pua["username"]
        userauth = pua["userauth"]
        addr_user = pua["add_user"]
        try:
            redis_key= r_connect.get(username).decode()
        except Exception as e:
            redis_key = str(e)
        # print()

        if redis_key==userauth:

            with Data_exec()as cursor:
                cursor.execute("select * from userinfo where username='%s'"%addr_user)
                dictss = cursor.fetchall()
            if dictss==():
                ro = json.dumps({"message": "用户不存在"}).encode("utf8")
                ro = eooer_response(402, ro)

            else:
                ro = json.dumps({"message": "用户存在"}).encode("utf8")
                ro = response(ro)
        else:
            ro = json.dumps({"message":"验证失效"}).encode("utf8")
            ro = eooer_response(500, ro)

        conn.send(ro)
        conn.close()

        # print(r_connect.get(username))


