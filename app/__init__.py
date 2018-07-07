from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config   #this is an important part in any flask applications
from flask_login import LoginManager


app=Flask(__name__)
app.config.from_object(Config)    #this must be defined before instantiation of db and migrate
login=LoginManager(app)    #adding instance of class LoginManager
db=SQLAlchemy(app)
migrate=Migrate(app,db)





from app import routes,models