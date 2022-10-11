"""
This is an incomplete sample implementation of the transaction model for
our qBnb plan.

Group 21 - CISC 327
Last Modified Date: October 7, 2022
"""

# TODO: Reference a database (SQL) of all successful transactions
# TODO: Generate an ID for successful transactions based on
# this database

# TODO: Link the class with databases from other classes for full functionality

from datetime import date
import os
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
# ^ need to decide what database we connect to?
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
t_db = SQLAlchemy(app)

class Transaction:


  t_id = t_db.Column(t_db.Integer, primary_key=True)
  start_date = t_db.Column(t_db.Integer, nullable=False)
  end_date = t_db.Column(t_db.Integer, nullable=False)

  renter = t_db.relationship('renter', backref='user')
  seller = t_db.relationship('seller', backref='user')
  property = t_db.relationship('property', backref='listing')

  def __init__(self, user, listing_info):
    self.user = user # user specific info
    self.username = user.username
    self.balance = user.balance
    self.unit_cost = listing_info.cost
    self.unit_name = listing_info.name
    self.unit_id = listing_info.id
    self.seller_name = listing_info.seller
    self.availability = listing_info.availability
    self.validity = False
    # default is False so that errors can be recognized later if any exist

    # TODO: Figure out how to connect to other databases to get information,
    # remove user.x and listing_info.x and replace with database info

  def check_balance(self):
    """
    This function ensures that the user's balance is great enough
    to afford the rental before the transaction goes through.
    """

    if self.balance >= self.unit_cost:
      self.validity = True
    else:
      self.validity = False
      # will later send an error that user's balance is not high
      # enough to purchase

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

  def check_dates(self):
    """
    This function checks the validity of the requested start and
    end dates of the rental as defined by the user.
    """

    todays_date = str(date.today())
    today = int(todays_date.replace("-", ""))
    
    thirty_days = [4, 6, 9, 11]
    thirtyone_days = [1, 3, 5, 7, 8, 10, 12]
    FEB = 2

    if self.start_date > self.end_date:
      # check the start date occurs before the end date
      self.validity = False
      # will later send an error saying invalid dates were chosen
    else:
      if len(str(self.start_date)) != 8 or len(str(self.end_date)) != 8:
        # check that the full dates were entered
        self.validity = False
        # will later send an error saying invalid dates were chosen

      elif self.start_date <= today:
        # check that the start date is in the future
        self.validity = False
        # will later send an error saying dates must be in the future

      elif (int(str(self.start_date)[4:6]) < 1 or
        int(str(self.start_date)[4:6]) > 12):
        # check that a valid month was used in both dates
        self.validity = False

      elif (int(str(self.start_date)[6:]) < 1 or
        int(str(self.start_date)[6:]) > 31):
        # check that a valid day was used in both dates
        # (more specific checks occur later)
        self.validity = False

      elif (int(str(self.end_date)[6:]) > int(str(self.start_date)[6:]) and
        int(str(self.end_date)[4:6]) == int(str(self.start_date)[4:6]) + 1):
        # ensure that end date is no more than 1 month after start date
        # (measured by day number, ex. Aug. 30 to Sep. 30 or
        # Apr. 19 to May 19 are valid)
        self.validity = False

      else:
        dates = [self.start_date, self.end_date]
        # loop to reduce code

        for day in dates:
          # ensure the month in the date has the correct number of days
          if int(str(day)[4:6]) in thirty_days:
            if int(str(day)[6:]) <= 30:
              self.validity = True
            else:
              self.validity = False
              return
          elif int(str(day)[4:6]) in thirtyone_days:
            if int(str(day)[6:]) <= 31:
              self.validity = True
            else:
              self.validity = False
              return
          elif int(str(day)[4:6]) == FEB:
            # leap years only occur every 4th year except every 100 years when
            # the year is not divisible by 400 (ex. 1900 was not a leap year, but
            # 2000 was), so this block of code below detects whether or not the
            # valid time can accomodate a leap year
            if int(str(day)[0:4]) % 4 == 0:
              if int(str(day)[2:4]) == 0 and int(str(day)[0:4]) % 400 != 0:
                if int(str(day)[6:]) <= 28:
                  self.validity = True
                else:
                  self.validity = False
                  return
              else:
                if int(str(day)[6:]) <= 29:
                  self.validity = True
                else:
                  self.validity = False
                  return
            else:
              if int(str(day)[6:]) <= 28:
                self.validity = True
              else:
                self.validity = False
                return
          else:
            self.validity = False
            return
            # some other error occurred
      