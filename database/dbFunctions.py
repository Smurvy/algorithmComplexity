import sqlite3

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