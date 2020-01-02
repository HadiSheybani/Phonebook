from Phonebook.Framework.querybuilder import QueryBuilder
from Phonebook.Framework.database import Database
from Phonebook.Entity.user import User

class UserDataAccess:
    def __init__(self, query_builder, database):
        self.__query_builder = query_builder
        self.__database = database
    
    def save(self, user):
        query = self.__query_builder.save_user_query(user)
        self.__database.execute(query)