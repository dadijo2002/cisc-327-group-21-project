"""
This is an incomplete sample implementation of the transaction model for
our qBnb plan.

Group 21 - CISC 327
Author: Daniel Dickson
Student Number: 20206675
Date: September 23, 2022
"""

# TODO: Reference a database (SQL) of all successful transactions
# TODO: Generate an ID for successful transactions based on
# this database

from datetime import date

user_db = {"name": "Felonius Gru",
                  "balance": 1000000.00}

transaction_db = {"unit cost": 1234.00,
                  "unit name": "Minion Beach",
                  "unit id": 16984,
                  "seller": "Bob the Minion",
                  "start date": 20220613,
                  "end date": 20220701,
                  "transaction id": 1,
                  "availability": True}
# this is an approximation of potential necessary values for a
# transaction, these values are not final: more may be added
# or some may be taken out in the final product

class Transaction:

  def __init__(self, user, transaction_info, name, balance, unit_cost,
               unit_name, unit_id, seller_name, start_date, end_date, transaction_id,
               availability, validity):
    self.user = user_db # user specific info
    self.transaction_info = transaction_db
    # transaction & property specific info
    self.name = user_db["name"]
    self.balance = user_db["balance"]
    self.unit_cost = transaction_db["unit cost"]
    self.unit_name = transaction_db["unit name"]
    self.unit_id = transaction_db["unit id"]
    self.seller_name = transaction_db["seller name"]
    self.start_date = transaction_db["start date"]
    self.end_date = transaction_db["end date"]
    self.transaction_id = transaction_db["transaction id"]
    self.availability = transaction_db["availability"]
    self.validity = False
    # default is False so that errors can be recognized later if any exist

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

    today_temp = str(date.today())
    today = int(today_temp.replace("-", ""))
    
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
            if int(str(date)[0:4]) % 4 == 0:
              if int(str(date)[2:4]) == 0 and int(str(date)[0:4]) % 400 != 0:
                if int(str(date)[6:]) <= 28:
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
      