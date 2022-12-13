import unittest
from qbnb.models import *
from datetime import datetime

user = User(34532, "Fox", "Fj@gmail.com",
            "AliveAgain", "223, elm drive",
            "L743B3", 200000)
listing1 = listing("John", "Mother Base",
                   "Seychelles", 250, "pools!",
                   "A wonderful base of operations",
                   "available year round!", "tuesday", "BB@gmail.com")


class MyTestCase(unittest.TestCase):
    def test_book_listing_throws_exception(self):
        self.assertRaises(Exception, book_listing, user, listing1,
                          datetime(2024, 1, 5).strftime('Y-%m-%d'),
                          datetime(2024, 1, 10).strftime('Y-%m-%d'))


def test_user():
    i_file = open("Generic_SQLi.txt")
    payloads = i_file.readlines()
    for payload in payloads:
        try:
            book_listing(payload, listing1,
                         datetime(2024, 1, 5).strftime('Y-%m-%d'),
                         datetime(2024, 1, 10).strftime('Y-%m-%d'))
        except (TypeError, ValueError):
            print("An SQL Injection attack was stopped.")
    i_file.close()


def test_listing():
    i_file = open("Generic_SQLi.txt")
    payloads = i_file.readlines()
    for payload in payloads:
        try:
            book_listing(user, payload,
                         datetime(2024, 1, 5).strftime('Y-%m-%d'),
                         datetime(2024, 1, 10).strftime('Y-%m-%d'))
        except (TypeError, ValueError):
            print("An SQL Injection attack was stopped.")
    i_file.close()


def test_start_date():
    i_file = open("Generic_SQLi.txt")
    payloads = i_file.readlines()
    for payload in payloads:
        try:
            book_listing(user, listing1,
                         payload,
                         datetime(2024, 1, 10).strftime('Y-%m-%d'))
        except (TypeError, ValueError):
            print("An SQL Injection attack was stopped.")
    i_file.close()


def test_end_date():
    i_file = open("Generic_SQLi.txt")
    payloads = i_file.readlines()
    for payload in payloads:
        try:
            book_listing(user, listing1,
                         datetime(2024, 1, 5).strftime('Y-%m-%d'),
                         payload)
        except (TypeError, ValueError):
            print("An SQL Injection attack was stopped.")
    i_file.close()
