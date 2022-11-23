"""
This is a list of test cases for the transaction system.
This is a WIP as the transaction system is improved.
"""

import transaction_system

def test_check_balance(self):
    """
    This function checks the function that checks the balance
    """
    self.balance = 0
    self.unit_cost = 2500
    assert self.check_balance() is False
    self.balance = 6000
    assert self.check_balance() is True
 
def test_check_avail(self):
    """
    This function tests check_avail
    """
    self.availability = False
    assert self.check_avail() is False
    self.availability = True
    assert self.check_avail() is True 

def test_check_dates(self):
    """
    This function tests check_dates
    """

    # test valid dates
    self.start_date = "20230501"
    self.end_date = "20230502"
    assert self.check_dates() is True

    # test less than 2 days
    self.start_date = "20230501"
    self.end_date = "20230501"
    assert self.check_dates() is False

    # test incomplete dates
    self.start_date = "202305"
    self.end_date = "202306"
    assert self.check_dates() is False

    # test start after end
    self.start_date = "20230502"
    self.end_date = "20230501"
    assert self.check_dates() is False

    # test start month invalid
    self.start_date = "20231302"
    self.end_date = "20240101"
    assert self.check_dates() is False

    # test end month invalid
    self.start_date = "20231231"
    self.end_date = "20231301"
    assert self.check_dates() is False

    # test start day invalid
    self.start_date = "20230532"
    self.end_date = "20230601"
    assert self.check_dates() is False

    # test end day invalid
    self.start_date = "20230502"
    self.end_date = "20230532"
    assert self.check_dates() is False

    # test too long duration
    self.start_date = "20230502"
    self.end_date = "20230603"
    assert self.check_dates() is False

    # test year invalid
    self.start_date = "20200502"
    self.end_date = "20200501"
    assert self.check_dates() is False

    # test wrong num of days in month
    self.start_date = "20230431"
    self.end_date = "20230501"
    assert self.check_dates() is False

    self.start_date = "20230603"
    self.end_date = "20230631"
    assert self.check_dates() is False

    # test invalid leap year
    self.start_date = "20230228"
    self.end_date = "20230229"
    assert self.check_dates() is False

    # test valid leap year
    self.start_date = "20240202"
    self.end_date = "20240229"
    assert self.check_dates() is True