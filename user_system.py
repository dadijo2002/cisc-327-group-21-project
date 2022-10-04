"""
# Description
Adding billing address and postal code attributes to the user class.
Making the user class compatible to SQL.


Author: Makayla McMullin
Fixes # 2

## Type of change

Please delete options that are not relevant.

- [ ] New feature (non-breaking change which adds functionality)
- [ ] This change requires a documentation update


# Checklist:

- [x] My code follows the style guidelines of this project (PEP 8)
- [x] I have performed a self-review of my own code
- [x] I have commented my code, particularly in hard-to-understand areas
- [x] My changes generate no new warnings
- [x] Any dependent changes have been merged and published in downstream modules

"""
import os
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy


from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
# ^ need to decide what database we connect to?
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class User(db.Model):
    """This class initializes the user data base"""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=True, nullable=False)
    billing_address=db.Column(db.String(120), unique=True, nullable=False)
    postal_code= db.Column(db.String(6), unique=True, nullable=False)
    balance =  db.Column(db.String(10), unique=True, nullable=False)
    # Create database column for each user attribute 

    listings = db.relationship('listing', backref='user')
    bookings = db.relationship('booking', backref='user')
    # Make realationship with listings and booking databases 
    # TODO: ensure listing and booking databases have crresponding code


    def __repr__(self):
        return '<User %r>' % self.username




