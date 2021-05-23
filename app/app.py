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

# DB connection
app.config["SECRET_KEY"] = "qwertyuiop"
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:securepwd@db:5432/postgres"
sleep(3)
db = SQLAlchemy(app)

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
Members_sports = Base.classes.members_sports

# print(Base.classes.keys())
# print(db.query(Members).filter_by(email='giles.leonard560@mail.com').first())

# For string in navbar
logged_in = False
if logged_in == False:
    nav_string = "My personal data"
else:
    user_id = session["user_id"]
    nav_name = db.session.query(Members_info).filter_by(
        member_id=user_id).first()
    nav_string = nav_name.first_name + " " + nav_name.last_name

members = pd.read_csv("members.csv", sep=",")


# Home
@app.route('/home')
def home():
    return render_template("home.html", nav_string=nav_string)


# Loginpage
@app.route('/')
def login():
    return render_template("login.html", nav_string=nav_string)


@app.route('/login', methods=["POST"])
def loginpage():
    email = request.form.get("email")
    password = request.form.get("password")
    error_statement = ""
    exists = db.session.query(db.exists().where(
        Members.email == email)).scalar()

    if not email or not password:
        error_statement = "Please fill in missing fields"
        return render_template("login.html",
                               email=email,
                               password=password,
                               error_statement=error_statement,
                               nav_string=nav_string)
    elif exists == True:
        user = db.session.query(Members).filter_by(email=email).first()
        user_info = db.session.query(
            Members_info).filter_by(email=email).first()
        if user.pw == password:
            session["user_id"] = user_info.member_id
            nachricht = session["user_id"]
            logged_in = True
            return render_template("welcome.html", nachricht=nachricht, nav_string=nav_string)
        else:
            error_statement = "Wrong email or password"
            return render_template("login.html",
                                   email=email,
                                   password=password,
                                   error_statement=error_statement,
                                   nav_string=nav_string)
    else:
        error_statement = "Wrong email or password"
        return render_template("login.html",
                               email=email,
                               password=password,
                               error_statement=error_statement,
                               nav_string=nav_string)


# Logout
@app.route('/')
def logout():
    session.clear()
    nav_string = "My personal data"
    logged_out()
    return render_template("login.html", nav_string=nav_string)


# View data
@app.route('/view')
def view():
    user_id = session["user_id"]
    user_data = db.session.query(Members_info).filter_by(
        member_id=user_id).first()
    user_sports_query = db.session.query(Members_sports).filter_by(member_id=user_id).all()
    user_sports =[]
    for i in user_sports_query:
        sports_query = db.session.query(Sports).filter_by(sport_id=i.sport_id).first()
        user_sports.append(sports_query.sport_name)
    print(user_sports)

#    for i in user_sports:
#        try:
#            if sports_query
#        professionalism_exists = db.session.query.filter(Professionalisms.professionalism_id)
#        if sports_query.:
#            professionalism_discount_query = db.session.query(Professionalisms).filter_by(professionalism_id = user_sports_query.professionalism_id).first()
#            professionalism_discount = professionalism_discount_query.discount
#        else:
#            professionalism_discount_query = db.session.query(Professionalisms).filter_by(professionalism_id = 2).first()
#            professionalism_discount = professionalism_discount_query.discount
    return render_template("view.html", user_data=user_data, user_sports=user_sports, nav_string=nav_string)


# edit data
@app.route('/edit', methods=["POST"])
def update_data():
    user_id = session["user_id"]
    user_info_data = db.session.query(
        Members_info).filter_by(member_id=user_id).first()

    # get info from html
    firstname = request.form.get("firstname")
    lastname = request.form.get("lastname")
    phone = request.form.get("phone")
    email = request.form.get("email")
    membership_type = request.form.get("membership_type")

    if request.method == "POST":
        if request.form.get("update"):
            # push to database
            user_info_data.first_name = firstname
            user_info_data.last_name = lastname
            user_info_data.phone_number = phone
            user_info_data.email = email
            user_info_data.membership_type_id = membership_type
            db.session.commit()

            update_statement = "Your data has been succesfully updated!"
            return render_template("edit.html",
                                   update_statement=update_statement,
                                   members=members,
                                   user_info_data=user_info_data,
                                   nav_string=nav_string)
        elif request.form.get("delete"):
            update_statement = "Your account has been succesfully deleted!"
            return render_template("edit.html",
                                   update_statement=update_statement,
                                   members=members,
                                   user_info_data=user_info_data,
                                   nav_string=nav_string)

    return render_template("edit.html",
                           update_statement=update_statement,
                           members=members,
                           nav_string=nav_string, user_info_data=user_info_data)


