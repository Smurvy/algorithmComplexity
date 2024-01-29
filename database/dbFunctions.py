import sqlite3
import math

def createConnection(dbFile):
    conn = None
    try:
        conn = sqlite3.connect(dbFile)
    except Exception as e:
        print(e)

    return conn

def getVals(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM function")

    rows = cur.fetchall()

    return rows

def pushVals(conn):
    cur = conn.cursor()

    for x in range(5):
        cur.execute("INSERT INTO function (x,y) VALUES (?,?)",
                    (x,math.pow(x,2)))
    
    conn.commit()

def resetVals(conn):
    cur = conn.cursor()

    cur.execute("DELETE FROM function")

    conn.commit()
    
