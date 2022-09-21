user_db = {"name": "Sam Fisher",
           "balance": 5643,
           "deposit method": "credit card",
           "expiry date": "04/27"}  # this is meant to simulate an actual database with data entries for every user
# more data entries would be necessary for all the things we're going to want to do with this class/entity/model


class Balance():
    # properties include actual total, deposit method, validity of deposit method
    total = user_db["balance"]  # this would be fetching the data from an external database normally
    deposit_method = user_db["deposit method"] # as would this
    validity = False
    # to check for validity, we'd need the length of the card number,
    # read the expiry date and the 3 digit code at the back, and that's just for using credit cards
    if user_db["deposit method"] == "credit card":
        if len(user_db["deposit method"]) != 16:
            validity = False
        else:
            validity = True
