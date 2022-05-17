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

    def get_all(self):
        con = sqlite3.connect("example.db")
        cur = con.cursor()
        cur.execute("SELECT * FROM todos")
        print(list(cur))

    def delete_where(self, id_):
        con = sqlite3.connect("example.db")
        cur = con.cursor()
        cur.execute(f"DELETE from todos where todo_id={id_}")
        con.commit()
        con.close()


x = Todolist(title="mi", details="amigo", deadline=dt(2022, 5, 24, 22, 30))
x.add_data()
x.delete_where(2)
x.get_all()

