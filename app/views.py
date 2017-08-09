from app import app,db,login_manager
from flask import request, redirect, url_for, flash,jsonify, make_response
from flask_login import login_user, logout_user, current_user, login_required
from models import *

@app.route("/login",methods=["POST"])
def login():
    if request.method== "POST":
        username= request.form['username']
        password= request.form['password']
        #Query
        user= auth.query.filter_by(username=username, password= password).first()
        if user == None:
            message= "Login Fail"
            error= "Incorrect username or password"
            login= False
            resp={"login":login, "message":message, "error": error}
            return jsonify(resp)
        else:
            login_user(user)
            message= "success"
            error= None
            login=True
            resp={"login":login, "message":message, "error": error}
            print user.id
            print user.role
            return jsonify(resp)
        
@login_manager.user_loader
def load_user(id):
    return auth.query.get(int(id))
    
@app.route("/logout",methods=["POST"])
def logout():
    if request.method== "POST":
        if current_user.is_authenticated:
            logout_user()
            message= "logout successful"
            error= None
            login= False
            resp={"login":login, "message":message, "error": error}
            return jsonify(resp) 
        else:
            message= None
            error= "User not logged in"
            login= False
            resp={"login":login, "message":message, "error": error}
            return jsonify(resp) 
 
@app.route("/create_account",methods=["POST"])
def new_acc():
    if request.method=="POST":
        first_name= request.form['first_name']
        last_name= request.form["last_name"]
        contact= request.form["contact"]
        trn= request.form["trn"]
        address_1 = request.form["address_1"]
        address_2= request.form["address_2"]
        city= request.form["city"]
        parish= request.form["parish"]
        country= request.form["country"]
        date_created= request.form["date_created"]
        username= request.form["username"]
        password= request.form["password"]
        role= "client"
        try:
            newClient= client(contact,first_name, last_name,trn,address_1,address_2,city,parish,country,date_created,username)
            db.session.add(newClient)
            newAuth= auth(username,password,role)
            db.session.add(newAuth)
            db.session.commit()
            message= "success"
            error= None
            data= [{"first_name":first_name, "last_name":last_name, "username": username}]
            resp={"data":data, "message":message, "error": error}
            return jsonify(resp)
        except:
            message= "Account not created"
            error= "Fail"
            data= None
            resp={"data":data, "message":message, "error": error}
            return jsonify(resp)
            
