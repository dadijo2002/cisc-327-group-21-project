
"""
This is an incomplete sample implementation of the user model for our
qBnb plan.

Group 21 - CISC 327
Author: Makayla McMullin
Student Number: 20226722
Date: September 23, 2022
"""

user_input={ "username": "user1234",
            "name": "John Smith",
            "email": "john.smith@yahoo.com",
            "password": "Vgk34_l"}

class User:

    def __init__(self):
        """Initalizes user information from user input"""
        self.username = user_input["username"]
        self.name= user_input["name"]
        self.email = user_input["email"]
        self.password = user_input["password"]
        self.listings = None 
        self.bookings=None
        self.balance = 0


    def get_balance(self):
        """Gets a user's blanace"""
        return self.balance



