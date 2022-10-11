
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

"""
R4-1: The title of the product has to be alphanumeric-only, and space allowed
 only if it is not as prefix and suffix.
R4-2: The title of the product no longer than 80 characters.
R4-3: The description of the product can be arbitrary characters,
 with a minimum length of 20 characters and a maximum of 2000 characters.
R4-4: Description has to be longer than the product's title.
"""

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
    last_modified_date = db.Column(db.String(50), unique=True, nullable=False)
    owner_email = db.Column(db.String(120), unique=True, nullable=False)

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
        # this serves to satisfy requirements R4-3, R4-4
        if len(self.description) < 20 or len(self.description) > 2000 or \
                len(self.description) < len(self.title):
            return False
        else:
            return True

    # R4-5: Price has to be of range [10, 10000]
    def price_validation(self):
        # checking to see if the price is valid
        if self.price < 10 or self.price > 10000:
            return False
        else:
            return True

    # R4-6: Last_modified_date must be after 2021-01-02 and before 2025-01-02

    def date_validation(self):
        # checking to see if the date is valid
        if self.last_modified_date < "2021-01-02" or \
                self.last_modified_date > "2025-01-02":
            return False
        else:
            return True

    # R4-7: owner_email cannot be empty. The owner of the corresponding
    # product must exist in the database
    def owner_email_validation(self):
        # checking to see if the owner email is valid
        if self.owner_email == "" or self.owner_email not in db.Model:
            return False
        else:
            return True

    # R4-8: A user cannot create products that have the same title
    def title_validation(self):
        # checking to see if the title is valid
        if self.title in db.Model:
            return False
        else:
            return True
