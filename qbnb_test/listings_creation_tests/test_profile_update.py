from seleniumbase import BaseCase

from qbay_test.conftest import base_url
from unittest.mock import patch
from qbay.models import User

"""
This file defines all integration tests for the profile update page.
"""


class test_profile_update(BaseCase):

    def setup_user(self, *_):
        """
        Log in to start testing
        """
        # do we need to do this?

        # create test user
        register("test", "test@grouptwentyone.ca", "FUNpswd123?!")

        # simulate login
        self.open(base_url + "/login")
        self.type("#email", "test@grouptwentyone.ca")
        self.type("#password", "FUNpswd123?!")
        self.click("input[type=\"submit\"]")
        self.click_link("update")

    def test_successful_profile_update(self, *_):
        """
        Test that a user can successfully update their profile.
        """
        # update profile
        self.type("#email", "yasho@gmail.com")
        self.type("#name", "Yasho45")
        self.type("#password", "FUNpswd123?!")
        self.type("#password2", "FUNpswd123?!")
        self.type("#Billing Address", "1234 Fake Street")
        self.type("#Postal", "V6T 1Z4")
        self.click("input[type=\"submit\"]")

    def test_unsuccessful_profile_update_email(self, *_):
        """
        Test that a user cannot update their profile with invalid inputs.
        did not follow email rules
        """
        # invalid email
        self.type("#email", "yashoatgmail.com")
        self.type("#name", "Yasho45")
        self.type("#password", "FUNpswd123?!")
        self.type("#password2", "FUNpswd123?!")
        self.type("#Billing Address", "1234 Fake Street")
        self.type("#Postal", "V6T 1Z4")
        self.click("input[type=\"submit\"]")
        self.assert_element("#errmessage")
        self.assert_text(
            "Something was incorrect! Please try again.", "#errmessage")

    def test_unsuccessful_profile_update_name(self, *_):
        """
        Test that a user cannot update their profile with invalid inputs.
        did not follow name rules
        """
        # invalid email
        self.type("#email", "yashoatgmail.com")
        self.type("#name", "")
        self.type("#password", "FUNpswd123?!")
        self.type("#password2", "FUNpswd123?!")
        self.type("#Billing Address", "1234 Fake Street")
        self.type("#Postal", "V6T 1Z4")
        self.click("input[type=\"submit\"]")
        self.assert_element("#errmessage")
        self.assert_text(
            "Something was incorrect! Please try again.", "#errmessage")

    def test_unsuccessful_profile_update_password(self, *_):
        """
        Test that a user cannot update their profile with invalid inputs.
        did not follow password rules
        """
        # invalid email
        self.type("#email", "yashoatgmail.com")
        self.type("#name", "Yasho45")
        self.type("#password", "pswd123")
        self.type("#password2", "pswd123")
        self.type("#Billing Address", "1234 Fake Street")
        self.type("#Postal", "V6T 1Z4")
        self.click("input[type=\"submit\"]")
        self.assert_element("#errmessage")
        self.assert_text(
            "Something was incorrect! Please try again.", "#errmessage")

    def test_unsuccessful_profile_update_passwordtwo(self, *_):
        """
        Test that a user cannot update their profile with invalid inputs.
        incorrect confirm password
        """
        # invalid email
        self.type("#email", "yashoatgmail.com")
        self.type("#name", "Yasho45")
        self.type("#password", "FUNpswd123?!")
        self.type("#password2", "FUNpswd")
        self.type("#Billing Address", "1234 Fake Street")
        self.type("#Postal", "V6T 1Z4")
        self.click("input[type=\"submit\"]")
        self.assert_element("#errmessage")
        self.assert_text(
            "Something was incorrect! Please try again.", "#errmessage")

    def test_unsuccessful_profile_update_billing(self, *_):
        """
        Test that a user cannot update their profile with invalid inputs.
        incorrect billing address
        """
        # invalid email
        self.type("#email", "yashoatgmail.com")
        self.type("#name", "Yasho45")
        self.type("#password", "FUNpswd123?!")
        self.type("#password2", "FUNpswd")
        self.type("#Billing Address", "")
        self.type("#Postal", "V6T 1Z4")
        self.click("input[type=\"submit\"]")
        self.assert_element("#errmessage")
        self.assert_text(
            "Something was incorrect! Please try again.", "#errmessage")

    def test_unsuccessful_profile_update_postal(self, *_):
        """
        Test that a user cannot update their profile with invalid inputs.
        incorrect postal code
        """
        # invalid email
        self.type("#email", "yashoatgmail.com")
        self.type("#name", "Yasho45")
        self.type("#password", "FUNpswd123?!")
        self.type("#password2", "FUNpswd")
        self.type("#Billing Address", "1234 Fake Street")
        self.type("#Postal", "")
        self.click("input[type=\"submit\"]")
        self.assert_element("#errmessage")
        self.assert_text(
            "Something was incorrect! Please try again.", "#errmessage")

    def test_unsuccessful_profile_update_postaltwo(self, *_):
        """
        Test that a user cannot update their profile with invalid inputs.
        incorrect postal code RULE - must be canadian
        """
        # invalid email
        self.type("#email", "yashoatgmail.com")
        self.type("#name", "Yasho45")
        self.type("#password", "FUNpswd123?!")
        self.type("#password2", "FUNpswd")
        self.type("#Billing Address", "1234 Fake Street")
        self.type("#Postal", "americanpostal234")
        self.click("input[type=\"submit\"]")
        self.assert_element("#errmessage")
        self.assert_text(
            "Something was incorrect! Please try again.", "#errmessage")

    def test_unsuccessful_profile_update_usertwo(self, *_):
        """
        Test that a user cannot update their profile with invalid inputs.
        incorrect username rule - must be alphanumeric
        """
        # invalid email
        self.type("#email", "yashoatgmail.com")
        self.type("#name", "yash!!x")
        self.type("#password", "FUNpswd123?!")
        self.type("#password2", "FUNpswd")
        self.type("#Billing Address", "1234 Fake Street")
        self.type("#Postal", "americanpostal234")
        self.click("input[type=\"submit\"]")
        self.assert_element("#errmessage")
        self.assert_text(
            "Something was incorrect! Please try again.", "#errmessage")
