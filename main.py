from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def homepage():
    data = [
        ("01-01-2020",1597),
        ("02-01-2020",1250),
        ("03-01-2020",1386),
        ("04-01-2020",1087),
        ("05-01-2020",1698),
        ("06-01-2020",1987)
    ]
    
    labels = [row[0] for row in data]
    values = [row[1] for row in data]

    return render_template('graph.html', labels=labels, values=values)
