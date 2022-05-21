import math
from flask_sqlalchemy import SQLAlchemy 
import os
from flask import Flask
#database 
basedir = os.path.abspath(os.path.dirname(__file__))  
app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///'+os.path.join(basedir, 'sport.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
bd = SQLAlchemy(app)
app.config['SECRET_KEY'] = 'WEG@^$^YWH#UQ@#YH#'

class Cup(bd.Model):
    __tablename__ = 'cups'
    year =bd.Column(bd.String(4), primary_key=True,unique=True)
    tname = bd.Column(bd.String, bd.ForeignKey('teams.name'))

class Team(bd.Model):
    __tablename__ = 'teams'
    name = bd.Column(bd.String(64), primary_key=True,unique=True)
    logo = bd.Column(bd.String(60))
    cups = bd.relationship( 'Cup', backref='team', lazy=True)    
#end of data base
class User(bd.Model):
    __tablename__ = 'users_data'
    username = bd.Column(bd.String(64), primary_key=True,unique=True)
    password=bd.Column(bd.String(64),nullable=False)
    email = bd.Column(bd.String(120))