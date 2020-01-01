import sys
sys.path.append('../')
from Entity import User
from Adapter import UserDataAccess

class UserRepository:
    def __init__(self, user_data_access):
        self.__user_data_access = user_data_access

    def create_user(self, name, email, password):
        pass_hash = hash(password)
        user = User(name, email, email, pass_hash)
        self.__user_data_access.save(user)
        return user