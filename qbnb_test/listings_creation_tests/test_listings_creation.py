from seleniumbase import BaseCase

from qbay_test.conftest import base_url
from unittest.mock import patch
from qbay.models import User

"""
This file defines all integration tests for the listing creation page.
"""


class TestListingsCreation(BaseCase):

    def test_listings_creation_success(self, *_):
        """
        This function tests the listing creation page for successful
        creation of a listing.
        Test method: Black Box Exhaustive output coverage (1 of 2)
        """

        # Open the listing creation page
        self.open(base_url + "/listings_creation")
        # Fill host, title, location, ppn, guests,
        # amenities, desc, availability
        self.type("#host", "test_host")
        self.type("#title", "test_title")
        self.type("#location", "test_location")
        self.type("#ppn", "test_ppn")
        self.type("#guests", "test_guests")
        self.type("#amenities", "test_amenities")
        self.type("#desc", "test_desc")
        self.type("#startavail", "2022-01-03")
        self.type("#endavail", "2024-01-01")

        # Click the submit button
        self.click('input[type="submit"]')

    def test_listings_creation_failure(self, *_):
        """
        This function tests the listing creation page for unsuccessful
        creation of a listing.
        Test method: Black Box Exhaustive output coverage (2 of 2)
        """

        # Open the listing creation page
        self.open(base_url + "/listings_creation")
        # Fill host, title, location, ppn, guests,
        # amenities, desc, availability
        self.type("#host", "")
        self.type("#title", "")
        self.type("#location", "")
        self.type("#ppn", "")
        self.type("#guests", "")
        self.type("#amenities", "")
        self.type("#desc", "")
        self.type("#startavail", "")
        self.type("#endavail", "")

        # Click the submit button
        self.click('input[type="submit"]')

    def listings_creation_date_invalid(self, *_):
        """
        This function tests the listing creation page
        sending an error message when the given date is incorrect.
        Test method: Black Box input coverage - input partitioning
        """

        # Open the listing creation page
        self.open(base_url + "/listings_creation")
        # Fill host, title, location, ppn, guests,
        # amenities, desc, availability
        self.type("#host", "test_host")
        self.type("#title", "test_title")
        self.type("#location", "test_location")
        self.type("#ppn", "test_ppn")
        self.type("#guests", "test_guests")
        self.type("#amenities", "test_amenities")
        self.type("#desc", "test_desc")
        # Incorrect date
        self.type("#startavail", "2010-01-02")
        self.type("#endavail", "2030-01-01")

        # Click the submit button
        self.click('input[type="submit"]')

    def test_listings_creation_title_invalid(self, *_):
        """
        This function tests the listing creation page
        sending an error message when the given title 
        is too short or too long.
        Test method: Black Box input coverage - input partitioning
        """
        # title too short
        # Open the listing creation page
        self.open(base_url + "/listings_creation")
        # Fill host, title, location, ppn, guests,
        # amenities, desc, availability
        self.type("#host", "")
        self.type("#title", "test_title")
        self.type("#location", "test_location")
        self.type("#ppn", "test_ppn")
        self.type("#guests", "test_guests")
        self.type("#amenities", "test_amenities")
        self.type("#desc", "test_desc")
        self.type("#startavail", "2022-01-03")
        self.type("#endavail", "2024-01-01")

        # Click the submit button
        self.click('input[type="submit"]')

        # test error message is thrown
        self.assert_element("#message")
        self.assert_text("The passwords do not match", "#message")

        # title too long
        # Open the listing creation page
        self.open(base_url + "/listings_creation")
        # Fill host, title, location, ppn, guests,
        # amenities, desc, availability
        self.type("#host", "111111111111111111111111111111111 \
            111111111111111111111111111111111111111111111111")
        self.type("#title", "test_title")
        self.type("#location", "test_location")
        self.type("#ppn", "test_ppn")
        self.type("#guests", "test_guests")
        self.type("#amenities", "test_amenities")
        self.type("#desc", "test_desc")
        self.type("#startavail", "2022-01-03")
        self.type("#endavail", "2024-01-01")

        # Click the submit button
        self.click('input[type="submit"]')

        # test error message is thrown
        self.assert_element("#message")
        self.assert_text("The passwords do not match", "#message")

    def test_listings_creation_location_invalid(self, *_):
        """
        This function tests the listing creation page
        sending an error message when the given location 
        is too short
        Test method: Black Box input coverage - input partitioning
        """
        # location too short
        # Open the listing creation page
        self.open(base_url + "/listings_creation")
        # Fill host, title, location, ppn, guests,
        # amenities, desc, availability
        self.type("#host", "test_host")
        self.type("#title", "test_title")
        self.type("#location", "")
        self.type("#ppn", "test_ppn")
        self.type("#guests", "test_guests")
        self.type("#amenities", "test_amenities")
        self.type("#desc", "test_desc")
        self.type("#startavail", "2022-01-03")
        self.type("#endavail", "2024-01-01")

        # Click the submit button
        self.click('input[type="submit"]')

        # test error message is thrown
        self.assert_element("#message")
        self.assert_text("The passwords do not match", "#message")

    def test_listings_creation_ppn_invalid(self, *_):
        """
        This function tests the listing creation page
        sending an error message when the given ppn 
        is too cheap or too expensive
        Test method: Black Box input coverage - input partitioning
        """
        # ppn too short
        # Open the listing creation page
        self.open(base_url + "/listings_creation")
        # Fill host, title, location, ppn, guests,
        # amenities, desc, availability
        self.type("#host", "test_host")
        self.type("#title", "test_title")
        self.type("#location", "test_location")
        self.type("#ppn", "5")
        self.type("#guests", "test_guests")
        self.type("#amenities", "test_amenities")
        self.type("#desc", "test_desc")
        self.type("#startavail", "2022-01-03")
        self.type("#endavail", "2024-01-01")

        # Click the submit button
        self.click('input[type="submit"]')

        # test error message is thrown
        self.assert_element("#message")
        self.assert_text("The passwords do not match", "#message")

        # ppn too long
        # Open the listing creation page
        self.open(base_url + "/listings_creation")
        # Fill host, title, location, ppn, guests,
        # amenities, desc, availability
        self.type("#host", "test_host")
        self.type("#title", "test_title")
        self.type("#location", "test_location")
        self.type("#ppn", "10005")
        self.type("#guests", "test_guests")
        self.type("#amenities", "test_amenities")
        self.type("#desc", "test_desc")
        self.type("#startavail", "2022-01-03")
        self.type("#endavail", "2024-01-01")

        # Click the submit button
        self.click('input[type="submit"]')

        # test error message is thrown
        self.assert_element("#message")
        self.assert_text("The passwords do not match", "#message")

    def test_listings_creation_guests_invalid(self, *_):
        """
        This function tests the listing creation page
        sending an error message when the given guests 
        is too few or too many
        Test method: Black Box input coverage - input partitioning
        """
        # guests too short
        # Open the listing creation page
        self.open(base_url + "/listings_creation")
        # Fill host, title, location, ppn, guests,
        # amenities, desc, availability
        self.type("#host", "test_host")
        self.type("#title", "test_title")
        self.type("#location", "test_location")
        self.type("#ppn", "test_ppn")
        self.type("#guests", "")
        self.type("#amenities", "test_amenities")
        self.type("#desc", "test_desc")
        self.type("#startavail", "2022-01-03")
        self.type("#endavail", "2024-01-01")

        # Click the submit button
        self.click('input[type="submit"]')

        # test error message is thrown
        self.assert_element("#message")
        self.assert_text("The passwords do not match", "#message")

    def test_listings_creation_amenities_invalid(self, *_):
        """
        This function tests the listing creation page
        sending an error message when the given amenities 
        is too short
        Test method: Black Box input coverage - input partitioning
        """
        # amenities too short
        # Open the listing creation page
        self.open(base_url + "/listings_creation")
        # Fill host, title, location, ppn, guests,
        # amenities, desc, availability
        self.type("#host", "test_host")
        self.type("#title", "test_title")
        self.type("#location", "test_location")
        self.type("#ppn", "test_ppn")
        self.type("#guests", "test_guests")
        self.type("#amenities", "")
        self.type("#desc", "test_desc")
        self.type("#startavail", "2022-01-03")
        self.type("#endavail", "2024-01-01")

        # Click the submit button
        self.click('input[type="submit"]')

        # test error message is thrown
        self.assert_element("#message")
        self.assert_text("The passwords do not match", "#message")

    def test_listings_creation_desc_invalid(self, *_):
        """
        This function tests the listing creation page
        sending an error message when the given desc 
        is too short or too long
        Test method: Black Box input coverage - input partitioning
        """
        # desc too short
        # Open the listing creation page
        self.open(base_url + "/listings_creation")
        # Fill host, title, location, ppn, guests,
        # amenities, desc, availability
        self.type("#host", "test_host")
        self.type("#title", "test_title")
        self.type("#location", "test_location")
        self.type("#ppn", "test_ppn")
        self.type("#guests", "test_guests")
        self.type("#amenities", "test_amenities")
        self.type("#desc", "")
        self.type("#startavail", "2022-01-03")
        self.type("#endavail", "2024-01-01")

        # Click the submit button
        self.click('input[type="submit"]')

        # test error message is thrown
        self.assert_element("#message")
        self.assert_text("The passwords do not match", "#message")

        # desc too long
        # Open the listing creation page
        self.open(base_url + "/listings_creation")
        # Fill host, title, location, ppn, guests,
        # amenities, desc, availability
        self.type("#host", "test_host")
        self.type("#title", "test_title")
        self.type("#location", "test_location")
        self.type("#ppn", "test_ppn")
        self.type("#guests", "test_guests")
        self.type("#amenities", "test_amenities")
        self.type("#desc", "1111111111111111111111111 \
            11111111111111111111111111111111111111111111111111111111")
        self.type("#startavail", "2022-01-03")
        self.type("#endavail", "2024-01-01")

        # Click the submit button
        self.click('input[type="submit"]')

        # test error message is thrown
        self.assert_element("#message")
        self.assert_text("The passwords do not match", "#message")

    def test_listings_creation_avail_invalid(self, *_):
        """
        This function tests the listing creation page
        sending an error message when the given availability 
        is not a date
        Test method: Black Box input coverage - input partitioning
        """
        # availability not a date
        # Open the listing creation page
        self.open(base_url + "/listings_creation")
        # Fill host, title, location, ppn, guests,
        # amenities, desc, availability
        self.type("#host", "test_host")
        self.type("#title", "test_title")
        self.type("#location", "test_location")
        self.type("#ppn", "test_ppn")
        self.type("#guests", "test_guests")
        self.type("#amenities", "test_amenities")
        self.type("#desc", "test_desc")
        self.type("#startavail", "test_startavail")
        self.type("#endavail", "test_endavail")

        # Click the submit button
        self.click('input[type="submit"]')

        # test error message is thrown
        self.assert_element("#message")
        self.assert_text("The passwords do not match", "#message")
