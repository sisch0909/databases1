#!/usr/bin/env python
from flask import Flask, render_template, request, redirect, session
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.automap import automap_base
from pandas import pandas as pd
from datetime import datetime, date
import psycopg2
from time import sleep

app = Flask(__name__)

# DB connection
retries_left = 200
while retries_left > 0:
    try:
        app.config["SECRET_KEY"] = "qwertyuiop"
        app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:securepwd@db:5432/postgres"
        retries_left = 0
    except:
        retries_left = retries_left - 1
        sleep(5)

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
Members_sports = Base.classes.members_sports

# For string in navbar
logged_in = False
nav_string = "My personal data"
log_string = "Login"
log_bool = True

# Home
@app.route('/')
def home():
    global logged_in
    global nav_string
    global log_string
    global log_bool
    return render_template("home.html",
                            nav_string=nav_string,
                            log_string=log_string,
                            log_bool=log_bool)


# Loginpage
@app.route('/login')
def login():
    global logged_in
    global nav_string
    global log_string
    log_bool = False
    return render_template("login.html", 
                            nav_string=nav_string,
                            log_string=log_string,
                            log_bool=log_bool)


@app.route('/login', methods=["POST"])
def loginpage():
    global logged_in
    global nav_string
    global log_string
    global log_bool
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
                                nav_string=nav_string,
                                log_string=log_string,
                                log_bool=log_bool)
    elif exists == True:
        user = db.session.query(Members).filter_by(email=email).first()
        user_info = db.session.query(
            Members_info).filter_by(email=email).first()
        if user.pw == password:
            session["user_id"] = user_info.member_id
            user_id = session["user_id"]
            user_data = db.session.query(Members_info).filter_by(member_id=user_id).first()
            logged_in = True
            nav_string = user_data.first_name + " " + user_data.last_name
            log_string = "Logout"
            return render_template("welcome.html", 
                                    nav_string=nav_string,
                                    user_data=user_data,
                                    log_string=log_string,
                                    log_bool=log_bool)
        else:
            error_statement = "Wrong email or password"
            return render_template("login.html",
                                    email=email,
                                    password=password,
                                    error_statement=error_statement,
                                    nav_string=nav_string,
                                    log_string=log_string,
                                    log_bool=log_bool)
    else:
        error_statement = "Wrong email or password"
        return render_template("login.html",
                                email=email,
                                password=password,
                                error_statement=error_statement,
                                nav_string=nav_string,
                                log_string=log_string,
                                log_bool=log_bool)


# Logout
@app.route('/', methods=["POST"])
def logout():
    session.clear()
    global logged_in
    global nav_string
    global log_string
    log_bool = False
    logged_in = False
    log_string = "Login"
    nav_string = "My personal data"
    return render_template("login.html", 
                            nav_string=nav_string,
                            log_string=log_string,
                            log_bool=log_bool)


