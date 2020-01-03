import pytest
from hamcrest import *
from mock import Mock
from Phonebook.UseCase.user_repository import UserRepository
from Phonebook.Adapter.user_data_access import UserDataAccess
from Phonebook.Entity.user import User

class TestUserRepository:
    def setup_method(self, method):
        self.__user_data_access = Mock(spec=UserDataAccess)
    
    def test_GivenUserDataWhenRunCreateUserThenUserRepositoryShouldCreateAndSaveInDataBase(self):
        test_user_name = 'hadi'
        test_user_email = 'test@email.com'
        test_user_password = '123456'
        user = User(test_user_name
                    , test_user_email
                    , test_user_email
                    , hash(test_user_password))
        user_repository = UserRepository(self.__user_data_access)
        output_user = user_repository.create_user(test_user_name
                                                , test_user_email
                                                , test_user_password)
        self.__user_data_access.save.assert_called_once()
        assert_that(output_user, equal_to(output_user))
    
    def test_GivenUsernameThenUserRepositoryShouldReturnUser(self):
        self.__user_data_access.get.return_value = None
        user_repository = UserRepository(self.__user_data_access)
        output_user = user_repository.get_user('hadi')
        assert_that(output_user, equal_to(None))
        self.__user_data_access.get.assert_called_once()