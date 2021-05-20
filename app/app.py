#!/usr/bin/env python
from flask import Flask, render_template
from flask_restful import Resource, Api
#from flask_sqlalchemy import SQLAlchemy
from pandas import pandas as pd

app = Flask(__name__)
api = Api(app)

#DB connection
#app.config["SQLAlchemy_DATABASE_URI"] = 'mysql://postgres:securepwd@db/main'

members = pd.read_csv("members.csv", sep=",")

@app.route('/')
def login():
    return render_template("login.html", members=members)

@app.route('/view')
def view():
    return render_template("view.html", members=members)

@app.route('/edit')
def edit():
    return render_template("edit.html", members=members)

@app.route('/home')
def home():
    return render_template("home.html", members=members)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)