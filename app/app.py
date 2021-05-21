#!/usr/bin/env python
from flask import Flask, render_template, request
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

@app.route('/login', methods=["POST"])
def loginpage():
    email = request.form.get("email")
    password = request.form.get("password")
    id=0
    i=0
    error_statement=""
    if not email or not password:
        error_statement = "Please fill in missing field"
        return render_template("login.html", 
            email=email, 
            password=password, 
            error_statement=error_statement)
    #while i == 1:
      #  if email == members.email.id:
       #     if password == members.pw.id:
        #        #return render_template("welcome.html", members=members)
         #       i=0
        #else:
        #    id=+1
        #    i=1
        #    return render_template("wrongpwd.html", member=len(members))

@app.route('/edit', methods=["POST"])
def update_data():
    email = request.form.get("email")
    password = request.form.get("password")
    update_statement=" Your data has been succesfully updated!"
    return render_template("edit.html", update_statement=update_statement, members=members)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)