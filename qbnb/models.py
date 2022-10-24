"""
This program establishes the user/profile system for qBnb.
Last Updated: October 11, 2022
"""
# need to get register function in here too
import os
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from email_validator import validate_email, EmailNotValidError

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
    billing_address = db.Column(db.String(120), unique=True, nullable=False)
    postal_code = db.Column(db.String(6), unique=True, nullable=False)
    balance = db.Column(db.String(10), unique=True, nullable=False)
    # Create database column for each user attribute

    listings = db.relationship('listing', backref='user')
    bookings = db.relationship('booking', backref='user')

    # Make realationship with listings and booking databases
    # TODO: ensure listing and booking databases have crresponding code

    def __repr__(self):
        return '<User %r>' % self.username


def login(username, password):
    """
    This function validates username and password before login is
    completed.
    """
    # TODO: find some way to obscure passwords at login?

    # verify username format
    if len(username) != 0 and username.isalnum():
        # verify password format
        if verify_password(password):
            # if both user & pass are valid, check database for existing user
            result = User.query.filter_by(username=username).first()

            # if user is found, check that password matches for that user
            if result != None:

                if result.password == password:
                    print("Login successful! Welcome back, " + username + "!")

                else:
                    print("Incorrect password! Please try again.")

            else:
                print("Username not found!")

        else:
            print("Invalid password format!")

    elif (" " in username and username[0] != " " and
          username[-1] != " "):
        temp_user = username.replace(" ", "")

        # If no special characters other than space and format allowed
        # Check that no existing account already has this username
        if temp_user.isalnum():

            for char in password:
                if char.isupper():
                    caps_check += 1
                elif char.islower():
                    lower_check += 1
                elif char.isnumeric():
                    num_check += 1

            # verify password format
            if (len(password) >= 6 and password.isalnum() and caps_check >= 1 and
                    lower_check >= 1 and num_check >= 1):

                # if both user & pass are valid, check database for existing user
                result = User.query.filter_by(username=username).first()

                # if user is found, check that password matches for that user
                if result != None:

                    if result.password == password:
                        print("Login successful! Welcome back, " + username + "!")

                    else:
                        print("Incorrect password! Please try again.")

                else:
                    print("Username not found!")

            else:
                print("Invalid password format!")

        else:
            print("Invalid username format!")


def update_username(self):
    """
    This function updates the username of the user.
    """

    new_username = input("New Username: ")

    # Check for proper username format
    if len(new_username) != 0 and new_username.isalnum():

        # Check that no existing account already has this username
        result = User.query.filter_by(username=new_username).first()

        # Once validated, update username
        if result == None:
            self.username = new_username
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
                if result == None:
                    self.username = new_username
                    print("Username successfully updated!")
        else:
            print("Invalid username format!")


def update_email(self):
    """
    This function updates the email of the user.
    """

    new_email = input("New Email: ")

    # Check for proper email format
    if len(new_email) != 0:
        try:
            valid_email = validate_email(new_email)
            new_email = valid_email["email"]
        except:
            return EmailNotValidError

        # Check that no existing account already has this email address
        result = User.query.filter_by(email=new_email).first()

        # Once validated, update username
        if result == None:
            self.email = new_email
            print("Email successfully updated!")

        else:
            print("Email already associated with existing account!")

    else:
        print("Invalid email format!")


def update_address(self):
    """
    This function updates the billing address of the user.
    """
    new_address = input("New Address: ")

    # Check that an address has been entered
    if len(new_address) != 0:
        self.billing_address = new_address
        print("Address successfully updated!")
    else:
        print("Invalid address format!")


def update_postal_code(self):
    """
    This function updates the postal code of the user.
    """

    new_postal_code = input("New Postal Code: ")

    # Check for proper postal code format
    if len(new_postal_code) != 0 and new_postal_code.isalnum():

        # Once validated, update postal code
        if (new_postal_code[0] in "ABCEGHJKLMNPRSTVXY" and
                new_postal_code[1].isnumeric() and new_postal_code[3].isnumeric() and
                new_postal_code[5].isnumeric() and new_postal_code[2].isalpha() and
                new_postal_code[2].isalpha()):
            # Checks for valid province/region code and valid format (ex. A1A1A1)
            # TODO: Add more specific verification since not every
            # character/combination is used

            self.postal_code = new_postal_code
            print("Postal Code successfully updated!")
    else:
        print("Invalid postal code format!")


def register(username, email, password):
    '''
    Register a new user
      Parameters:
        name (string):     user name
        email (string):    user email
        password (string): user password
      Returns:
        True if registration succeeded otherwise False
    '''
    if validate_username: # username vaild (r1-5, r1-6)
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
            print("Invalid email format!")
            return


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

    for char in password:
        if char.isupper():
            caps_check += 1
        elif char.islower():
            lower_check += 1
        elif char.isnumeric():
            num_check += 1

    if (len(password) >= 6 and password.isalnum() and caps_check >= 1 and
            lower_check >= 1 and num_check >= 1):
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
