import sqlite3
import math

connection = sqlite3.connect('database/database.db')

cur = connection.cursor()

with open('database/schema.sql') as f:
    connection.executescript(f.read())

for x in range(50):
    cur.execute("INSERT INTO function (x,y) VALUES (?,?)",
                (x,math.pow(x,2)))
        

connection.commit()
connection.close()
