import pymysql
import redis



class Data_exec(pymysql.Connect):
    def __init__(self,
        user="root",  # The first four arguments is based on DB-API 2.0 recommendation.
        password="202468",
        host="127.0.0.1",
        database="py_data",
        port=3306):
        super(Data_exec, self).__init__(user=user, password=password, host=host, database=database, port=port)

    def __enter__(self):
        self.cursor_i = self.cursor()

        return self.cursor_i

    def __exit__(self, exc_type, exc_val, exc_tb):


        self.commit()
        self.cursor_i.close()
        self.close()



r_connect = redis.Redis(host='localhost', port=6379, db=0)




    # conn.commit()

    # cursor.execute("INSERT INTO UserInfo(username, password) VALUES (%s, %s)", ("月", "admin"))
    # conn.commit()


