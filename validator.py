import re
from typing import List
from zad5.my_exceptions import *


def common_validator(atr, pattern, to_check, Error):
    pattern = re.compile(pattern)
    if result := re.match(pattern, to_check):
        return result
    raise Error(f"Invalid {atr} = {to_check}")


def email_validator(atr, email):
    pattern = r"^[\w.\d-]{,20}@[\w.\d-]{,10}\.\w{,5}$"
    common_validator(atr, pattern, email, InvalidEmailException)


def zip_code_validator(atr, zip_code):
    pattern = r"^[\d]{2}-[\d]{3}$"
    common_validator(atr, pattern, zip_code, InvalidZipCodeException)


def pesel_validator(atr, pesel):
    pattern = r"^[\d]{11}$"
    common_validator(atr, pattern, pesel, InvalidPeselException)


def last_name_validator(atr, last_name):
    pattern = r"^[\w]{,15}$"
    common_validator(atr, pattern, last_name, InvalidLastNameException)


def street_validator(atr, street):
    pattern = r"^[\w]{,15} st.$"
    common_validator(atr, pattern, street, InvalidStreetException)


def validator(fields: List[str]):
    def validator_wrapper(func):
        def wrapper(self, user, *args, **kwargs):
            for field in fields:
                eval(f'{field}_validator(field, user.{field})')
            return func(self, user, *args, **kwargs)
        return wrapper
    return validator_wrapper


def print_message(user, exc):
    print(f"Error: {exc} of {user.full_name}")




# def email_validator(email):
#     pattern = re.compile(r"^[\w.\d-]{,20}@[\w.\d-]{,10}\.\w{,5}$")
#     if result := re.match(pattern, email):
#         return result
#     raise InvalidEmailException("Invalid email address")


# def zip_code_validator(zip_code):
#     pattern = re.compile(r"^[\d]{2}-[\d]{3}$")
#     if result := re.search(pattern, zip_code):
#         return result.group()
#     raise InvalidZipCodeException("Invalid zip-code number")


# def pesel_validator(pesel):
#     pattern = re.compile(r"^[\d]{11}$")
#     if result := re.match(pattern, pesel):
#         return result
#     raise InvalidPeselException("Invalid pesel number")

