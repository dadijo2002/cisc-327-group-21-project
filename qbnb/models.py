"""
This program establishes the user/profile system for qBnb.
Last Updated: October 28, 2022
"""
from datetime import date
from qbnb import app

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, ForeignKey, Integer, Table
from sqlalchemy.orm import declarative_base, relationship
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
    postal_code = db.Column(db.String(6), nullable=False)
    balance = db.Column(db.Integer(), nullable=False)

    # Create database column for each user attribute

    listings = db.relationship('listing', backref='user')

    transaction = db.relationship('transaction', backref='user')

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
    id = db.Column(db.Integer, primary_key=True)
    host = db.Column(db.String(80), nullable=False)
    title = db.Column(db.String(80), unique=True, nullable=False, primary_key=True)
    location = db.Column(db.String(120), unique=True, nullable=False)
    guests = db.Column(db.Integer, nullable=False)
    price_per_night = db.Column(db.Integer, nullable=False)
    amenities = db.Column(db.String(120), nullable=False)
    description = db.Column(db.String(2000), nullable=False)
    availability = db.Column(db.String(10), nullable=False)
    # unavailability = db.Column(db.lis)
    last_modified_date = db.Column(db.String(50), nullable=False)
    owner_email = db.Column(db.String(120), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    transaction = db.relationship('transaction', backref='listing')

    def __repr__(self):
        return '<User %r>' % self.username

class Transaction(db.Model):
  
    id = db.Column(db.Integer, primary_key=True)
    start_date = db.Column(db.Integer, nullable=False)
    end_date = db.Column(db.Integer, nullable=False)

    renter_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    seller_id= db.Column(db.Integer, db.ForeignKey('user.id'))
    listing_id = db.Column(db.Integer, db.ForeignKey('listing.id'))

    # renter = db.relationship('renter', backref='user')
    # owner = db.relationship('owner', backref='user')
    # property = db.relationship('property', backref='listing')

#   def __init__(self, user, listing_info):
#     self.user = user # user specific info
#     self.username = user.username
#     self.balance = user.balance
#     self.unit_cost = listing_info.cost
#     self.unit_name = listing_info.name
#     self.unit_id = listing_info.id
#     self.seller_name = listing_info.seller
#     self.availability = listing_info.availability
#     self.validity = False
    # default is False so that errors can be recognized later if any exist

    # TODO: Figure out how to connect to other databases to get information,
    # remove user.x and listing_info.x and replace with database info

db.create_all()

def check_balance(user_balance, listing_price_per_night, number_of_nights):
    """
    This function ensures that the user's balance is great enough
    to afford the rental before the transaction goes through.
    """

    if user_balance >= (listing_price_per_night * number_of_nights):
      return True
    else:
      return False


def check_avail(self):
    """
    This function will reference a list of bookings once implemented
    to ensure that the property is available for rental on the selected
    dates.
    """

    if self.availability == True:
      self.validity = True
    else:
      self.validity = False
      # will later send an error that property isn't available on
      # selected date(s)

def check_dates(start_date, end_date):
    """
    This function checks the validity of the requested start and
    end dates of the rental as defined by the user.
    """
    
    todays_date = str(date.today())
    today = int(todays_date.replace("-", ""))
    
    thirty_days = [4, 6, 9, 11]
    thirtyone_days = [1, 3, 5, 7, 8, 10, 12]
    FEB = 2

    if  int(str(start_date)[:4]) <2021 or  int(str(end_date)[:4]> 2025):
        return False
    if start_date > end_date:
      # check the start date occurs before the end date
      return False
      # will later send an error saying invalid dates were chosen
    else:
      if len(str(start_date)) != 8 or len(str(end_date)) != 8:
        # check that the full dates were entered
        return False
        # will later send an error saying invalid dates were chosen

      elif start_date <= today:
        # check that the start date is in the future
        return False
        # will later send an error saying dates must be in the future

      elif (int(str(start_date)[4:6]) < 1 or
        int(str(start_date)[4:6]) > 12):
        # check that a valid month was used in both dates
        return False

      elif (int(str(start_date)[6:]) < 1 or
        int(str(start_date)[6:]) > 31):
        # check that a valid day was used in both dates
        # (more specific checks occur later)
        return False

      elif (int(str(end_date)[6:]) > int(str(start_date)[6:]) and
        int(str(end_date)[4:6]) == int(str(start_date)[4:6]) + 1):
        # ensure that end date is no more than 1 month after start date
        # (measured by day number, ex. Aug. 30 to Sep. 30 or
        # Apr. 19 to May 19 are valid)
        return False

      else:
        dates = [start_date, end_date]
        # loop to reduce code

        for day in dates:
          # ensure the month in the date has the correct number of days
          if int(str(day)[4:6]) in thirty_days:
            if int(str(day)[6:]) <= 30:
              return True
            else:
              return False
              return
          elif int(str(day)[4:6]) in thirtyone_days:
            if int(str(day)[6:]) <= 31:
              return True
            else:
              return False
          
          elif int(str(day)[4:6]) == FEB:
            # leap years only occur every 4th year except every 100 years when
            # the year is not divisible by 400 (ex. 1900 was not a leap year, but
            # 2000 was), so this block of code below detects whether or not the
            # valid time can accomodate a leap year
            if int(str(day)[0:4]) % 4 == 0:
              if int(str(day)[2:4]) == 0 and int(str(day)[0:4]) % 400 != 0:
                if int(str(day)[6:]) <= 28:
                  return True
                else:
                  return False
                  return
              else:
                if int(str(day)[6:]) <= 29:
                  return True
                else:
                  return False
                  return
            else:
              if int(str(day)[6:]) <= 28:
                return True
              else:
                return False
                
          else:
            return False
            # some other error occurred

def calc_number_of_nights(start_date,end_date):
    """
    Function calculates the number of days between the star date
    and end date.
    """
    thirty_days = [4, 6, 9, 11]
    thirtyone_days = [1, 3, 5, 7, 8, 10, 12]
    FEB = 2
    days=0

    # Save values of dates 
    start_year= int(str(start_date)[:4])
    end_year= int(str(end_date)[:4])
    start_month= int(str(start_date)[4:6])
    start_day = int(str(start_date)[6:])
    end_month = int(str(end_date)[4:6])
    end_day = int(str(end_date)[6:])
    
    if start_month == end_month: # Days in same month
        days= end_day - start_day 
    else: 
        # calculate days in start month
        if start_month in thirty_days:
            days = 30-start_day
        elif start_month in thirtyone_days:
            days = 31 - start_day
        elif start_month== FEB:
            if ((start_year % 4 == 0 and start_year % 100 != 0) or
                 (start_year % 100 == 0 and start_year % 400 != 0)):
                    days = 29 - start_day
            else:
                days = 28 - start_day
       
       # calculate days in end month 
        if end_month in thirty_days:
            days = days + end_day
        elif end_month in thirtyone_days:
            days = days + end_day
        elif end_month== FEB:
            if ((end_year % 4 == 0 and end_year % 100 != 0) or
                (end_year % 100 == 0 and end_year % 400 != 0)):
                days = days + end_day
            else:
                days = days + start_day
                
    return days
        
def no_scheduling_conflict(listing, start, end):
    """
    This function will look through the transactions in the tranactions
    table to see if any transactions for the given property have
    overlaping dates with the potential new booking dates. 
    """
    flag= True # defult is: no conflict 
    
    # thirty_days = [4, 6, 9, 11]
    # thirtyone_days = [1, 3, 5, 7, 8, 10, 12]
    # FEB = 2
    # days=0
    end_of_month= [131,228,331,430,531,630,731,831,930,1031,1130,1231]

    # Save values of dates 
    start_year= int(str(start)[:4])
    end_year= int(str(end)[:4])
    start_month= int(str(start)[4:6])
    start_day = int(str(start)[6:])
    end_month = int(str(end)[4:6])
    end_day = int(str(end)[6:])
    
    unavilable= Transaction.query.filter_by(listing_id = listing.id)
    for booking in unavilable:
        
        if (int(str(booking.start_date)[:4]) == start_year or
            int(str(booking.end_date)[:4]) == start_year or 
            int(str(booking.start_date)[:4]) == end_year or
            int(str(booking.end_date)[:4]) == end_year):
                # if booking and wanted time in the same years

            if (int(str(booking.start_date)[4:6]) == start_month or
            int(str(booking.end_date)[4:6]) == start_month or 
            int(str(booking.start_date)[4:6]) == end_month or
            int(str(booking.end_date)[4:6]) == end_month):
                # if booking and wanted time are in same months
                
                if (start_day==1 or ( int(str(end)[4:]) in end_of_month)):
                # if the booking starts on a 1 or ends on the last day of the month 
                    if ( not (int(str(booking.end_date)[4:6]) == start_month-1) and 
                         not (int(str(booking.start_date)[4:6]) == end_month +1)):
                    # if end date for wanted time is not before start
                    # date of booking or the start date for wanted
                    # time is not after the booking end date
                         flag = False # There is a conflict 
                
                elif(not (end_day < int(str(booking.start_date)[6:])) and 
                    not (start_day> int(str(booking.end_date)[6:]))):
                     # if the end date from the potential booking is
                     # not before the start date of a booking and the
                     # start date of the potential booking is not
                     # after the end of a booking 
                    flag= True # There is no conflict 
    return flag



def book_listing(user, listing, start_date, end_date):
    """
    This function confirms that booking is possible,
    then makes the booking.
    Parameters:
        user (User): user idenity
        listing (Listing): listing user wants to book
        start_date ()
    Returns:
        True if the booking is made successfully and false if the
        booking failed. 
    """
    # make sure listing does not belong to user
    if user == listing.user:
        return False
    
    # make sure given dates are vaild 
    vaild_dates = check_dates(start_date,end_date)
    if not vaild_dates:
        return False    
    
    # make sure user has big enough balance
    enough_funds= check_balance(user.balance, listing.price_per_night, 
                                calc_number_of_nights(start_date,end_date))
    if not enough_funds:
        return False
    
    # make sure listing is available for time period 
    if not no_scheduling_conflict(listing, start_date,end_date):
        return False
    
    # now that we know transaction request is valid, create transaction
    booking = Transaction(start_date = start_date, end_date=end_date,
                          renter_id = user.id, seller_id = listing.user_id,
                          listing_id= listing.id)
    
    # add it to the current database session 
    db.session.add(booking)
    # Actually save the booking object 
    db.session.commit()
    return True

    
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

    if verify_password(password) and verify_email(email):
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
            valid_email = validate_email(new_email).email
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

    if validate_username(username) == True:  # username vaild (r1-5, r1-6)
        if verify_password(password) == True:  # password vaild (r1-4)
            if verify_email(email) == True:  # email vaild (r1-3)
                # check if the email has been used: (r1-7)
                existed = User.query.filter_by(email=email).all()
                if len(existed) > 0:
                    return False

                # create a new user
                user = User(username=username, email=email, password=password,
                            billing_address=" ", postal_code=" ", balance=100)
                # add it to the current database session
                db.session.add(user)
                # actually save the user object
                db.session.commit()
                return True

    return False


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
            valid_email = validate_email(email).email
            email = valid_email["email"]
            return True
        except:
            return False


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
                     username.find(" ") == len(username)):
        return True
    else:
        return False


