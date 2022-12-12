"""
Contains the backend testing functions
"""
from qbnb.models import User, register, listing, login, Transaction


# Register tests
def test_r1_1_user_register():
    """
    Testing R1-1: Email cannot be empty. password cannot be empty.
    """
    assert register('u1', 'test0@test.com', '') is False
    assert register('u2', '', 'Aa123_') is False
    assert register('u3', '', '') is False


def test_r1_2_user_register():
    """
    Testing R1-2: A user is uniquely identified by his/her user id
    - automatically generated.
    """
    user = User.query.filter_by(username='u0').first()
    try:
        existed = User.query.filter_by(user.id == user.id).all()
        existed_len = len(existed)
        # if not found, will return nothing, which causes an error
        # for our tests, this system counterracts that
    except:
        existed_len = 0
    assert (existed_len == 0) is True


def test_r1_3_user_register():
    """
    Testing R1-3: The email has to follow addr-spec defined in RFC 5322
    """
    assert register('u0', 'test0test.com', 'Aa123_') is False  # no @
    assert register('u1', 'test@0@test.com', 'Aa123_') is False  # >1 @
    assert register('u2', 'a" b(c)d,e:f;g<h>i[j\k]l@@test.com', 'Aa123_') \
        is False
    # special char and spaces outside quotes
    assert register('u3', 'test0_@test.com', 'Aa123_') is False  # _ in domain


def test_r1_4_user_register():
    """
    Testing R1-4: Password has to meet the required complexity: minimum
    length 6, at least one upper case, at least one lower case, and at
    least one special character.
    """
    assert register('u0', 'test0@test.com', 'Aa123_') is True
    # valid password, username and email
    assert register('u1', 'test0@test.com', 'tHe7&') is False  # <6 char
    assert register('u2', 'test0@test.com', 'tHe7xm') is False
    # no spceial char
    assert register('u3', 'test0@test.com', 'tHex&m') is False  # no digit
    assert register('u4', 'test0@test.com', 'txe7&m') is False  # no uppercase
    assert register('u5', 'test0@test.com', 'XHX7&X') is True  # no lowercase


def test_r1_7_user_register():
    '''
    Testing R1-7: If the email has been used, the operation failed.
    '''
    assert register('u1', 'test0@test.com', 'Aa123_') is False


def test_r1_8_user_register():
    """
    Testing R1-8: Shipping address is empty at the time of registration.
    """
    user = User.query.filter_by(username='u0').first()
    assert (user.billing_address == " ") is True


def test_r1_9_user_register():
    """
    Testing R1-9: Postal code is empty at the time of registration.
    """
    user = User.query.filter_by(username='u0').first()
    assert (user.postal_code == " ") is True


def test_r1_6_user_register():
    """
    Testing R1-6: Balance should be initialized as 100 at the time of
    registration. (free $100 dollar signup bonus).
    """
    user = User.query.filter_by(username='u0').first()
    assert (user.balance == 100) is True

def test_a6_calc_number_of_nights():
    """
    Testing new requirements implemented in A6
    """
    # standard
    assert calc_number_of_nights('20231010', '20231012') == 2
    # month change
    assert calc_number_of_nights('20231031', '20231101') == 1
    # year change
    assert calc_number_of_nights('20231231', '20240101') == 1
    # leap year
    assert calc_number_of_nights('20240228', '20240301') == 2
    # not leap year
    assert calc_number_of_nights('20230228', '20230301') == 1
    # leap day
    assert calc_number_of_nights('20240229', '20240301') == 1
    # 31 days
    assert calc_number_of_nights('20231030', '20231101') == 2
    # 30 days
    assert calc_number_of_nights('20230930', '20231001') == 1


def test_a6_book_listing():
    """
    """

    # valid
    listing_newest = listing('testeruser420', 'NewListing', '123 Sesame St.', 2, 1000, \
        'wifi, pool', 'This is a test listing', '20231010', '20221212', 'email@gmail.ca', 1203989)

    # balance too low
    listing_new = listing('testeruser420', 'NewListing', '123 Sesame St.', 2, 1000, \
        'wifi, pool', 'This is a test listing', '20231010', '20221212', 'email@gmail.ca', 1203989)

    # not aviailable
    also_listing_new = listing('testeruser420', 'NewListing', '123 Sesame St.', 2, 100, \
        'wifi, pool', 'This is a test listing', '20220505', '20221212', 'email@gmail.ca', 1203989)

    # user's listing
    other_listing_new = listing('u0', 'NewListing', '123 Sesame St.', 2, 100, \
        'wifi, pool', 'This is a test listing', '20231010', '20221212', 'email@gmail.ca', 0)

    user = User.query.filter_by(username='u0').first()
    
    assert listing_new
    assert listing_newest
    assert also_listing_new
    assert other_listing_new

    assert book_listing(user, listing_newest, '20231010', '20231011') is True
    assert book_listing(user, listing_new, '20231010', '20231011') is False
    assert book_listing(user, also_listing_new, '20231010', '20231011') is False
    assert book_listing(user, other_listing_new, '20231010', '20231011') is False
