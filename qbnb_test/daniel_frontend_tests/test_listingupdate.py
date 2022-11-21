from seleniumbase import BaseCase

from qbnb_test.conftest import base_url
from unittest.mock import patch
from qbnb.models import User


"""
This file defines all integration tests for the frontend homepage.
"""

class FrontEndHomePageTest(BaseCase):

    def setup(self, *-):
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

        self.type("#email", "test@grouptwentyone.ca")
        self.type("#password", "FUNpswd123?!")
        self.click('input[type="submit"]')

        self.open(base_url)
        self.assert_element("#welcome_header")
        self.assert_text("Welcome test !", "welcome-header")

        # Open the listing creation page so there is something
        # to actually test
        self.open(base_url + "/listings_creation")
        # Fill host, title, location, ppn, guests,
        # amenities, desc, availability
        self.type("#host", "Joseph Mother")
        self.type("#title", "New Listing")
        self.type("#location", "1234 Sesame Street")
        self.type("#ppn", "100")
        self.type("#guests", "6")
        self.type("#amenities", "none :(")
        self.type("#desc", "This property is the best thing since sliced bread!")
        self.type("#startavail", "2022-06-09")
        self.type("#endavail", "2023-04-20")

        # Click the submit button
        self.click('input[type="submit"]')

    def test_cancelupdate(self, *_):
        """
        Test when user cancels update
        Test method: Black Box exhaustive output coverage (1 of 2)
        """
        self.click_link("Cancel")
        self.assert_equal(self.get_current_url(), base_url + "/")

    def test_successfulupdate(self, *_):
        """
        Test that products can be updated successfully
        Test method: Black Box exhaustive output coverage (2 of 2)
        """

        # open page
        self.open(base_url + '/listings_update')
        # test all fields can be modified with valid input
        self.type("#host", "Joe Mama")
        self.type("#title", "Newer Product")
        self.type("#location", "1273 Rockefeller Street")
        self.type("#guests", "5")
        self.type("#amenities", "Sliced Bread, Baked Beans, and a nice view")
        self.type("#description", "This property is better than sliced bread!")
        self.type("#ppn", "100")
        self.type("#startavail", "2023-03-19")
        self.type("#endavail", "2024-03-19")
        # make sure on the correct page
        self.assert_equal(self.get_current_url(), base_url + "/update-product/")
        # submit changes
        self.click("input[type=\"submit\"]")

        # If product update successful, return to profile page
        self.assert_equal(self.get_current_url(), base_url + "/")
        # Product list on homepage should now be updated
        self.assert_text("Newer Product")

    def test_update_listing_fail_dates(self, *_):
        """
        Tests that register page sends an error message when end date is before
        beginning date
        Test method: Black Box input coverage- input partitioning
        """
        # open register page
        self.open(base_url + '/register')
        # test error if end available date before start available date
        self.type("#host", "Joe Mama")
        self.type("#title", "Newer Product")
        self.type("#location", "1273 Rockefeller Street")
        self.type("#guests", "5")
        self.type("#amenities", "Sliced Bread, Baked Beans, and a nice view")
        self.type("#description", "This property is better than sliced bread!")
        self.type("#ppn", "100")
        self.type("#startavail", "2024-03-19")
        self.type("#endavail", "2023-03-19")
        # make sure on the correct page
        self.assert_equal(self.get_current_url(), base_url + "/update-product/")
        # submit changes
        self.click("input[type=\"submit\"]")
        self.assert_element("#errmessage")
        self.assert_text("Something was incorrect! Please try again.", "#errmessage")

    def test_update_listing_fail_bounds(self, *_):
        """
        Tests that register page sends an input is too large or small
        Test method: Black Box input coverage - input boundary
        """
        # open register page
        self.open(base_url + '/register')
        # test error if end date past limit
        self.type("#host", "Joe Mama")
        self.type("#title", "Newer Product")
        self.type("#location", "1273 Rockefeller Street")
        self.type("#guests", "5")
        self.type("#amenities", "Sliced Bread, Baked Beans, and a nice view")
        self.type("#description", "This property is better than sliced bread!")
        self.type("#ppn", "100")
        self.type("#startavail", "2023-03-19")
        self.type("#endavail", "2025-03-19")
        # make sure on the correct page
        self.assert_equal(self.get_current_url(), base_url + "/update-product/")
        # submit changes
        self.click("input[type=\"submit\"]")
        self.assert_element("#message")
        self.assert_text("Date range was invalid! Please try again.", "#message")

        # test error if beginning date before limit
        self.type("#host", "Joe Mama")
        self.type("#title", "Newer Product")
        self.type("#location", "1273 Rockefeller Street")
        self.type("#guests", "5")
        self.type("#amenities", "Sliced Bread, Baked Beans, and a nice view")
        self.type("#description", "This property is better than sliced bread!")
        self.type("#ppn", "100")
        self.type("#startavail", "2020-03-19")
        self.type("#endavail", "2023-03-19")
        # make sure on the correct page
        self.assert_equal(self.get_current_url(), base_url + "/update-product/")
        # submit changes
        self.click("input[type=\"submit\"]")
        self.assert_element("#message")
        self.assert_text("Date range was invalid! Please try again.", "#message")

        # test error if host name too long
        # 81 character input
        self.type("#host", 
            "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA \
                AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
            # honestly same
        self.type("#title", "Newer Product")
        self.type("#location", "1273 Rockefeller Street")
        self.type("#guests", "5")
        self.type("#amenities", "Sliced Bread, Baked Beans, and a nice view")
        self.type("#description", "This property is better than sliced bread!")
        self.type("#ppn", "100")
        self.type("#startavail", "2022-03-19")
        self.type("#endavail", "2023-03-19")
        # make sure on the correct page
        self.assert_equal(self.get_current_url(), base_url + "/update-product/")
        # submit changes
        self.click("input[type=\"submit\"]")
        self.assert_element("#message")
        self.assert_text("Something was incorrect! Please try again.", "#message")

        # test error if listing title name too long
        self.type("#host", "Joe Mama")
        # 81 character input
        self.type("#title",
            "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA \
                AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
        self.type("#location", "1273 Rockefeller Street")
        self.type("#guests", "5")
        self.type("#amenities", "Sliced Bread, Baked Beans, and a nice view")
        self.type("#description", "This property is better than sliced bread!")
        self.type("#ppn", "100")
        self.type("#startavail", "2022-03-19")
        self.type("#endavail", "2023-03-19")
        # make sure on the correct page
        self.assert_equal(self.get_current_url(), base_url + "/update-product/")
        # submit changes
        self.click("input[type=\"submit\"]")
        self.assert_element("#message")
        self.assert_text("Something was incorrect! Please try again.", "#message")

        # test error if address name too long
        self.type("#host", "Joe Mama")
        self.type("#title", "Newer Product")
        # 121 character input
        self.type("#location",
            "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA \
                AAAAAAAAAAAAAAAAAAAAAADRESSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS")
        self.type("#guests", "5")
        self.type("#amenities", "Sliced Bread, Baked Beans, and a nice view")
        self.type("#description", "This property is better than sliced bread!")
        self.type("#ppn", "100")
        self.type("#startavail", "2022-03-19")
        self.type("#endavail", "2023-03-19")
        # make sure on the correct page
        self.assert_equal(self.get_current_url(), base_url + "/update-product/")
        # submit changes
        self.click("input[type=\"submit\"]")
        self.assert_element("#message")
        self.assert_text("Something was incorrect! Please try again.", "#message")

        # test error if address name too long
        self.type("#host", "Joe Mama")
        self.type("#title", "Newer Product")
        self.type("#location", "1273 Rockefeller Street")
        self.type("#guests", "5")
        # 121 character input
        self.type("#amenities", 
            "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA \
                AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
        self.type("#description", "This property is better than sliced bread!")
        self.type("#ppn", "100")
        self.type("#startavail", "2022-03-19")
        self.type("#endavail", "2023-03-19")
        # make sure on the correct page
        self.assert_equal(self.get_current_url(), base_url + "/update-product/")
        # submit changes
        self.click("input[type=\"submit\"]")
        self.assert_element("#message")
        self.assert_text("Something was incorrect! Please try again.", "#message")

        # test error if description name too long
        self.type("#host", "Joe Mama")
        self.type("#title", "Newer Product")
        self.type("#location", "1273 Rockefeller Street"))
        self.type("#guests", "5")
        self.type("#amenities", "Sliced Bread, Baked Beans, and a nice view")
        # 2001 character input
        self.type("#description", "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA \
            AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA \
                AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA \
                    AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA \
                        AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA \
                            AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA \
                                AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA \
                                    AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA \
                                        AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA \
                                            AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA \
                                                AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA \
                                                    AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA \
                                                        AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA \
                                                            AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA \
                                                                AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA \
                                                                    AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA \
                                                                        AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA \
                                                                            AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA \
                                                                                AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA \
                                                                                    AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA \
                                                                                        AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA \
                                                                                            AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA \
                                                                                                AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA \
                                                                                                    AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA \
                                                                                                        AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA \
                                                                                                            AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA \
                                                                                                                AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA \
                                                                                                                    AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA \
                                                                                                                        AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA \
                                                                                                                            AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA \
                                                                                                                                AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA \
                                                                                                                                    AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA \
                                                                                                                                        AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
        self.type("#ppn", "100")
        self.type("#startavail", "2022-03-19")
        self.type("#endavail", "2023-03-19")
        # make sure on the correct page
        self.assert_equal(self.get_current_url(), base_url + "/update-product/")
        # submit changes
        self.click("input[type=\"submit\"]")
        self.assert_element("#message")
        self.assert_text("Something was incorrect! Please try again.", "#message")

        # make sure that mandatory data is entered
        # empty host
        self.type("#host", "")
        self.type("#title", "Newer Product")
        self.type("#location", "1273 Rockefeller Street")
        self.type("#guests", "5")
        self.type("#amenities", "Sliced Bread, Baked Beans, and a nice view")
        self.type("#description", "This property is better than sliced bread!")
        self.type("#ppn", "100")
        self.type("#startavail", "2023-03-19")
        self.type("#endavail", "2024-03-19")
        # make sure on the correct page
        self.assert_equal(self.get_current_url(), base_url + "/update-product/")
        # submit changes
        self.click("input[type=\"submit\"]")
        self.assert_element("#message")
        self.assert_text("Please fill out this field", "#message")

        # make sure that mandatory data is entered
        self.type("#host", "Joe Mama")
        # empty title
        self.type("#title", "")
        self.type("#location", "1273 Rockefeller Street")
        self.type("#guests", "5")
        self.type("#amenities", "Sliced Bread, Baked Beans, and a nice view")
        self.type("#description", "This property is better than sliced bread!")
        self.type("#ppn", "100")
        self.type("#startavail", "2023-03-19")
        self.type("#endavail", "2024-03-19")
        # make sure on the correct page
        self.assert_equal(self.get_current_url(), base_url + "/update-product/")
        # submit changes
        self.click("input[type=\"submit\"]")
        self.assert_element("#message")
        self.assert_text("Please fill out this field", "#message")

        # make sure that mandatory data is entered
        self.type("#host", "Joe Mama")
        self.type("#title", "Newer Product")
        # empty address
        self.type("#location", "")
        self.type("#guests", "5")
        self.type("#amenities", "Sliced Bread, Baked Beans, and a nice view")
        self.type("#description", "This property is better than sliced bread!")
        self.type("#ppn", "100")
        self.type("#startavail", "2023-03-19")
        self.type("#endavail", "2024-03-19")
        # make sure on the correct page
        self.assert_equal(self.get_current_url(), base_url + "/update-product/")
        # submit changes
        self.click("input[type=\"submit\"]")
        self.assert_element("#message")
        self.assert_text("Please fill out this field", "#message")

        # make sure that mandatory data is entered
        self.type("#host", "Joe Mama")
        self.type("#title", "Newer Product")
        self.type("#location", "1273 Rockefeller Street")
        # empty number of max guests
        self.type("#guests", "")
        self.type("#amenities", "Sliced Bread, Baked Beans, and a nice view")
        self.type("#description", "This property is better than sliced bread!")
        self.type("#ppn", "100")
        self.type("#startavail", "2023-03-19")
        self.type("#endavail", "2024-03-19")
        # make sure on the correct page
        self.assert_equal(self.get_current_url(), base_url + "/update-product/")
        # submit changes
        self.click("input[type=\"submit\"]")
        self.assert_element("#message")
        self.assert_text("Please fill out this field", "#message")

        # make sure that mandatory data is entered
        self.type("#host", "Joe Mama")
        self.type("#title", "Newer Product")
        self.type("#location", "1273 Rockefeller Street")
        self.type("#guests", "5")
        # empty amenities list
        self.type("#amenities", ")
        self.type("#description", "This property is better than sliced bread!")
        self.type("#ppn", "100")
        self.type("#startavail", "2023-03-19")
        self.type("#endavail", "2024-03-19")
        # make sure on the correct page
        self.assert_equal(self.get_current_url(), base_url + "/update-product/")
        # submit changes
        self.click("input[type=\"submit\"]")
        self.assert_element("#message")
        self.assert_text("Please fill out this field", "#message")

        # make sure that mandatory data is entered
        self.type("#host", "Joe Mama")
        self.type("#title", "Newer Product")
        self.type("#location", "1273 Rockefeller Street")
        self.type("#guests", "5")
        self.type("#amenities", "Sliced Bread, Baked Beans, and a nice view")
        self.type("#description", "This property is better than sliced bread!")
        self.type("#ppn", "100")
        self.type("#startavail", "2023-03-19")
        self.type("#endavail", "2024-03-19")
        # make sure on the correct page
        self.assert_equal(self.get_current_url(), base_url + "/update-product/")
        # submit changes
        self.click("input[type=\"submit\"]")
        self.assert_element("#message")
        self.assert_text("Please fill out this field", "#message")

        # make sure that mandatory data is entered
        self.type("#host", "Joe Mama")
        self.type("#title", "Newer Product")
        self.type("#location", "1273 Rockefeller Street")
        self.type("#guests", "5")
        self.type("#amenities", "Sliced Bread, Baked Beans, and a nice view")
        self.type("#description", "This property is better than sliced bread!")
        self.type("#ppn", "100")
        self.type("#startavail", "2023-03-19")
        self.type("#endavail", "2024-03-19")
        # make sure on the correct page
        self.assert_equal(self.get_current_url(), base_url + "/update-product/")
        # submit changes
        self.click("input[type=\"submit\"]")
        self.assert_element("#message")
        self.assert_text("Please fill out this field", "#message")

        # make sure that mandatory data is entered
        self.type("#host", "Joe Mama")
        self.type("#title", "Newer Product")
        self.type("#location", "1273 Rockefeller Street")
        self.type("#guests", "5")
        self.type("#amenities", "Sliced Bread, Baked Beans, and a nice view")
        # empty description
        self.type("#description", "")
        self.type("#ppn", "100")
        self.type("#startavail", "2023-03-19")
        self.type("#endavail", "2024-03-19")
        # make sure on the correct page
        self.assert_equal(self.get_current_url(), base_url + "/update-product/")
        # submit changes
        self.click("input[type=\"submit\"]")
        self.assert_element("#message")
        self.assert_text("Please fill out this field", "#message")

        # make sure that mandatory data is entered
        self.type("#host", "Joe Mama")
        self.type("#title", "Newer Product")
        self.type("#location", "1273 Rockefeller Street")
        self.type("#guests", "5")
        self.type("#amenities", "Sliced Bread, Baked Beans, and a nice view")
        self.type("#description", "This property is better than sliced bread!")
        # empty price per night
        self.type("#ppn", "")
        self.type("#startavail", "2023-03-19")
        self.type("#endavail", "2024-03-19")
        # make sure on the correct page
        self.assert_equal(self.get_current_url(), base_url + "/update-product/")
        # submit changes
        self.click("input[type=\"submit\"]")
        self.assert_element("#message")
        self.assert_text("Please fill out this field", "#message")

        # make sure that mandatory data is entered
        self.type("#host", "Joe Mama")
        self.type("#title", "Newer Product")
        self.type("#location", "1273 Rockefeller Street")
        self.type("#guests", "5")
        self.type("#amenities", "Sliced Bread, Baked Beans, and a nice view")
        self.type("#description", "This property is better than sliced bread!")
        self.type("#ppn", "100")
        # empty start date
        self.type("#startavail", "")
        self.type("#endavail", "2024-03-19")
        # make sure on the correct page
        self.assert_equal(self.get_current_url(), base_url + "/update-product/")
        # submit changes
        self.click("input[type=\"submit\"]")
        self.assert_element("#message")
        self.assert_text("Please fill out this field", "#message")

        # make sure that mandatory data is entered
        self.type("#host", "Joe Mama")
        self.type("#title", "Newer Product")
        self.type("#location", "1273 Rockefeller Street")
        self.type("#guests", "5")
        self.type("#amenities", "Sliced Bread, Baked Beans, and a nice view")
        self.type("#description", "This property is better than sliced bread!")
        self.type("#ppn", "100")
        self.type("#startavail", "2023-03-19")
        # empty start date
        self.type("#endavail", "")
        # make sure on the correct page
        self.assert_equal(self.get_current_url(), base_url + "/update-product/")
        # submit changes
        self.click("input[type=\"submit\"]")
        self.assert_element("#message")
        self.assert_text("Please fill out this field", "#message")