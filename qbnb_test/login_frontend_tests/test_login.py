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

    def test_login_email_valid(self, *_):
        """
        Tests if invalid email input sends error
        Test method: Black Box input partitioning
        """
        self.open(base_url + '/login')
        self.type("#email", "test1test.com")
        self.type("#password", "_TaskF141")
        self.click('input[type="submit"]')
        self.assert_element("#message")
        self.assert_text("Login failed", "#message")

    def test_login_boundaries(self, *_):
        """
        Tests if the password or email inputs outside boundaries
        cause an error
        Test method: Black Box Input Boundary Testing
        """

        self.open(base_url + '/login')
        self.type("#email", "test1@test.com")
        self.type("#password", "_Aa123333333333333333333333333333333333\
                          333333333333333333333333333333333333333333")
        self.assert_element("#message")
        self.assert_text("Login failed", "#message")

        self.type("#email", "test1@test.com")
        self.type("#password", "_Aa12")
        self.click('input[type="submit"]')
        # test error message is thrown
        self.assert_element("#message")
        self.assert_text("Login failed.", "#message")