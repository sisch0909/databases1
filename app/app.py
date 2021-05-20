from flask import Flask, render_template
from flask_restful import Resource, Api
import pandas as pd

app = Flask(__name__)
api = Api(app)



@app.route('/')
def index():
    return render_template("index.html")

@app.route('/view')
def view():
    return render_template("view.html")

@app.route('/edit')
def edit():
    return render_template("edit.html")

@app.route('/home')
def home():
    return render_template("home.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)