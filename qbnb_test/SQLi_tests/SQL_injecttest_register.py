from qbnb.models import User 

payloads= open('Generic_SQLI.txt', 'r' )
lines= payloads.readlines()

def test_username_parameter():
    for line in lines:
        try:
            register("u0","test0@yahoo.com", "_Aa1234", "_Aa1234" )
        except (TypeError,ValueError):
            print("An SQL Injection attack was stopped.")

def test_email_parameter():
    for line in lines:
        try:
            register("u1","test1yahoo.com", "_Aa1234", "_Aa1234" )
        except (TypeError,ValueError):
            print("An SQL Injection attack was stopped.")


def test_password_parameter():
    for line in lines:
        try:
            register("u2","test2@yahoo.com", "_Aa1234", "_Aa1234" )
        except (TypeError,ValueError):
            print("An SQL Injection attack was stopped.")

def test_password2_parameter():
    for line in lines:
        try:
            register("u3","test3@yahoo.com", "_Aa1234", "_Aa1234" )
        except (TypeError,ValueError):
            print("An SQL Injection attack was stopped.")

payloads.close()