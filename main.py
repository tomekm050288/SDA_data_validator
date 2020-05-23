from zad5.user import User, UserRepository
from zad5.validator import print_message
from zad5.my_exceptions import *

user_repository = UserRepository()
user = User("John", "Doe", "firststreet st.", "38-611", "89004567895", "john.doe@gmail.com")
user1 = User("Alice", "Doe", "yellow st.", "38-611", "98028989898", "alice.doe@gmail.com")
user2 = User("Jack", "Doe", "blue st.", "00-909", "94949494949", "jack.doe@gmail.com")

users = [user, user1, user2]

try:
    for user in users:
        user_repository.add_user(user)
    print("All data ar valid")
except InvalidEmailException as exc:
    print_message(user, exc)
except InvalidPeselException as exc:
    print_message(user, exc)
except InvalidZipCodeException as exc:
    print_message(user, exc)
finally:
    print("Validation finished!")