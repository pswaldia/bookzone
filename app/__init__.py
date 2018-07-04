from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config   #this is an important part in any flask applications


app=Flask(__name__)
app.config.from_object(Config)    #this must be defined before instantiation of db and migrate

db=SQLAlchemy(app)
migrate=Migrate(app,db)





from app import routes,models