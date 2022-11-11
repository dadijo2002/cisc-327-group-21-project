from seleniumbase import BaseCase

from qbnb_test.conftest import base_url
from unittest.mock import patch
from qbnb.models import User

# create test user and example listing
register("test", "test@grouptwentyone.ca", "FUNpswd123?!")
create_listing("Joseph Mother", "New Listing", "1234 Sesame Street",
                "6", "none :(", "This property is the best thing since sliced bread!", 
                "2022-06-09", "2023-04-20")

"""
This file defines all integration tests for the frontend homepage.
"""

class FrontEndHomePageTest(BaseCase):

    def setup(self):
        """
        Log in to start testing
        """
        # simulate login
        self.open(base_url + "/login")
        self.type("#email", "test@grouptwentyone.ca")
        self.type("#password", "FUNpswd123?!")
        self.click("input[type=\"submit\"]")
        self.click_link("update")

    def test_cancelupdate(self):
        """
        Test when user cancels update
        Test method: Black Box exhaustive output coverage (1 of 2)
        """
        self.click_link("Cancel")
        self.assert_equal(self.get_current_url(), base_url + "/")

    def test_successfulupdate(self):
        """
        Test that products can be updated successfully
        Test method: Black Box exhaustive output coverage (2 of 2)
        """
        # test all fields can be modified
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