from seleniumbase import BaseCase

from qbnb_test.conftest import base_url
from unittest.mock import patch
from qbnb.models import User

"""
This file defines all integration tests for the frontend homepage.
"""

class FrontEndHomePageTest(BaseCase):

    def setup(self):
        """
        Log in to start testing
        """

        # open register page
        self.open(base_url + '/register')
        # fill email, username, password and password2
        self.type("#email", "test@grouptwentyone.ca")
        self.type("#name", "test")
        self.type("#password", "FUNpswd123?!")
        self.type("#password2", "FUNpswd123?!")

        # click Register button
        self.click('input[type="submit"]')

        # open login page
        self.open(base_url + '/login')
        # test if the page loads correctly
        self.assert_element("#message")
        self.assert_text("Please login", "#message")
        # log in as test user
        self.type("#email", "test@grouptwentyone.ca")
        self.type("#password", "FUNpswd123?!")
        self.click("input[type=\"submit\"]")
        self.click_link("update")

    def test_pageload(self):
        """
        Tests that the homepage loads properly.
        Test method: Black Box exhaustive output coverage
        """
        self.open(base_url)
        self.assert_element("h1")
        self.assert_element("h2")
        self.assert_element("h4")  # i think we skipped h3 oops
        self.assert_text("Welcome, test!", "h1")
        self.assert_text("Here are all available products", "h2")