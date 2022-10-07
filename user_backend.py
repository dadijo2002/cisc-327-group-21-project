from flask import Flask
from flask_sqlalchemy import SQLAlchemy


"""
This is an incomplete sample implementation
of some of the backend features for the user class
Group 21 - CISC 327
Author: Aniket Mukherjee
Student Number: 20245057
Date: October 3, 2022
"""
# setting up some flask and sqlalchemy functionality
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class User(db.Model):
    """
        This class creates a Review object for use within our QB&B project
        Attributes:
            id (Integer): This serves as the user id
            username (Str): This serves as the user's username
            email (Str): Serves as the user's email
            password(Str): Serves as the user's password
            billing_address(str): The billing address of the user
            postal_code(str): the postal code of this user
            balance(Integer): the amount of money the user has in app
            listings(Listings): a listing object
            bookings(Bookings): a booking object

        """
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=True, nullable=False)
    billing_address = db.Column(db.String(120), unique=True, nullable=False)
    postal_code = db.Column(db.String(6), unique=True, nullable=False)
    balance = db.Column(db.Integer, unique=True, nullable=False)
    listings = db.relationship('listing', backref='user')
    bookings = db.relationship('booking', backref='user')

    def validate_username(self):
        """

        :return: A boolean that determines if the username is valid or not
        """
        # This function serves to satisfy requirements R1-5 and R1-6
        if self.username != "" and self.username.isalnum()\
                and (self.username.find(" ") == 0 or
                     self.username.find(" ") == self.username.length):
            return True
        else:
            return False

    def email_search(self, email):
        """

        :param email:
        :return: A boolean that determines if a
        specific email was found in the database
        """
        # this function serves to satisfy requirement R1-7
        for address in self.email:
            # since email is defined as a column in the class definition,
            # we just need to iterate through that column and look for a match
            if address == email:
                return False
            else:
                return True
