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
   