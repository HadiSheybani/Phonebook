from Phonebook.Framework.querybuilder import QueryBuilder
from Phonebook.Framework.database import Database
from Phonebook.Entity.user import User
import json

class UserDataAccess:
    def __init__(self, query_builder, database):
        self.__query_builder = query_builder
        self.__database = database
    
    def save(self, user):
        query = self.__query_builder.save_user_query(user)
        self.__database.execute(query)
    
    def get(self, username):
        query = self.__query_builder.get_user_query(username)
        output_user = self.__database.execute(query)
        if (output_user == ""):
            return None
        user_data = json.loads(output_user)
        user = User(user_data['name'], user_data['email'], user_data['username'], user_data['pass_hash'])
        return user