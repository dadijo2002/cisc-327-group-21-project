from seleniumbase import BaseCase

from qbnb_test.conftest import base_url
from unittest.mock import patch
from qbnb.models import User

"""
This file defines all integration tests for the frontend register page.
"""


class FrontEndRegistration(BaseCase):

    def test_register_success(self, *_):
        """
        Tests if register page takes a sucessful registation to the
        login page
        Test method: Black Box  exhaustive output coverage (1 of 2)
        """
        # open register page
        self.open(base_url + '/register')
        # fill email, username, password and password2
        self.type("#email", "test0@test.com")
        self.type("#name", "u0")
        self.type("#password", "_Aa123")
        self.type("#password2", "_Aa123")

        # click Register button
        self.click('input[type="submit"]')

        # open login page
        self.open(base_url + '/login')
        # test if the page loads correctly
        self.assert_element("#message")
        self.assert_text("Please login", "#message")

    def test_register_fail(self, *_):
        """
        Tests if invail register sends error message
        Test method: Black Box  exhaustive output coverage (2 of 2)
        """
        # open register page
        self.open(base_url + '/register')
        # empty email, username, password and password2
        self.type("#email", "")
        self.type("#name", "")
        self.type("#password", "")
        self.type("#password2", "")

        # click Register button
        self.click('input[type="submit"]')

        # test if error message loads
        self.assert_element("#message")
        self.assert_text("Registration failed.", "#message")

    def test_register_passwords_diff(self, *_):
        """
        Tests that register page sends an error message when password
        and password2 inputs are different
        Test method: Black Box input coverage- input partitioning
        """
        # open register page
        self.open(base_url + '/register')
        # fill email, username, password and password2
        self.type("#email", "test1@test.com")
        self.type("#name", "u1")
        self.type("#password", "_Aa123")
        self.type("#password2", "_Aa1234")
        # click Register button
        self.click('input[type="submit"]')
        # test error message is thrown
        self.assert_element("#message")
        self.assert_text("The passwords do not match", "#message")

    def test_register_boundaries(self, *_):
        """
        Tests if password or username (email lengths are caught by
        email vailidator) inputs out side boundary
        values cause error message.
        Test method: Black Box Input Boundary Testing
        """
        # open register page
        self.open(base_url + '/register')

        # password too long
        # (length > 80 chars, restriction in Users class definition)
        self.type("#email", "test1@test.com")
        self.type("#name", "u1")
        self.type("#password", "_Aa123333333333333333333333333333333333\
                  333333333333333333333333333333333333333333")
        self.type("#password2", "_Aa123333333333333333333333333333333333\
                  333333333333333333333333333333333333333333")
        # click Register button
        self.click('input[type="submit"]')
        # test error message is thrown
        self.assert_element("#message")
        self.assert_text("Registration failed.", "#message")

        # password too short (<6)
        self.type("#email", "test1@test.com")
        self.type("#name", "u1")
        self.type("#password", "_Aa12")
        self.type("#password2", "_Aa12")
        # click Register button
        self.click('input[type="submit"]')
        # test error message is thrown
        self.assert_element("#message")
        self.assert_text("Registration failed.", "#message")

        # username empty (too short)
        self.type("#email", "test1@test.com")
        self.type("#name", "")
        self.type("#password", "_Aa123")
        self.type("#password2", "_Aa123")
        # click Register button
        self.click('input[type="submit"]')
        # test error message is thrown
        self.assert_element("#message")
        self.assert_text("Registration failed.", "#message")

        # username too long
        # (length > 80 chars, restriction in Users class definition)
        self.type("#email", "test1@test.com")
        self.type("#name", "u100000000000000000000000000000000000000000000\
                    00000000000000000000000000000000000")
        self.type("#password", "_Aa123")
        self.type("#password2", "_Aa123")
        # click Register button
        self.click('input[type="submit"]')
        # test error message is thrown
        self.assert_element("#message")
        self.assert_text("Registration failed.", "#message")

    def test_register_password_vaild(self, *_):
        """
        Tests if invaild passoword imput sends error message
        Test method: Black Box imput partiioning
        (partitions: vaild and invailid)
        """
        # open register page
        self.open(base_url + '/register')
        # enter email, username, password and password2
        self.type("#email", "test1@test.com")
        self.type("#name", "u1")
        self.type("#password", "123456")
        self.type("#password2", "123456")

        # click Register button
        self.click('input[type="submit"]')

        # test error message appears
        self.assert_element("#message")
        self.assert_text("Registration failed.", "#message")

    def test_register_email_vaild(self, *_):
        """
        Tests if invaild email imput sends error message
        Test method: Black Box imput partiioning
        (partitions: vaild and invailid)
        """
        # open register page
        self.open(base_url + '/register')
        # empty email, username, password and password2
        self.type("#email", "test1test.com")
        self.type("#name", "u1")
        self.type("#password", "_Aa123")
        self.type("#password2", "_Aa123")

        # click Register button
        self.click('input[type="submit"]')

        # test error message appears
        self.assert_element("#message")
        self.assert_text("Registration failed.", "#message")
