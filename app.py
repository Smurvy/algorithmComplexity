from flask import Flask, render_template,request
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

@app.route('/data-seed', methods=['POST'])
def update():
    conn = db.createConnection("database/database.db")
    
    db.pushVals(conn)

    conn.close()
    
    return homepage()

@app.route('/data-reset', methods=['POST'])
def reset():
    conn = db.createConnection("database/database.db")
    
    db.resetVals(conn)

    conn.close()
    
    return homepage()

@app.route('/graph', methods=['GET'])
def graph():
    conn = db.createConnection("database/database.db")

    db.resetVals(conn)

    data = db.getVals(conn)
    
    
    labels = [row[0] for row in data]
    values = [row[1] for row in data]

    conn.close()

    return render_template('graph.html', labels=labels, values=values)
    





