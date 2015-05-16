#!usr/bin/python

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__, static_url_path="")
db = SQLAlchemy(app)

class Base(db.Model):
    __abstract__ = True
    id = db.Column(db.Integer, primary_key=True)
