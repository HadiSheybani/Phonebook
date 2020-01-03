import pytest
from mock import Mock
import json
from hamcrest import *
from Phonebook.Framework.querybuilder import QueryBuilder
from Phonebook.Framework.database import Database
from Phonebook.Entity.user import User
from Phonebook.Adapter.user_data_access import UserDataAccess

class TestUserDataAccess:
    def setup_method(self, method):
        self.__query_builder = Mock(spec=QueryBuilder)
        self.__database = Mock(spec=Database)
    
    def test_GivenAUserAndThenUserDataAccessShouldSaveItInDatabase(self):
        test_user_name = 'hadi'
        test_user_email = 'test@email.com'
        test_user_password = '123456'

        user = User(test_user_name
                    , test_user_email
                    , test_user_email
                    , test_user_password)
        self.__query_builder.save_user_query.return_value = json.dumps({"name": user.name
                                                                , "email": user.email
                                                                , "username": user.email
                                                                , "pass_hash": user.pass_hash
                                                                , "contacts": []})

        user_data_access = UserDataAccess(self.__query_builder, self.__database)
        user_data_access.save(user)
        self.__database.execute.assert_called_once_with(self.__query_builder.save_user_query.return_value)

    def test_GivenUsernameThenUserDataAccessShouldReturnUser(self):
        test_user_name = 'hadi'
        test_user_email = 'test@email.com'
        test_user_password = '123456'

        user = User(test_user_name
                    , test_user_email
                    , test_user_email
                    , test_user_password)
        self.__query_builder.get_user_query.return_value = json.dumps({"name": user.name
                                                                , "email": user.email
                                                                , "username": user.email
                                                                , "pass_hash": user.pass_hash
                                                                , "contacts": []})
        self.__database.execute.return_value = user
        user_data_access = UserDataAccess(self.__query_builder, self.__database)
        output_user = user_data_access.get(test_user_email)
        self.__database.execute.assert_called_once_with(self.__query_builder.get_user_query.return_value)
        assert_that(output_user, equal_to(user))
