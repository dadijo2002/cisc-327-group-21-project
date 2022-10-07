
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


"""
This is an incomplete sample implementation of
some of the backend features for the listings class
Group 21 - CISC 327
Author: Aniket Mukherjee
Student Number: 20245057
Date: October 3, 2022
"""

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Listings(db.Model):
    """
    This class creates a Review object for use within our QB&B project
    Attributes:
        host (Integer): This serves as the review id
        title (Integer): This serves as the user id
        location (Integer): Serves as the id for the listing
        price_per_night (Str): Serves as the content of the review itself
        amenities(str): The date when the review was made
        description(Str): A description of the listing
        availability(Str): A string that says whether or
        not a listing is available

    """
    host = db.Column(db.String(80), unique=True, nullable=False)
    title = db.Column(db.String(80), unique=True, nullable=False)
    location = db.Column(db.String(120), unique=True, nullable=False)
    price_per_night = db.Column(db.Integer, primary_key=True)
    amenities = db.Column(db.String(120), unique=True, nullable=False)
    description = db.Column(db.String(2000), unique=True, nullable=False)
    availability = db.Column(db.String(10), unique=True, nullable=False)

    def title_check(self):
        """
        :return: a boolean value that determines whether the title is valid
        """
        # This serves to satisfy requirements R4-1 and R4-2
        if self.title.isalnum() and \
                (self.title.find(" ") == 0 or
                 self.title.find(" ") == self.username.length) \
                and len(self.title) <= 80:
            return True
        else:
            return False

    def description_check(self):
        """
        :return: a boolean value that determines whether
        the description is valid or not
        """
        # this serves to satisfy requirements R4-3 and R4-4
        if len(self.description) < 20 or len(self.description) > 2000\
                or len(self.description) < len(self.title):
            return False
        else:
            return True
