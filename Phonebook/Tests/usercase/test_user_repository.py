import pytest
from hamcrest import *
from mock import Mock
from Phonebook.UseCase.user_repository import UserRepository
from Phonebook.Adapter.user_data_access import UserDataAccess
from Phonebook.Entity.user import User

class TestUserRepository:

    def test_GivenUserDataWhenRunCreateUserThenUserRepositoryShouldCreateAndSaveInDataBase(self):
        test_user_name = 'hadi'
        test_user_email = 'test@email.com'
        test_user_password = '123456'
        user_data_access = Mock(spec=UserDataAccess)
        user = User(test_user_name
                    , test_user_email
                    , test_user_email
                    , hash(test_user_password))
        user_repository = UserRepository(user_data_access)
        output_user = user_repository.create_user(test_user_name
                                                , test_user_email
                                                , test_user_password)
        user_data_access.save.assert_called_once()
        assert_that(output_user, equal_to(output_user))