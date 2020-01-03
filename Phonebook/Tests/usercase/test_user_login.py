import pytest
from mock import Mock
from hamcrest import *
from Phonebook.UseCase.user_login import UserLogin
from Phonebook.UseCase.user_repository import UserRepository
from Phonebook.Entity.user import User

class TestUserLogin:
    def setup_method(self, method):
        self.__user_repository = Mock(spec=UserRepository)
    def test_GivenAValidUserThenUserLoginShouldReturnAValidToken(self):
        username = 'hadi'
        password = '123456'
        self.__user_repository.get_user.return_value.pass_hash = hash(password)
        user_login = UserLogin(self.__user_repository)
        token = user_login.login(username, password)
        assert_that(token, equal_to(hash(username + str(hash(password)))))
    
    def test_GivenUserWithInvalidUsernameDataThenUserLoginShouldRaiseInavlidUsernameOrPasswordError(self):
        username = 'hadi'
        password = '123456'
        self.__user_repository.get_user.return_value = None
        user_login = UserLogin(self.__user_repository)
        
        try:
            token = user_login.login(username, password)
            assert False
        except ValueError as error:
            assert_that(error.args[0], "Invalid Username")
    
    def test_GivenUserWithInvalidPasswordDataThenUserLoginShouldRaiseInavlidUsernameOrPasswordError(self):
        username = 'hadi'
        password = '123456'
        self.__user_repository.get_user.return_value.pass_hash = "invalidhash"
        user_login = UserLogin(self.__user_repository)
        try:
            token = user_login.login(username, password)
            assert False
        except ValueError as error:
            assert_that(error.args[0], "Invalid Password")