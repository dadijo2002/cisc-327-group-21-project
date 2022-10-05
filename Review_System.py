import mysql.connector
import os
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

"""
This is an incomplete sample implementation of the Review system model for our
qBnB plan.
Group 21 - CISC 327
Author: Aniket Mukherjee
Student Number: 20245057
Date: October 3, 2022
"""
# creating a mysql database to merge with SQLAlchemy code
review_db = mysql.connector.connect(host="localhost",
                                    user="root",
                                    password="Splinter_Ce11",
                                    database="review_database"

                                    )
review_cursor = review_db.cursor()

app = Flask(__name__)
# merging here
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/review_database'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Review(db.Model):  # making each property a column in the database
    identification = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, primary_key=True)
    listing_id = db.Column(db.Integer, primary_key=True)
    review_content = db.Column(db.String(500), Unique=True, nullable=False)
    date = db.Column(db.String(50), Unique=False, Nullable=False)

    def __init__(self, identification, user_id, listing_id, review_content, date):

        self.identification = identification
        self.user_id = user_id
        self.listing_id = listing_id
        self.review_content = review_content
        self.date = date

    def validate(self):
        # checking to see if the review is valid, and none of the fields can't be accounted for
        if self.identification == "" or self.user_id == "" or \
                self.listing_id == "" or self.review_content == "" or \
                self.date == "":
            return False
        else:
            return True
