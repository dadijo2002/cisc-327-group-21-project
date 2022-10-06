import mysql.connector
import os
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

"""
R4-1: The title of the product has to be alphanumeric-only, and space allowed only if it is not as prefix and suffix.
R4-2: The title of the product is no longer than 80 characters.
R4-3: The description of the product can be arbitrary characters, with a minimum length of 20 characters and a maximum of 2000 characters.
R4-4: Description has to be longer than the product's title.
"""

"""
This is an incomplete sample implementation of some of the backend features for the listings class
Group 21 - CISC 327
Author: Aniket Mukherjee
Student Number: 20245057
Date: October 3, 2022
"""

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Listings(db.Model):  # SQLified the old Listings class a little bit
    host = db.Column(db.String(80), Unique=True, nullable=False)
    title = db.Column(db.String(80), unique=True, nullable=False)
    location = db.Column(db.String(120), unique=True, nullable=False)
    price_per_night = db.Column(db.Integer, primary_key=True)
    amenities = db.Column(db.String(120), unique=True, nullable=False)
    description = db.Column(db.String(2000), unique=True, nullable=False)
    availability = db.Column(db.String(10), unique=True, nullable=False)

    def title_check(self):
        # This serves to satisfy requirements R4-1 and R4-2
        if self.title.isalnum() and (self.title.find(" ") == 0 or self.title.find(" ") == self.username.length) and len(
                self.title) <= 80:
            return True
        else:
            return False

    def description_check(self):
        # this serves to satisfy requirements R4-3 and R4-4
        if len(self.description) < 20 or len(self.description) > 2000 or len(self.description) < len(self.title):
            return False
        else:
            return True
