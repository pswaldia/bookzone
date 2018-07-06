from app import db
from app import login
from datetime import datetime
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin  #this helps in implementing the flask_login methods easily

class User(UserMixin,db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    posts=db.relationship('Post',backref='author',lazy='dynamic')
    #the posts is a high level view of the relation bw the user and post , it is not the exact datafield
    

    def __repr__(self):
        return '<User {}>'.format(self.username)  #for debug purpose

    
    def set_password(self,password):
        self.password_hash=generate_password_hash(password)

    def check_password(self,password):
        return check_password_hash(self.password_hash,password)
#the user_loader decorator helps in loading the user , the id that flask_login pass to the function
#it then query the database to return the user object by id.
@login.user_loader
def load_user(id):
    return User.query.get(int(id))



class Post(db.Model):
	id=db.Column(db.Integer,primary_key=True)
	body=db.Column(db.String(140))
	timestamp=db.Column(db.DateTime,index=True,default=datetime.utcnow)
	user_id=db.Column(db.Integer,db.ForeignKey('user.id'))

	def __repr__(self):
		return '<Post {}>'.format(self.body)