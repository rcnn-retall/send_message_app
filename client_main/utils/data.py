import sqlite3


db = "utils/data.db"


class connsqlit3(sqlite3.Connection):
    def __init__(self, db=db):
        super().__init__(db)

    def __enter__(self):
        self.cursor_i = self.cursor()
        self.cursor_i.execute("create table if not exists login_auth(id integer primary key,userauth text not null,username text not null)")
        # self.cursor_i.execute()
        return self.cursor_i
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.commit()
        self.cursor_i.close()
        self.close()