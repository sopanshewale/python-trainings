#!/usr/bin/python3
import sqlite3
import pandas as pd

db_filename = 'todo.db'

with sqlite3.connect(db_filename) as conn:
    cursor = conn.cursor()

    cursor.execute(""" select id, priority, details, status, deadline from task where project = 'assignments' """)

    for row in cursor.fetchall():
        task_id, priority, details, status, deadline = row
        print('{:2d} [{:d}] {:<25} [{:<8}] ({})'.format( task_id, priority, details, status, deadline))

db_connection = sqlite3.connect(db_filename)
df = pd.read_sql('SELECT id, priority, details, status, deadline  FROM task', con=db_connection)
print (df)

