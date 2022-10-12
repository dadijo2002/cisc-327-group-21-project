from flask import Flask
from flask_sqlalchemy import SQLAlchemy

"""
This is an incomplete sample implementation of the Review system model for our
qBnB plan.
Group 21 - CISC 327
Author: Aniket Mukherjee
Student Number: 20245057
Date: October 3, 2022
"""

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Review(db.Model):  # making each property a column in the database
    """
    This class creates a Review object for use within our QB&B project
    Attributes:
        identification (Integer): This serves as the review id
        user_id (Integer): This serves as the user id
        listing_id (Integer): Serves as the id for the listing
        review_content(Str): Serves as the content of the review itself
        date(str): The date when the review was made

    """
    identification = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, primary_key=True)
    listing_id = db.Column(db.Integer, primary_key=True)
    review_content = db.Column(db.String(500), unique=True, nullable=False)
    date = db.Column(db.String(50), unique=False, nullable=False)

    def __init__(self, identification, user_id, listing_id,
                 review_content, date):
        """
        :param identification:
        :param user_id:
        :param listing_id:
        :param review_content:
        :param date:
        """
        # Initializes a review object with it's attributes

        self.identification = identification
        self.user_id = user_id
        self.listing_id = listing_id
        self.review_content = review_content
        self.date = date

    def validate(self):
        """
        :return Boolean:
        """
        # checking to see if the review is valid,
        # and none of the fields can't be accounted for
        if self.identification == "" or self.user_id == "" or \
                self.listing_id == "" or self.review_content == "" or \
                self.date == "":
            return False
        else:
            return True
