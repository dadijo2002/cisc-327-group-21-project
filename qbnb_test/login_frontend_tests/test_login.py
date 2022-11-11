from seleniumbase import BaseCase
from qbnb_test.conftest import base_url
from unittest.mock import patch
from qbnb.models import *


class test_login_page(BaseCase):

    def test_login_success(self, *_):
        """
        Tests if the login page can log a user in
        successfully and take them to the user homepage
        Test method: Black Box exhaustive output coverage (1 of 3)
        """
        self.open(base_url + '/login')
        self.type("#email", "test0@test.com")
        self.type("#password", "123456")
        self.click('input[type="submit"]')

        self.open(base_url)
        self.assert_element("#welcome_header")
        self.assert_text("Welcome u0 !", "welcome-header")

    def test_login_pw(self, *_):  # try to make a test with no password
        """
        Tests if the password field is unfilled
        Test method: Black Box exhaustive output coverage(2 of 3)
        """
        self.open(base_url + '/login')
        self.type("#email", "test1@test.com")
        self.type("#password", " ")
        self.click('input[type="submit"]')
        self.open(base_url)
        self.assert_element("#error_header")
        self.assert_text("Error! You didn't input a password", "error-header")

    def test_login_email(self, *_):
        """
        Tests if the email field is unfilled
        Test method: Black Box exhaustive output coverage(3 of 3)
        """
        self.open(base_url + '/login')
        self.type("#email", " ")
        self.type("#password", "hamburgers")
        self.click('input[type="submit"]')
        self.open(base_url)
        self.assert_element("#error_header")
        self.assert_text("Error! You didn't input an email address!", "error-header")
