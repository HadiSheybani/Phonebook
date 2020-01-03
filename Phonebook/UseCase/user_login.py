from .user_repository import UserRepository
from Phonebook.Entity.user import User

class UserLogin:
    def __init__(self, user_repository):
        self.__user_repository = user_repository
    
    def login(self, username, password):
        user = self.__user_repository.get_user(username)

        if user is None:
            raise ValueError("Invalid Username")
        if hash(password) == user.pass_hash:
            return hash(username + str(user.pass_hash))
        else:
            raise ValueError("Invalid Password")