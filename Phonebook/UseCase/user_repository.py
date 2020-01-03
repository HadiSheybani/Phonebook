from Phonebook.Entity.user import User
from Phonebook.Adapter.user_data_access import UserDataAccess

class UserRepository:
    def __init__(self, user_data_access):
        self.__user_data_access = user_data_access

    def create_user(self, name, email, password):
        pass_hash = hash(password)
        user = User(name, email, email, pass_hash)
        self.__user_data_access.save(user)
        return user
    
    def get_user(self, username):
        return self.__user_data_access.get(username)