# View data
@app.route('/view')
def view():
    global logged_in
    global nav_string
    global log_string
    global log_bool

    #Users can't view or edit any data if they are not logged in
    if logged_in == False:
        return render_template("not_logged_in.html", 
                                nav_string=nav_string,
                                log_string=log_string,
                                log_bool=log_bool)
    
    user_id = session["user_id"]
    user_data = db.session.query(Members_info).filter_by(member_id=user_id).first()
    role_data = db.session.query(Roles).filter_by(role_id=user_data.role_id).first()
    age_group_data = db.session.query(Age_groups).filter_by(age_group_id=user_data.age_group_id).first()
    duration_group_data = db.session.query(Duration_groups).filter_by(duration_group_id=user_data.duration_group_id).first()
    membership_data = db.session.query(Memberships).filter_by(membership_type_id=user_data.membership_type_id).first()

    user_sports_query = db.session.query(Members_sports).filter_by(member_id=user_id).all()
    user_sports =[]
    user_sports_professionalism =[]
    for i in user_sports_query:
        sports_query = db.session.query(Sports).filter_by(sport_id=i.sport_id).first()
        user_sports.append(sports_query.sport_name)
        user_sports_professionalism.append(sports_query.professionalism_id)
    
    sports="0"

    if len(user_sports)==0:
        pass
    else:
        sports = user_sports[0]
        a = 1
        while len(user_sports) - a > 0:
            sports = sports + ", " + user_sports[a]
            a += 1   

    professional = False
    for i in range(len(user_sports_professionalism)):
        if user_sports_professionalism[i] == 1:
            professional = True
            break
    
    if professional == True:
        professionalism_query = db.session.query(Professionalisms).filter_by(professionalism_id=1).first()
    else:
        professionalism_query = db.session.query(Professionalisms).filter_by(professionalism_id=2).first()
    
    professionalism_discount = professionalism_query.discount
    age_group_discount = age_group_data.discount
    duration_group_discount = duration_group_data.discount
    original_price = membership_data.price

    price = int(original_price - original_price*(professionalism_discount*0.01 + age_group_discount*0.01 + duration_group_discount*0.01))
    original_price = int(original_price)


    return render_template("view.html", 
                            user_data=user_data, 
                            sports=sports,
                            original_price=original_price,
                            price = price,
                            professionalism_discount = professionalism_discount,
                            age_group_data = age_group_data,
                            duration_group_data = duration_group_data,
                            role_data = role_data,
                            membership_data = membership_data, 
                            nav_string=nav_string,
                            log_string=log_string,
                            log_bool=log_bool)


# edit data
@app.route('/edit', methods=["POST"])
def update_data():
    global logged_in
    global nav_string
    global log_string
    global log_bool
    
    user_id = session["user_id"]
    user_info_data = db.session.query(Members_info).filter_by(member_id=user_id).first()
    user_data = db.session.query(Members).filter_by(email = user_info_data.email).first()

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
                                    user_info_data=user_info_data,
                                    nav_string=nav_string,
                                    log_string=log_string,
                                    log_bool=log_bool)
        elif request.form.get("delete"):
            user_id = session["user_id"]
            user_query = db.session.query(Members_info).filter_by(member_id=user_id).first()
            user_email = user_query.email
            db.session.query(Members).filter_by(email=user_email).delete()
            db.session.query(Members_info).filter_by(member_id=user_id).delete()
            db.session.query(Members_sports).filter_by(member_id=user_id).delete()
            db.session.commit()

            logged_in = False
            log_string = "Login"
            nav_string = "My personal data"

            update_statement = "Your account has succesfully been deleted!"
            return render_template("home.html",
                                    update_statement=update_statement,
                                    nav_string=nav_string,
                                    log_string=log_string,
                                    log_bool=log_bool)

    return render_template("edit.html",
                            nav_string=nav_string, 
                            user_info_data=user_info_data,
                            log_string=log_string,
                            log_bool=log_bool)


@app.route('/edit', methods=['POST', 'GET'])
def edit():
    global logged_in
    global nav_string
    global log_string
    global log_bool

    #Users can't view or edit any data if they are not logged in
    if logged_in == False:
        return render_template("not_logged_in.html", 
                                nav_string=nav_string,
                                log_string=log_string,
                                log_bool=log_bool)

    user_id = session["user_id"]
    user_info_data = db.session.query(
        Members_info).filter_by(member_id=user_id).first()
    return render_template("edit.html", 
                            user_info_data=user_info_data, 
                            nav_string=nav_string,
                            log_string=log_string,
                            log_bool=log_bool)


# Create new account
@app.route('/createaccount')
def create_account():
    global logged_in
    global nav_string
    global log_string
    global log_bool
    sports = []
    return render_template("create_account.html", 
                            sports=sports, 
                            nav_string=nav_string,
                            log_string=log_string,
                            log_bool=log_bool)


