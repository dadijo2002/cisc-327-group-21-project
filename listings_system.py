import mysql.connector
import os
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import datetime


"""
This is an incomplete listings 
system for the qBnB plan.
Group 21 - CISC 327
Author: Yash Patel
Student Number: 20227432
Date: September 25, 2022
"""
# This block of code represents a simulation of a listing entry in a database
# I have read through the airbnb website and made a checklist of what
# could be included for the listing entries;

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Listings(db.Model):  # SQLified the old Listings class a little bit
    host = db.Column(db.String(80), Unique=True, nullable=False)
    title = db.Column(db.String(80), unique=True, nullable=False)
    location = db.Column(db.String(120), unique=True, nullable=False)
    price_per_night = db.Column(db.Integer, primary_key=True)
    amenities = db.Column(db.String(120), unique=True, nullable=False)
    description = db.Column(db.String(2000), unique=True, nullable=False)
    availability = db.Column(db.String(10), unique=True, nullable=False)
    last_modified_date = db.Column(db.String(50), unique=True, nullable=False)
    owner_email = db.Column(db.String(120), unique=True, nullable=False)

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
        """

        if self.validate() is True:
            db.Model.append(self.host, self.title, self.location,
                            self.price_per_night,
                            self.guests, self.amenities,
                            self.description, self.availability)
            return True
        else:
            return False

    # R5-1: User can change all attributes of a listing, except owner_id
    # and last_modified_date
    def change_listing(self):
        """
        This Function will change the listing information
        of the listing that the user is looking at.
        It will ask the user if they want to change the
        host, title, location, price per night, guests,
        amenities, description, or availability of the listing.
        It will then ask the user to input the new information
        for the attribute they want to change.
        """
        print("Which attribute of the listing do you want to change?")
        print("1: Host")
        print("2: Title")
        print("3: Location")
        print("4: Price Per Night")
        print("5: Guests")
        print("6: Amenities")
        print("7: Description")
        print("8: Availability")
        print("9: Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            self.host = input("Enter the new host: ")
        elif choice == "2":
            self.title = input("Enter the new title: ")
        elif choice == "3":
            self.location = input("Enter the new location: ")
        elif choice == "4":
            self.price_per_night += input(
                "User can only increase this value, Enter the amount you would \
                 like to increase the price by: ")
        elif choice == "5":
            self.guests = input("Enter the new amount of guests: ")
        elif choice == "6":
            self.amenities = input("Enter the new amenities: ")
        elif choice == "7":
            self.description = input("Enter the new description: ")
        elif choice == "8":
            self.availability = input("Enter the new availability: ")
        elif choice == "9":
            return
        else:
            print("Invalid choice.")

        # Here is where last_modified_date would be updated
        self.last_modified_date = datetime.datetime.now()
