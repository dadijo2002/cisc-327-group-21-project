
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

    def validate_password(password):
        """This Function will serve as our way to check if a password
            is valid before adding it to the system. """
        lower, upper, special, digit = 0, 0, 0, 0
        # counter variables of lowercase, uppercase,special and digit
        # characters  
        if len(password)>=6:
            for i in password:
            
                # counting lowercase alphabets
                if (i.islower()):
                    lower+=1           
            
                # counting uppercase alphabets
                if (i.isupper()):
                    upper+=1           
            
                # counting digits
                if (i.isdigit()):
                    digit+=1           
 
                # counting special characters
                if(i=='@'or i=='$' or i=='_'):
                    special+=1          
            if (lower>=1 and upper>=1 and special>=1 and 
                digit>=1 and lower+special+upper+digit==len(password)):
                # If password has one or more uppercase letter, lowercase
                # letter, sepecial character,and digit and no other
                # characters
                return True
        else:
            return False 

        

    def __repr__(self):
        return '<User %r>' % self.username


