from app import db
from datetime import datetime


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    posts=db.relationship('Post',backref='author',lazy='dynamic')
    #the posts is a high level view of the relation bw the user and post , it is not the exact datafield
    

    def __repr__(self):
        return '<User {}>'.format(self.username)  #for debug purpose

class Post(db.Model):
	id=db.Column(db.Integer,primary_key=True)
	body=db.Column(db.String(140))
	timestamp=db.Column(db.DateTime,index=True,default=datetime.utcnow)
	user_id=db.Column(db.Integer,db.ForeignKey('user.id'))

	def __repr__(self):
		return '<Post {}>'.format(self.body)