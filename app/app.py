#!/usr/bin/env python
from flask import Flask, render_template, request, redirect
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.automap import automap_base
from pandas import pandas as pd
from datetime import datetime
import psycopg2
from time import sleep

app = Flask(__name__)
#api = Api(app)

sleep(3)
#DB connection
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:securepwd@db:5432/postgres"
sleep(3)
db = SQLAlchemy(app)
sleep(3)
Base = automap_base()
Base.prepare(db.engine, reflect=True)
Members = Base.classes.members
Members_info = Base.classes.members_info
Age_groups = Base.classes.age_groups
Sports = Base.classes.sports
Professionalisms = Base.classes.professionalisms
Roles = Base.classes.roles
Duration_groups = Base.classes.duration_groups
Memberships = Base.classes.memberships
#Members_sports = Base.classes.members_sports

#print(Base.classes.keys())
#print(db.query(Members).filter_by(email='giles.leonard560@mail.com').first())


members = pd.read_csv("members.csv", sep=",")

@app.route('/')
def login():
    return render_template("login.html", members=members)

@app.route('/view')
def view():
    return render_template("view.html", members=members)

@app.route('/edit', methods=[ 'POST', 'GET'])
def edit():
    if request.method == "POST":
        user_firstname = request.form['firstname']
        user_lastname = request.form['lastname']

        #push to database
        try:
            #db.session.add(user_firstname)
            #db.session.commit(user_firstname)
            return redirect('/edit')
        except:
            return "There was an Error"


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

@app.route('/createaccount')
def create_account():
    return render_template("create_account.html", members=members)

@app.route('/resetpassword')
def reset_password():
    return render_template("reset_password.html", members=members)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)