@app.route('/createaccount', methods=["POST"])
def really_create_account():
    global logged_in
    global nav_string
    global log_string
    global log_bool
    firstname = request.form.get("firstname")
    lastname = request.form.get("lastname")
    gender = request.form.get("gender")
    phone = request.form.get("phone")
    membership_type = request.form.get("membership_type")
    birthdate = request.form.get("birthdate")
    email = request.form.get("email")
    password = request.form.get("password")

    date_time_obj = datetime. strptime(birthdate, '%Y-%m-%d')
    date_time_obj = date_time_obj.date()
    time_difference = date.today() - date_time_obj
    age_days = time_difference.days
    age = age_days / 365
    if age <= 12:
        age_group_id = 1
    elif age > 12 and age <=19:
        age_group_id = 2
    elif age >19 and age <= 65:
        age_group_id = 3
    else:
        age_group_id = 4


    #getting picked sports
    sports = []
    if request.form.get("2") == "2":
        sports.append(2)
    if request.form.get("4") == "4":
        sports.append(4)
    if request.form.get("6") == "6":
        sports.append(6)
    if request.form.get("8") == "8":
        sports.append(8)
    if request.form.get("10") == "10":
        sports.append(10)
    if request.form.get("12") == "12":
        sports.append(12)

    error_statement = ""
    update_statement = ""
    exists = db.session.query(db.exists().where(Members.email == email)).scalar()

    if request.method == "POST":
        if not firstname or not lastname or not gender or not phone or not membership_type or not birthdate or not email or not password or len(sports)==0:
            error_statement = "Please fill in missing fields"
        elif exists == True:
            error_statement = "This email is already in use."
        else:
            new_member1 = Members_info(email=email, first_name=firstname, last_name=lastname, phone_number=phone, birthday=birthdate, gender=gender, membership_type_id=membership_type, duration_group_id=1, role_id=3, age_group_id=age_group_id)
            new_member2 = Members(email=email, pw=password)
            db.session.add(new_member1)
            db.session.add(new_member2)
            db.session.commit()
            new_member_query = db.session.query(Members_info).filter_by(email=email).first()
            new_member_id = new_member_query.member_id

            for sport in sports:
                new_members_sports = Members_sports(member_id=new_member_id, sport_id=sport)
                db.session.add(new_members_sports)
                db.session.commit()
            

            update_statement = "Application has been sent. You can now login."
        return render_template("create_account.html",
                                firstname=firstname,
                                lastname=lastname,
                                gender=gender,
                                phone=phone,
                                membership_type=membership_type,
                                sports = sports,
                                birthdate=birthdate,
                                email=email,
                                password=password,
                                update_statement=update_statement,
                                error_statement=error_statement,
                                nav_string=nav_string,
                                log_string=log_string,
                                log_bool=log_bool)


# reset password
@app.route('/resetpassword')
def reset_password():
    global logged_in
    global nav_string
    global log_string
    global log_bool
    return render_template("reset_password.html", 
                            nav_string=nav_string,
                            log_string=log_string,
                            log_bool=log_bool)


@app.route('/resetpassword', methods=["POST"])
def really_reset_password():
    global logged_in
    global nav_string
    global log_string
    global log_bool
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
                                nav_string=nav_string,
                                log_string=log_string,
                                log_bool=log_bool)
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
            logged_in = True

            if request.method == "POST":
                user_data.pw = new_password
                db.session.commit()
                logged_in = True
                nav_string = user_info.first_name + " " + user_info.last_name
                log_string = "Logout"
                return render_template("welcome.html", 
                                        nav_string=nav_string, 
                                        log_string=log_string,
                                        log_bool=log_bool,
                                        user_data=user_info)
        else:
            error_statement = "Wrong email or password"
            return render_template("reset_password.html",
                                    email=email,
                                    password=password,
                                    error_statement=error_statement,
                                    nav_string=nav_string, 
                                    log_string=log_string,
                                    log_bool=log_bool)
    else:
        error_statement = "Wrong email or password"
        return render_template("reset_password.html",
                                email=email,
                                password=password,
                                error_statement=error_statement,
                                nav_string=nav_string,
                                log_string=log_string,
                                log_bool=log_bool)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)