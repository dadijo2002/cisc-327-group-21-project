"""
This is an incomplete sample implementation of the Balance system model for our
qBnB plan.
Group 21 - CISC 327
Author: Aniket Mukherjee
Student Number: 20245057
Date: September 23, 2022
"""

user_db = {"name": "Sam Fisher",
           "balance": 5643,
           "deposit method": "credit card",
           "expiry date": "04/27"}
# this is meant to simulate an actual database with data entries for every user


# more data entries would be necessary
# will likely use an off-site sql database to store user balance data


class Balance:
    # properties include actual total, deposit method, validity of deposit method
    total = user_db["balance"]
    # this would be fetching the data from an external database normally
    deposit_method = user_db["deposit method"]  # as would this
    validity = False  # assume it's false until we run the validate function

    def __init__(self):  # initialization function
        total = self.total
        deposit_method = self.deposit_method
        validity = self.validity

    def validate(self):
        """
        This Function will serve as our way to check if a payment type or deposit method is valid before actually
        adding money to ones balance on the site
        """

        # to check for validity, we'd need the length of the card number,
        # read the expiry date and the 3 digit code at the back
        # and that's just for using credit cards
        if user_db["deposit method"] == "credit card":  # checking to see if the user chose to deposit via credit cards
            if len(user_db["deposit method"]) != 16 and user_db["expiry date"] != "04/27":
                # checking if the credit card number has enough digits
                # also need to check if the expiry date is of valid format
                return False
            else:
                return True
