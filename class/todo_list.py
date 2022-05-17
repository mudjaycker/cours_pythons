from datetime import datetime as dt
from pprint import pprint

import sqlite3


_CON = sqlite3.connect("example.db")
cur =_CON.cursor()
cur.execute(
"""CREATE TABLE IF NOT EXISTS  todos
            (id int not null AUTO_INCREMENT ,title varchar(45), details text, register_date datetime, 
            deadline datetime, is_completed varchar(5)), PRIMARY KEY(id)"""
            )

cur.close()
class Todolist:
    def __init__(
        self, title, details, deadline, resgister_date=dt.now(), is_completed=False
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
            f"""INSERT INTO todos VALUES ('{self.title}', '{self.details}', 
            '{self.resgister_date}', '{self.deadline}', '{self.is_completed}')"""
            )
        con.commit()
        con.close()

    def get_all(self):
        con = sqlite3.connect("example.db")
        cur = con.cursor()
        cur.execute("SELECT * FROM todos")
        print(list(cur))



x = Todolist("mi", "amigo", dt(2022, 5, 24, 22, 30))
x.add_data()
x.get_all()

