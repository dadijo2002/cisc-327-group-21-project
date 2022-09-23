user_db = {"name": "Sam Fisher",
           "balance": 5643,
           "deposit method": "credit card",
           "expiry date": "04/27"}  # this is meant to simulate an actual database with data entries for every user


# more data entries would be necessary for all the things we're going to want to do with this class/entity/model
# will likely use an actual off-site sql database to store user balance data and pull stuff from there instead.


class Balance:
    # properties include actual total, deposit method, validity of deposit method
    total = user_db["balance"]  # this would be fetching the data from an external database normally
    deposit_method = user_db["deposit method"]  # as would this
    validity = False  # assume it's false until we run the validate function

    def __init__(self):  # initialization function
        total = self.total
        deposit_method = self.deposit_method
        validity = self.validity

    def validate(self):
        # to check for validity, we'd need the length of the card number,
        # read the expiry date and the 3 digit code at the back, and that's just for using credit cards
        if user_db["deposit method"] == "credit card":  # checking to see if the user chose to deposit via credit cards
            if len(user_db["deposit method"]) != 16 and user_db["expiry date"] != "04/27":
                # checking if the credit card number is long enough to be a valid credit card
                # also need to check if the expiry date is of valid format, was planning on doing that, just couldn't
                # quite remember how just yet
                return False
            else:
                return True
