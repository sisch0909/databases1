#!/usr/bin/env python
from flask import Flask, render_template, request, redirect, session
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.automap import automap_base
from pandas import pandas as pd
from datetime import datetime
import psycopg2
from time import sleep

app = Flask(__name__)
#api = Api(app)

#DB connection
app.config["SECRET_KEY"] = "qwertyuiop"
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:securepwd@db:5432/postgres"
sleep(3)
db = SQLAlchemy(app)

Base = automap_base()
Base.prepare(db.engine, reflect=True)
Members = Base.classes.members
Members_info = Base.classes.members_info
Age_groups = Base.classes.age_groups
#Sports = Base.classes.sports
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
    user_id = session["user_id"]
    user_data = db.session.query(Members_info).filter_by(member_id=user_id).first()

    return render_template("view.html", members=members, user_data = user_data)


@app.route('/')
def logout():
    session.clear()
    return render_template("login.html")

@app.route('/edit', methods=[ 'POST', 'GET'])
def edit():
    user_id = session["user_id"]
    user_info_data = db.session.query(Members_info).filter_by(member_id=user_id).first()
    
    #get info from data
    firstname = request.form.get("firstname")
    lastname = request.form.get("lastname")
    gender = request.form.get("gender")
    phone = request.form.get("phone")
    #email = request.form.get("email")

    
    

    

    if request.method == "POST":
        user_firstname = request.form['firstname']
        user_lastname = request.form['lastname']

        #push to database
        #user_info_data.first_name = firstname
        user_info_data.last_name = lastname
        #user_info_data.gender = gender
        #user_info_data.phone_number = phone
    #   user_info_data.email = email
        db.session.commit()
        update_statement=" Your data has been succesfully updated!"
        return render_template("edit.html", update_statement=update_statement, members=members, user_info_data = user_info_data)


    return render_template("edit.html", members=members, user_info_data = user_info_data)

@app.route('/home')
def home():
    return render_template("home.html", members=members)

@app.route('/login', methods=["POST"])
def loginpage():
    email = request.form.get("email")
    password = request.form.get("password")
    #id=0
    #i=0
    error_statement=""
    exists = db.session.query(db.exists().where(Members.email == email)).scalar()

    if not email or not password:
        error_statement = "Please fill in missing fields"
        return render_template("login.html", 
        email=email, 
        password=password, 
        error_statement=error_statement)
    elif exists == True:
        user = db.session.query(Members).filter_by(email=email).first()
        user_info = db.session.query(Members_info).filter_by(email=email).first()
        if user.pw == password:
            session["user_id"] = user_info.member_id
            nachricht = session["user_id"]
            return render_template("welcome.html", nachricht=nachricht)
        else:
            error_statement = "Wrong email or password"
            return render_template("login.html", 
            email=email, 
            password=password, 
            error_statement=error_statement)
    else:
        error_statement = "Wrong email or password"
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
    firstname = request.form.get("firstname")
    lastname = request.form.get("lastname")
    gender = request.form.get("gender")
    phone = request.form.get("phone")
    membership_type = request.form.get("membership_type")
    #birthdate = request.form.get("birthdate")
    #email = request.form.get("email")
    if request.method == "POST":
        new_member1 = Members_info(email="fgehfkshfsd@fsd.com", first_name=firstname, last_name=lastname, phone_number=phone, birthday="2000-01-01", gender=gender, membership_type_id=membership_type, duration_group=1, role_id=4)
        db.session.add(new_member1)
        db.session.commit()
        update_statement="Application has been sent. You can now login."
        return render_template("create_account.html", update_statement=update_statement)

    return render_template("create_account.html")

@app.route('/resetpassword')
def reset_password():
    return render_template("reset_password.html", members=members)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)