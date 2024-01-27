from flask import Flask, render_template
import database.dbFunctions as db
import math


app = Flask(__name__)


@app.route('/')
def homepage():
    conn = db.createConnection("database/database.db")

    data = db.getVals(conn)
    
    labels = [row[0] for row in data]
    values = [row[1] for row in data]

    conn.close()

    return render_template('graph.html', labels=labels, values=values)

