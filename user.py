from typing import NamedTuple
from zad5.validator import validator


class User(NamedTuple):
    name: str
    last_name: str
    street: str
    zip_code: str
    pesel: str
    email: str

    @property
    def full_name(self):
        return f"{self.name} {self.last_name}"


class UserRepository:

    def __init__(self):
        self.users = []

    @validator(fields=['zip_code', 'pesel', 'email', 'street', 'last_name'])
    def add_user(self, user: User):
        self.users.append(user)


