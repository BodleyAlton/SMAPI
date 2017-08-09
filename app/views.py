from app import app,db,login_manager
from sqlalchemy import func
from flask import request, redirect, url_for, flash,jsonify, make_response
from flask_login import login_user, logout_user, current_user, login_required
from models import *
import os,time

def date():
    return time.strftime ("%m-%d-%Y")
    
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
            
@app.route("/invoice_upload", methods=["POST"])
def file_upload():
    spath = "./app/static/clients/"
    rpath= "/static/clients/"
    if request.method=="POST":
        file_name= request.form["file_name"]
        orderNum= request.form["orderNum"]
        file= request.files["invoice"]
        ext= request.form["ext"]
        upload_date= date()
        print current_user.username
        print "CURRENT USER"
        user= current_user.username 
        if os.path.exists(spath+user):
            if os.path.exists(spath+user+"/"+file.name):
               file.save(spath+user+"/"+file.name+"/"+file.name+"-"+orderNum+"."+ext)
            else:
                os.makedirs(spath+user+"/"+file.name)
                file.save(spath+user+"/"+file.name+"/"+file.name+"-"+orderNum+"."+ext)
        else:
            os.makedirs(spath+user)
            os.makedirs(spath+user+"/"+file.name)
            file.save(spath+user+"/"+file.name+"/"+file.name+"-"+orderNum+"."+ext)
        file_path= rpath+user+"/"+file.name+"/"+file.name+"-"+orderNum+"."+ext
        print current_user.username
        print "CURRENT USER"
        trn_search= db.session.query(client.trn).filter_by(username=current_user.username).first()
        print "TRN"
        print trn_search.trn
        trn=trn_search.trn
        maxfid= db.session.query(func.max(files.fid)).all()
        for i in maxfid:
            print i[0]
            if i[0]==None:
                fid=0
            else:
                fid=i[0]
            print fid
        print "ORDER"
        print orderNum
        newInv= invoice(trn,fid+1,orderNum)
        newFile= files(file.name,file_path,file_name,upload_date,ext)
        billNo=None
        title=None
        descr=None
        status=None
        weight=None
        leng=None
        width=None
        height=None
        newProduct= product(orderNum,billNo,title,descr,status,weight,leng,width,height)
        
        
        db.session.add(newFile)
        db.session.commit()
        db.session.add(newInv)
        db.session.commit()
        db.session.add(newProduct)
        db.session.commit()
        
       
        
        message= "success"
        error= None
        data= [{"file name":file.name+"-"+orderNum, "orderNum":orderNum, "idname": file_name,"ext":ext, "date":upload_date,"user":current_user.username}]
        resp={"data":data, "message":message, "error": error}
        return jsonify(resp)