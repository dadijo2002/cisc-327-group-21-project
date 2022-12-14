from seleniumbase import BaseCase
from qbnb_test.conftest import base_url



class test_bookings_page(BaseCase):

    def test_owner_booking_success(self, *_):
        """
        This is to test to see if the owner side of the
        booking page works
        """

        self.open(base_url + '/booking_owner')
        self.type("#owner", "John Price")
        self.type("#balance", "203467")
        self.type("#start_date", "December 12th")
        self.type("#end_date", "December 23rd")
        self.click('input[type="submit"]')

    def test_booking_success(self, *_):
        """
        This is to test if we can navigate to the
        bookings page and verify if things are
        labelled properly
        """
        self.open(base_url + '/booking')
        self.type("#name", "Simon Riley")
        self.type("#email", "GHST141@gmail.com")
        self.click('input[type="submit"]')

    def test_booking_fail(self, *_):
        """
        Tests if invalid parameters sends an error message
        """
        self.open(base_url + '/booking')
        self.type("#name", "")
        self.type("#email", "")
        self.click('input[type="submit"]')
        self.assert_element("#message")
        self.assert_text("Booking failed.", "#message")

    def test_booking_valid_email(self, *_):
        """
        Tests if the email parameter is invalid and
        what the webpage does when it isn't
        """
        self.open(base_url + '/booking')
        self.type("#name", "John Wick")
        self.type("#email", "test1test.com")
        self.click('input[type="submit"]')
        self.assert_element("#message")
        self.assert_text("Booking failed.", "#message")

    def test_balance_boundaries(self, *_):
        self.open(base_url + '/booking_owner')
        self.type("#owner", "Sam Fisher")
        self.type("#balance", "-100000")
        self.type("#start_date", "December 12th")
        self.type("#end_date", "December 23rd")
        self.click('input[type="submit"]')
        self.assert_element("#message")
        self.assert_text("Booking failed.", "#message")
