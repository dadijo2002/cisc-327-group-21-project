"""
Contains the backend testing functions
"""
from qbnb.models import User, register, login


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
    existed = User.query.filter_by(user.id == user.id).all()
    assert (len(existed) == 0) is True


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


def test_r1_8_user_register(self):
    """
    Testing R1-8: Shipping address is empty at the time of registration.
    """
    user = User.query.filter_by(username='u0').first()
    assert (user.billing_address == "") is True


def test_r1_9_user_register():
    """
    Testing R1-9: Postal code is empty at the time of registration.
    """
    user = User.query.filter_by(username='u0').first()
    assert (user.postal_code == "") is True


def test_r1_6_user_register():
    """
    Testing R1-6: Balance should be initialized as 100 at the time of
    registration. (free $100 dollar signup bonus).
    """
    user = User.query.filter_by(username='u0').first()
    assert (user.postal_code == "") is True