def title_check(self):
    """
    :return: a boolean value that determines whether the title
    of a listing is valid
    """
    # This serves to satisfy requirements R4-1 and R4-2
    if self.title.isalnum() and \
            (self.title.find(" ") == 0 or
             self.title.find(" ") == len(self.username)) \
            and len(self.title) <= 80:
        return True
    else:
        return False


def description_check(self):
    """
    :return: a boolean value that determines whether the discription
    of a listing is valid
    """
    # this serves to satisfy requirements R4-3, R4-4
    if len(self.description) < 20 or len(self.description) > 2000 or \
            len(self.description) < len(self.title):
        return False
    else:
        return True


# R4-5: Price has to be of range [10, 10000]
def price_validation(self):
    """
    :return: a boolean value that determines whether the price
    of a listing is valid
    """
    # checking to see if the price is valid
    if self.price < 10 or self.price > 10000:
        return False
    else:
        return True

    # R4-6: Last_modified_date must be after 2021-01-02 and before 2025-01-02


def date_validation(self):
    """
    :return: a boolean value that determines whether the date
    of a listing is valid
    """
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
    """
    :return: a boolean value that determines whether the title
    of a listing is has been used before
    """
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



"""
def update_listing(listing, host, title, location, price_per_night, guests, amenities, description, availability):
    '''
    This Function will add a listing to the listing db.
    It will check if the inputted listing is valid,
    by calling the validate function,and if it
    returns true, it will add the listing to the listing db.
    '''

    if validate(host, title, location, price_per_night, guests, amenities, description, availability) is True:
        db.Model.append(host, title, location,
                        price_per_night,
                        guests, amenities,
                        description, availability)
        return True
    else:
        return False

# TODO: change so it updates listing
# add ID system for listings?

"""
