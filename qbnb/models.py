"""
This program establishes the user/profile system for qBnb.
Last Updated: October 28, 2022
"""
from datetime import date
from qbnb import app

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from email_validator import validate_email, EmailNotValidError

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
# # ^ need to decide what database we connect to?
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class User(db.Model):
    """This class initializes the user data base"""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=True, nullable=False)
    billing_address = db.Column(db.String(120), unique=True, nullable=False)
    postal_code = db.Column(db.String(6), unique=True, nullable=False)
    balance = db.Column(db.Integer(), unique=True, nullable=False)

    # Create database column for each user attribute

    listings = db.relationship('listing', backref='user')

    # bookings = db.relationship('booking', backref='User')

    # Make relationship with listings and booking databases
    # TODO: ensure listing and booking databases have corresponding code


class listing(db.Model):
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
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<User %r>' % self.username


db.create_all()


def login(email, password):
    # TODO change to email
    """
    This function validates username and password before login is
    completed.

    Parameters:
        username (string): user name
        password (string): user password
    """
    # TODO: find some way to obscure passwords at login?

    if verify_password(password):
        result = User.query. \
            filter_by(email=email, password=password).all()

        # check to see if the search got precisely one result
        if len(result) != 1:
            print("User not found, maybe try to register first?")
            return None
        else:
            print("Login successful! Welcome back, " + email + "!")
            return result[0]


def update_username(new_username):
    """
    This function updates the username of the user.
    """

    # Check for proper username format
    if len(new_username) != 0 and new_username.isalnum():

        # Check that no existing account already has this username
        result = User.query.filter_by(username=new_username).first()

        # Once validated, update username
        if result is None:
            print("Username successfully updated!")

        else:
            print("Username already taken!")
    else:
        # factor in requirements about allowing spaces
        if (" " in new_username and new_username[0] != " " and
                new_username[-1] != " "):
            temp_user = new_username.replace(" ", "")

            # If no special characters other than space and format allowed
            # Check that no existing account already has this username
            if temp_user.isalnum():
                result = User.query.filter_by(username=new_username).first()

                # Once validated, update username
                if result is None:
                    print("Username successfully updated!")
        else:
            print("Invalid username format!")


def update_email(new_email):
    """
    This function updates the email of the user.
    """

    # Check for proper email format
    if len(new_email) != 0:
        try:
            valid_email = validate_email(new_email)
            new_email = valid_email["email"]

        except:
            print("Invalid email format!")
            return False

        # Check that no existing account already has this email address
        result = User.query.filter_by(email=new_email).first()

        # Once validated, update username
        if result is None:
            return True

        else:
            return False

    else:
        return False


def update_address(new_address):
    """
    This function updates the billing address of the user.
    """

    # Check that an address has been entered
    if len(new_address) != 0:
        return True
    else:
        return False


def update_postal_code(new_postal_code):
    """
    This function updates the postal code of the user.
    """

    # Check for proper postal code format
    if len(new_postal_code) != 0 and new_postal_code.isalnum():

        # Once validated, update postal code
        if (new_postal_code[0] in "ABCEGHJKLMNPRSTVXY" and
                new_postal_code[1].isnumeric() and
                new_postal_code[3].isnumeric() and
                new_postal_code[5].isnumeric() and
                new_postal_code[2].isalpha() and
                new_postal_code[2].isalpha()):
            # Checks for valid province/region code and valid format
            # TODO: Add more specific verification since not every
            # character/combination is used

            postal_code = new_postal_code
            return True
    else:
        return False


def validate(host, title, location, price_per_night, guests, amenities, description, availability):
    """
    This Function will check if a listing is valid
    before adding it to the listing db.
    If something is left blank, it will return false
    as the listing is not valid. If all the fields
    are filled, it will return true, as it is a valid listing.
    """
    if host == "" or title == "" or location == "" or \
            price_per_night == "" or guests == "" or \
            amenities == "" or description == "" \
            or availability == "":
        return False
    else:

        today = date.today()
        year_today = str(today)[0:4]
        month_today = str(today)[5:7]
        day_today = str(today)[8:]

        # ensure date is between/including Jan 3, 2021 and Jan 1, 2025
        # per R4-6 and R5-3
        if 2022 <= int(year_today) <= 2024:
            if 1 <= int(month_today) <= 12:
                if 1 <= int(day_today) <= 31:
                    last_modified_date = str(today)

        elif int(year_today) == 2021:

            if int(month_today) == 1:
                if 3 <= int(day_today) <= 31:
                    last_modified_date = str(today)

            elif 2 <= int(month_today) <= 12:
                if 1 <= int(day_today) <= 31:
                    last_modified_date = str(today)

        elif int(year_today) == 2025 and int(month_today) == 1 and int(day_today) == 1:
            last_modified_date = str(today)

        # listing modification is valid, return True
        return True


def register(username, email, password):
    """
    Register a new user
      Parameters:
        username (string):     user name
        email (string):    user email
        password (string): user password
      Returns:
        True if registration succeeded otherwise False

    """

    if validate_username:  # username vaild (r1-5, r1-6)
        if verify_password:  # password vaild (r1-4)
            if verify_email:  # email vaild (r1-3)
                # check if the email has been used: (r1-7)
                existed = User.query.filter_by(email=email).all()
                if len(existed) > 0:
                    return False

                # create a new user
                user = User(username=username, email=email, password=password,
                            billing_address="", postal_code="", balance=100)
                # add it to the current database session
                db.session.add(user)
                # actually save the user object
                db.session.commit()

    return True


def verify_email(email):
    """
    This function is used in the register and update_email functions to
    check that a given email is valid under RFC 5322 specifications.
    parameter: an email address
    return: boolean variable True if email address is vaild and False
            if not valid.
    """

    if len(email) != 0:
        try:
            valid_email = validate_email(email)
            email = valid_email["email"]
        except:
            EmailNotValidError


def verify_password(password):
    """
    This function is used in the register and login functions to check
    that a given password is vaild
    parameter: password
    return: boolean variable True if password is vaild and False if
            not valid.
    """

    caps_check = 0
    lower_check = 0
    num_check = 0
    special_check = 0

    for char in password:
        if char.isupper():
            caps_check += 1
        elif char.islower():
            lower_check += 1
        elif char.isnumeric():
            num_check += 1
        elif not char.isalnum():
            special_check += 1

    if (len(password) >= 6 and caps_check >= 1 and
            lower_check >= 1 and num_check >= 1 and special_check >= 1):
        return True
    else:
        return False


def validate_username(username):
    """
    :return: A boolean that determines if the username is valid or not
    """
    # This function serves to satisfy requirements R1-5 and R1-6
    if username != "" and username.isalnum() \
            and not (username.find(" ") == 0 or
                     username.find(" ") == username.length):
        return True
    else:
        return False


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


def add_listing(host, title, location, price_per_night, guests, amenities, description, availability):
    """
    This Function will add a listing to the listing db.
    It will check if the inputted listing is valid,
    by calling the validate function,and if it
    returns true, it will add the listing to the listing db.
    """

    if validate(host, title, location, price_per_night, guests, amenities, description, availability) is True:
        db.Model.append(host, title, location,
                        price_per_night,
                        guests, amenities,
                        description, availability)
        return True
    else:
        return False