@app.route('/edit', methods=['POST', 'GET'])
def edit():
    user_id = session["user_id"]
    user_info_data = db.session.query(
        Members_info).filter_by(member_id=user_id).first()

    # get info from html
    firstname = request.form.get("firstname")
    lastname = request.form.get("lastname")
    phone = request.form.get("phone")
    email = request.form.get("email")
    membership_type = request.form.get("membership_type")

    if request.method == "POST":
        if request.form.get("update"):
            # push to database
            user_info_data.first_name = firstname
            user_info_data.last_name = lastname
            user_info_data.phone_number = phone
            user_info_data.email = email
            user_info_data.membership_type_id = membership_type
            db.session.commit()

            update_statement = "Your data has been succesfully updated!"
            return render_template("edit.html",
                                   update_statement=update_statement,
                                   members=members,
                                   user_info_data=user_info_data,
                                   nav_string=nav_string)
        elif request.form.get("delete"):
            update_statement = "Your account has been succesfully deleted!"
            return render_template("edit.html",
                                   update_statement=update_statement,
                                   members=members,
                                   user_info_data=user_info_data,
                                   nav_string=nav_string)

    return render_template("edit.html",
                           members=members,
                           user_info_data=user_info_data,
                           nav_string=nav_string)


# Create new account
@app.route('/createaccount')
def create_account():
    return render_template("create_account.html", nav_string=nav_string)


@app.route('/createaccount', methods=["POST"])
def really_create_account():
    firstname = request.form.get("firstname")
    lastname = request.form.get("lastname")
    gender = request.form.get("gender")
    phone = request.form.get("phone")
    membership_type = request.form.get("membership_type")
    birthdate = request.form.get("birthdate")
    email = request.form.get("email")
    password = request.form.get("password")

    if request.method == "POST":
        #new_member1 = Members_info(email="fgehfkshfsd@fsd.com", first_name=firstname, last_name=lastname, phone_number=phone, birthday="2000-01-01", gender=gender, membership_type_id=membership_type, duration_group=1, role_id=4)
        # db.session.add(new_member1)
        # db.session.commit()
        update_statement = "Application has been sent. You can now login."
        return render_template("create_account.html",
                               firstname=firstname,
                               lastname=lastname,
                               gender=gender,
                               phone=phone,
                               membership_type=membership_type,
                               #sport = sport,
                               birthdate=birthdate,
                               email=email,
                               password=password,
                               update_statement=update_statement,
                               nav_string=nav_string)


# reset password
@app.route('/resetpassword')
def reset_password():
    return render_template("reset_password.html", nav_string=nav_string)


@app.route('/resetpassword', methods=["POST"])
def really_reset_password():
    email = request.form.get("email")
    password = request.form.get("old_password")
    new_password = request.form.get("new_password")

    error_statement = ""
    exists = db.session.query(db.exists().where(
        Members.email == email)).scalar()

    if not email or not password or not new_password:
        error_statement = "Please fill in missing fields"
        return render_template("reset_password.html",
                               email=email,
                               password=password,
                               error_statement=error_statement,
                               nav_string=nav_string)
    elif exists == True:
        user = db.session.query(Members).filter_by(email=email).first()
        user_info = db.session.query(
            Members_info).filter_by(email=email).first()
        if user.pw == password:
            # DB connection
            session["user_id"] = user_info.member_id
            user_id = session["user_id"]
            user_info_data = db.session.query(
                Members_info).filter_by(member_id=user_id).first()
            user_data = db.session.query(Members).filter_by(
                email=user_info_data.email).first()

            nachricht = session["user_id"]
            logged_in = True

            if request.method == "POST":
                user_data.pw = new_password
                db.session.commit()
                return render_template("welcome.html", nachricht=nachricht, nav_string=nav_string)
        else:
            error_statement = "Wrong email or password"
            return render_template("reset_password.html",
                                   email=email,
                                   password=password,
                                   error_statement=error_statement,
                                   nav_string=nav_string)
    else:
        error_statement = "Wrong email or password"
        return render_template("reset_password.html",
                               email=email,
                               password=password,
                               error_statement=error_statement,
                               nav_string=nav_string)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
