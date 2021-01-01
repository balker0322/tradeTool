
from .task import Task, info_list
import sqlite3
# import copy

class Model(): 
    def __init__(self, db):
        self.db = db
        # self.conn = sqlite3.connect(db)
        self.info_list = info_list
        columns = ", ".join([info + " text" for info in self.info_list[1:]])
        with sqlite3.connect(self.db) as con:
            cur = con.cursor()
            cur.execute(
                "CREATE TABLE IF NOT EXISTS tasks (" + self.info_list[0] + " INTEGER PRIMARY KEY, " + 
                columns + ")")
            con.commit()

    def add_new_task(self, new_task : Task):
        # new_task = new_task.copy()
        new_task_info = [new_task.task_info[info] for info in self.info_list[1:]]
        question_marks = ", ".join(["?" for _ in range(len(self.info_list[1:]))])
        with sqlite3.connect(self.db) as con:
            cur = con.cursor()
            cur.execute("INSERT INTO tasks VALUES (NULL, " + question_marks + ")",
                            tuple(new_task_info))
            con.commit()

    def get_all_pending_tasks(self):

        rows = list()
        with sqlite3.connect(self.db) as con:
            cur = con.cursor()
            columns = ", ".join(self.info_list)
            cur.execute("SELECT " + columns + " FROM tasks")
            rows = cur.fetchall()

        task_list = []
        for row in rows:
            task = Task()
            for i, info in enumerate(self.info_list):
                task.task_info[info] = row[i]
            task_list.append(task)

        return task_list

    def update_task(self, new_task_details : Task):
        new_task_id = new_task_details.get_id()
        new_task_info = [new_task_details.task_info[info] for info in self.info_list[1:]]
        new_task_info.append(new_task_id)
        columns = [info + " = ?" for info in self.info_list[1:]]
        columns = ", ".join(columns)
        with sqlite3.connect(self.db) as con:
            cur = con.cursor()
            cur.execute("UPDATE tasks SET " + columns + " WHERE id = ?",
                         tuple(new_task_info))
            con.commit()

# for reference
'''
class Database:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS parts (id INTEGER PRIMARY KEY, part text, customer text, retailer text, price text)")
        self.conn.commit()

    def fetch(self):
        self.cur.execute("SELECT * FROM parts")
        rows = self.cur.fetchall()
        return rows

    def insert(self, part, customer, retailer, price):
        self.cur.execute("INSERT INTO parts VALUES (NULL, ?, ?, ?, ?)",
                         (part, customer, retailer, price))
        self.conn.commit()

    def remove(self, id):
        self.cur.execute("DELETE FROM parts WHERE id=?", (id,))
        self.conn.commit()

    def update(self, id, part, customer, retailer, price):
        self.cur.execute("UPDATE parts SET part = ?, customer = ?, retailer = ?, price = ? WHERE id = ?",
                         (part, customer, retailer, price, id))
        self.conn.commit()

    def __del__(self):
        self.conn.close()

'''