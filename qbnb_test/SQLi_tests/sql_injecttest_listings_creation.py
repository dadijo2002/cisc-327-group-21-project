import unittest
from qbnb.models import *
from datetime import datetime


class MyTestCase(unittest.TestCase):
    def test_addlistings_throws_exception(self):
        # not exactly sure if this is at all necessary
        self.assertRaises(Exception, add_listing,
                          "Simon riley", "Westchester", 800, 4,
                          "Bourbon", datetime(2024, 1, 7).strftime('Y-%m-%d'))


def test_host():
    i_file = open("Generic_SQLi.txt")
    payloads = i_file.readlines()
    for payload in payloads:
        try:
            add_listing(payload, "Grand Plaza",
                        "Ohio", 600, 4,
                        "Chocolate", "4 bed and bath",
                        datetime(2024, 11, 9).strftime('Y-%m-%d'))
        except (TypeError, ValueError):
            print("An SQL Injection attack was stopped.")

    i_file.close()


def test_title():
    i_file = open("Generic_SQLi.txt")
    payloads = i_file.readlines()
    for payload in payloads:
        try:
            add_listing("John Price", payload,
                        "London", 600, 4,
                        "pop tarts", "4 bed 1 bath",
                        datetime(2022, 11, 17).strftime('Y-%m-%d'))
        except (TypeError, ValueError):
            print("An SQLi attack was stopped")

    i_file.close()


def test_location():
    i_file = open("Generic_SQLi.txt")
    payloads = i_file.readlines()
    for payload in payloads:
        try:
            add_listing("Kestrel", "motel", payload, 600, 4,
                        "pop tarts", "4 bed 1 bath",
                        datetime(2024, 1, 7).strftime('Y-%m-%d'))
        except (TypeError, ValueError):
            print("An SQLi injection was stopped.")

    i_file.close()


def test_ppn():
    i_file = open("Generic_SQLi.txt")
    payloads = i_file.readlines()
    for payload in payloads:
        try:
            add_listing("Kestrel", "motel",
                        "Munich", payload, 10,
                        "pop tarts", "10 bed 10 bath",
                        datetime(2024, 3, 7).strftime('Y-%m-%d'))
        except (TypeError, ValueError):
            print("An SQLi was stopped")

    i_file.close()


def test_guests():
    i_file = open("Generic_SQLi.txt")
    payloads = i_file.readlines()
    for payload in payloads:
        try:
            add_listing("Kestrel", "motel", "Moscow",
                        600, payload, "pop tarts",
                        "4 bed 1 bath",
                        datetime(2024, 2, 7).strftime('Y-%m-%d'))
        except (TypeError, ValueError):
            print("An SQLi was stopped")

    i_file.close()


def test_amenities():
    i_file = open("Generic_SQLi.txt")
    payloads = i_file.readlines()
    for payload in payloads:
        try:
            add_listing("Kestrel", "motel", "Moscow",
                        600, 4,
                        payload, "4 bed 1 bath",
                        datetime(2024, 10, 7).strftime('Y-%m-%d'))
        except (TypeError, ValueError):
            print("An SQLi was stopped")

    i_file.close()


def test_description():
    i_file = open("Generic_SQLi.txt")
    payloads = i_file.readlines()
    for payload in payloads:
        try:
            add_listing("Kestrel", "motel", "Moscow",
                        600, 4, "pop tarts", payload,
                        datetime(2024, 9, 18).strftime('Y-%m-%d'))
        except (TypeError, ValueError):
            print("An SQLi was stopped.")
    i_file.close()


def test_availability():
    i_file = open("Generic_SQLi.txt")
    payloads = i_file.readlines()
    for payload in payloads:
        try:
            add_listing("Kestrel", "motel", "Moscow",
                        600, 4, "pop tarts", "4 bed 1 bath", payload)
        except (TypeError, ValueError):
            print("An SQLi was stopped.")
    i_file.close()
