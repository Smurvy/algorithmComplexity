import sqlite3
import math

connection = sqlite3.connect('database/database.db')

cur = connection.cursor()

with open('database/schema.sql') as f:
    connection.executescript(f.read())


connection.commit()
connection.close()
