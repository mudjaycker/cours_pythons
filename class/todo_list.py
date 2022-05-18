from datetime import datetime as dt
from pprint import pprint

import sqlite3


_CON = sqlite3.connect("example.db")
cur =_CON.cursor()
cur.execute(
"""CREATE TABLE IF NOT EXISTS  todos
            (todo_id INTEGER PRIMARY KEY, title varchar(45), details text, register_date datetime, 
            deadline datetime, is_completed varchar(5))"""
            )

cur.close()
class Todolist:
    def __init__(
         self, title="NULL", details="NULL", deadline="NULL", resgister_date=dt.now(), is_completed=False
    ):

        self.title = title
        self.details = details
        self.resgister_date = resgister_date
        self.deadline = deadline
        self.is_completed = is_completed


    def add_data(self):
        con = sqlite3.connect("example.db")
        cur = con.cursor()
        cur.execute(
            f"""INSERT INTO todos VALUES (NULL,'{self.title}', '{self.details}', 
            '{self.resgister_date}', '{self.deadline}', '{self.is_completed}')"""
            )
        con.commit()
        con.close()

    @classmethod
    def get_all(cls):
        con = sqlite3.connect("example.db")
        cur = con.cursor()
        cur.execute("SELECT * FROM todos where is_completed")
        return list(cur)

    @classmethod
    def get_completed(cls):
        con = sqlite3.connect("example.db")
        cur = con.cursor()
        cur.execute("SELECT * FROM todos where is_completed is 'True'")
        return list(cur)

    @classmethod
    def get_uncompleted(cls):
        con = sqlite3.connect("example.db")
        cur = con.cursor()
        cur.execute("SELECT * FROM todos where is_completed is 'False'")
        return list(cur)


    @classmethod
    def get_whrere(cls, id_):
        con = sqlite3.connect("example.db")
        cur = con.cursor()
        cur.execute(f"SELECT * FROM todos where todo_id={id_}")
        return [x for x in cur]

    @classmethod
    def get_whrere(cls, id_):
        con = sqlite3.connect("example.db")
        cur = con.cursor()
        cur.execute(f"SELECT * FROM todos where todo_id={id_}")
        return list(cur)

    def update_where(self, id_):
        con = sqlite3.connect("example.db")
        cur = con.cursor()
        cur.execute(f"""UPDATE todos SET title={self.title}, details={self.details}
        register_date={self.resgister_date}, deadline={self.deadline}, is_completed={self.is_completed},   
        where todo_id={id_}""")
        con.close()


for x in Todolist.get_all():
    print(x)
