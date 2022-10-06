import mysql.connector
import os
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

"""
R1-5: User name has to be non-empty, alphanumeric-only, and space allowed only if it is not as the prefix or suffix.
R1-6: User name has to be longer than 2 characters and less than 20 characters.
R1-7: If the email has been used, the operation failed.
"""

"""
This is an incomplete sample implementation of some of the backend features for the user class
Group 21 - CISC 327
Author: Aniket Mukherjee
Student Number: 20245057
Date: October 3, 2022
"""
# setting up some flask and sqlalchemy functionality
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/user_database'
# ^^^ interfacing with a mySQL database I had already made before switching frameworks
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
user_db = mysql.connector.connect(host="localhost",
                                  user="root",
                                  password="Splinter_Ce11",
                                  database="user_database")


class User(db.Model):  # using Makayla's class definition
    """This class initializes the user data base"""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=True, nullable=False)
    billing_address = db.Column(db.String(120), unique=True, nullable=False)
    postal_code = db.Column(db.String(6), unique=True, nullable=False)
    balance = db.Column(db.String(10), unique=True, nullable=False)
    listings = db.relationship('listing', backref='user')
    bookings = db.relationship('booking', backref='user')

    def validate_username(self):
        # This function serves to satisfy requirements R1-5 and R1-6
        if self.username != "" and self.username.isalnum() and (self.username.find(" ") == 0
                                                                or self.username.find(" ") == self.username.length):
            return True
        else:
            return False

    def email_search(self, email):
        # this function serves to satisfy requirement R1-7
        for address in self.email:  # since email is defined as a column in the class definition,
            # we just need to iterate through that column and look for a match
            if address == email:
                return False
            else:
                return True
