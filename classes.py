from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request



app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Log_Pas.db'
db = SQLAlchemy(app)


class Register(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(300), nullable=False)
    password = db.Column(db.String(300), nullable=False)
