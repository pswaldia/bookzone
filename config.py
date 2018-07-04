import os
basedir=os.path.abspath(os.path.dirname(__file__))

class Config(object):
	SECRET_KEY=	os.environ.get('SECRET_KEY') or "you-will-never-guess-that"
	SQLALCHEMY_DATABASE_URI=os.environ.get('DATABASE_URL') or 'sqlite///'+os.path.join(basedir,'app.db')
	#flask_sqlalchemy stores the application database location
	SQLACHEMY_TRACK_MODIFICATIONS=False 
    
