import pytest
from mock import Mock
import json
from hamcrest import *
from Phonebook.Framework.querybuilder import QueryBuilder
from Phonebook.Framework.database import Database
from Phonebook.Entity.user import User
from Phonebook.Adapter.user_data_access import UserDataAccess

class TestUserDataAccess:

    def test_GivenAUserAndThenUserDataAccessShouldSaveItInDatabase(self):
        test_user_name = 'hadi'
        test_user_email = 'test@email.com'
        test_user_password = '123456'

        query_builder = Mock(spec=QueryBuilder)
        database = Mock(spec=Database)
        user = User(test_user_name
                    , test_user_email
                    , test_user_email
                    , test_user_password)
        query_builder.save_user_query.return_value = json.dumps({"name": user.name
                                                                , "email": user.email
                                                                , "username": user.email
                                                                , "pass_hash": user.pass_hash
                                                                , "contacts": []})

        user_data_access = UserDataAccess(query_builder, database)
        user_data_access.save(user)
        database.execute.assert_called_once_with(query_builder.save.return_value)        
