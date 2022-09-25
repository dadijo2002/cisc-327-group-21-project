"""
This is an incomplete listings system for the qBnB plan.
Group 21 - CISC 327
Author: Yash Patel
Student Number: 20227432
Date: September 25, 2022
"""
# This block of code represents a simulation of a listing entry in a database
# I have read through the airbnb website and made a checklist of what
# could be included for the listing entries;
listing_db = {"Host": "Bob Dylan",
              "Title": "groovy Cottage",
              "Location": "Sault Ste. Marie, Ontario",
              "Price Per Night": 450,
              "Amount of Guests": 8,
              "Amenities": ["Wifi", "Kitchen", "TV", "Washer", "Dryer"],
              "Description": "A groovy cottage in Guelph, Ontario",
              "Availability": "1997-10-9 to 2024-12-12",  # Year | month | day!
              }


class listing:
    # Main listing class
    def __init__(self, host, title, location, price_per_night,
                 guests, amenities, description, availability):
        # Initialize the database jazz
        self.host = listing_db["Host"]
        self.title = listing_db["Title"]
        self.location = listing_db["Location"]
        self.price_per_night = listing_db["Price Per Night"]
        self.guests = listing_db["Amount of Guests"]
        self.amenities = listing_db["Amenities"]
        self.description = listing_db["Description"]
        self.availability = listing_db["Availability"]
        self.valid = False  # Default value is false for future error spotting

    def validate(self):
        """
        This Function will check if a listing is valid
        before adding it to the listing db.
        If something is left blank, it will return false
        as the listing is not valid. If all the fields
        are filled, it will return true, as it is a valid listing.
        """
        if self.host == "" or self.title == "" or self.location == "" or \
                self.price_per_night == "" or self.guests == "" or \
                self.amenities == "" or self.description == ""\
                or self.availability == "":
            return False
        else:
            return True

    def get_listing(self):
        """
        This Function will return the listing information
        of the listing that the user is looking at.
        """
        return self.host, self.title, self.location,\
            self.price_per_night,\
            self.guests, self.amenities,\
            self.description, self.availability

    def add_listing(self):
        """
        This Function will add a listing to the listing db.
        It will check if the inputted listing is valid,
        by calling the validate function,and if it
        returns true, it will add the listing to the listing db.

        THIS is not complete yet, todo: create a database using
        sql or mariadb or something.
        """
        if self.validate() is True:
            listing_db.append(self.host, self.title, self.location,
                              self.price_per_night,
                              self.guests, self.amenities,
                              self.description, self.availability)
            return True
        else:
            return False
