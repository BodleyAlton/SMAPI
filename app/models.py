from . import db

class client(db.Model):
    cid= db.Column(db.Integer,autoincrement = True, primary_key=True)
    contact = db.Column(db.Integer)
    first_name = db.Column(db.String(40))
    last_name = db.Column(db.String(40))
    address_1 = db.Column(db.String(60))
    address_2 = db.Column(db.String(60))
    city = db.Column(db.String(60))
    parish = db.Column(db.String(12))
    date_created=db.Column(db.Date)
    
    def __init__(self, cid,contact,first_name, last_name,address_1,address_2,city,parish,date_created):
        self.cid= cid
        self.contact = contact
        self.first_name= first_name
        self.last_name= last_name
        self.address_1= address_1
        self.address_2 = address_2
        self.city = city
        self.parish = parish
        self.date_created= date_created
        
class product(db.Model):
    pid=  db.Column(db.Integer,autoincrement = True, primary_key=True)
    title = db.Column(db.String(50))
    descr= db.Column(db.String(70))
    status= db.Column(db.String(10))
    weight= db.Column(db.decimal(4))
    leng = db.Column(db.decimal(5))
    width = db.Column(db.decimal(5))
    height = db.Column(db.decimal(5))
    
    def __init__(self,pid,title,descr,status,weight,leng,width,height):
        self.pid=pid
        self.title= title
        self.descr= descr
        self.status= status
        self.weight= weight
        self.leng= leng
        self.width= width
        self.height= height
        
class files(db.Model):
    fid=db.Column(db.Integer,autoincrement = True, primary_key=True)
    file_type= db.Column(db.String(5))
    file_path=db.Column(db.String(40))
    file_name= db.Column(db.String(30))
    
    def __init__(self,fid,file_type,file_path,file_name):
        self.fid=fid
        self.file_type= file_type
        self.file_path= file_path
        self.file_name= file_name
    

class own(db.Model):
    pid=  db.Column(db.Integer,primary_key=True)
    cid= db.Column(db.Integer,primary_key=True)
    
    def __init__(self, pid,cid):
        self.pid
        self.cid
        
class assoc(db.Model):
    pid=  db.Column(db.Integer,primary_key=True)
    fid= db.Column(db.Integer,primary_key=True)
    
    def __init__(self,pid,fid):
        self.pid=pid
        self.fid=fid
        
class auth(db.Model):
    id= db.Column(db.Integer,autoincrement=True)
    username= db.Column(db.String(30))
    password= db.Column(db.String(80))
    role= db.Column(db.String(300))
    
    def __init__(self, id,username,password,role):
        self.id=id
        self.username= username
        self.password= password
        self.role= role
    
    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support

    def __repr__(self):
        return '<User %r>' % (self.username)
        
    
    