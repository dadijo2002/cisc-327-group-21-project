"""
This is an incomplete listings 
system for the qBnB plan.
Group 21 - CISC 327
Author: Yash Patel
Student Number: 20227432
Date: September 25, 2022
"""

from datetime import date

# This block of code represents a simulation of a listing entry in a database
# I have read through the airbnb website and made a checklist of what
# could be included for the listing entries;
listing_db = {"Host": "Bob Dylan",
              "Title": "groovy Cottage",
              "Location": "Sault Ste. Marie, Ontario",
              "Price Per Night": 450,
              "Amount of Guests": 8,
              "Amenities": ["Wi-fi", "Kitchen", "TV", "Washer", "Dryer"],
              "Description": "A groovy cottage in Guelph, Ontario",
              "Availability": "2021-01-03 to 2024-12-12",  # Year | month | day!
              "Last Modified Date": "2021-01-03" # default value
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
        self.last_modified_date = listing_db["Last Modified Date"]
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

            today = date.today()
            year_today = str(today)[0:4]
            month_today = str(today)[5:7]
            day_today = str(today)[8:]

            # ensure date is between/including Jan 3, 2021 and Jan 1, 2025
            # per R4-6 and R5-3
            if int(year_today) >= 2022 and int(year_today) <= 2024:
                if int(month_today) >= 1 and int(month_today) <= 12:
                    if int(day_today) >= 1 and int(day_today) <= 31:
                        self.last_modified_date = str(today)

            elif int(year_today) == 2021:

                if int(month_today) == 1:
                    if int(day_today) >= 3 and int(day_today) <= 31:
                        self.last_modified_date = str(today)

                elif int(month_today) >= 2 and int(month_today) <= 12:
                    if int(day_today) >= 1 and int(day_today) <= 31:
                        self.last_modified_date = str(today)

            elif int(year_today) == 2025 and int(month_today) == 1 and int(day_today) == 1:
                self.last_modified_date = str(today)

            # listing modification is valid, return True
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
