from . import db

class client(db.Model):
    cid= db.Column(db.Integer,autoincrement = True, primary_key=True)
    contact = db.Column(db.Integer)
    first_name = db.Column(db.String(40))
    last_name = db.Column(db.String(40))
    trn = db.Column(db.Integer)
    address_1 = db.Column(db.String(60))
    address_2 = db.Column(db.String(60))
    city = db.Column(db.String(60))
    parish = db.Column(db.String(12))
    country= db.Column(db.String(10))
    date_created=db.Column(db.Date)
    username= db.Column(db.String(30),primary_key=True)
    
    def __init__(self,contact,first_name, last_name,trn,address_1,address_2,city,parish,country,date_created,username):
        # self.cid= cid
        self.contact = contact
        self.first_name= first_name
        self.last_name= last_name
        self.trn = trn
        self.address_1= address_1
        self.address_2 = address_2
        self.city = city
        self.parish = parish
        self.country= country
        self.date_created= date_created
        self.username=username
        
class product(db.Model):
    pid=  db.Column(db.Integer,autoincrement = True, primary_key=True)
    ordernum= db.Column(db.Integer)
    billno= db.Column(db.Integer)
    title = db.Column(db.String(50))
    descr= db.Column(db.String(70))
    status= db.Column(db.String(10))
    weight= db.Column(db.Integer)
    leng = db.Column(db.Integer)
    width = db.Column(db.Integer)
    height = db.Column(db.Integer)
    
    def __init__(self,ordernum,billno,title,descr,status,weight,leng,width,height):
        self.ordernum=ordernum
        self.billno=billno
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
    upload_date= db.Column(db.Date)
    ext= db.Column(db.String(5))
    
    def __init__(self,file_type,file_path,file_name,upload_date,ext):
        self.file_type= file_type
        self.file_path= file_path
        self.file_name= file_name
        self.upload_date= upload_date
        self.ext= ext
    

class invoice(db.Model):
    inid= db.Column(db.Integer,autoincrement=True, primary_key=True)
    trn= db.Column(db.Integer,primary_key=True)
    fid= db.Column(db.Integer,primary_key=True)
    ordernum= db.Column(db.Integer)
    
    def __init__(self,trn,fid,ordernum):
        self.trn= trn
        self.fid= fid
        self.ordernum= ordernum
        
# class assoc(db.Model):
#     pid=  db.Column(db.Integer,primary_key=True)
#     fid= db.Column(db.Integer,primary_key=True)
    
#     def __init__(self,pid,fid):
#         self.pid=pid
#         self.fid=fid
        
class auth(db.Model):
    __tablename__="auth"
    id= db.Column(db.Integer,autoincrement=True, primary_key=True)
    username= db.Column(db.String(30))
    password= db.Column(db.String(80))
    role= db.Column(db.String(300))
    
    def __init__(self,username,password,role):
        # self.id=id
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
        
    
    