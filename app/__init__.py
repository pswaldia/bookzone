from flask import Flask 
from flask_sqlalchemy import SQLALchemy
from flask_migrate import Migrate

app=Flask(__name__)

db=SQLALchemy(app)

migrate=Migrate(app,db)

from config import Config   #this is an important part in any flask applications

app.config.from_object(Config)

from app import routes,models