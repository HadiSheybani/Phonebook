import pytest
from hamcrest import *
from mock import Mock
import mock
from Phonebook.Framework.service_runner import ServiceRunner
from Phonebook.Framework.command import Command
from Phonebook.UseCase.user_repository import UserRepository
from Phonebook.Framework.parser import Parser
from Phonebook.UseCase.user_login import UserLogin
from Phonebook.Framework.command_instractions import *

class TestServiceRunner:
    def setup_method(self, method):
        self.__parser = Mock(spec=Parser)
        self.__user_repository = Mock(spec=UserRepository)
        self.__user_login = Mock(spec=UserLogin)
    
    def test_GivenACreateUserCommandThenRunService(self):
        input_command = "create_user name=hadi email=test@email.com password=123456"
        service_command = Command(CREATE_USER, {'name': 'hadi', 'email': 'test@email.com', 'password': '123456'})
        self.__parser.parse.return_value = service_command
        service_runner = ServiceRunner(self.__parser, self.__user_repository, None)
        service_runner.run(input_command)
        self.__parser.parse.assert_called_once_with(input_command)
        self.__user_repository.create_user.assert_called_once_with('hadi', 'test@email.com', '123456')
    
    def test_GivenALoginUserCommandThenServiceRunnerShouldReturnToken(self):
        input_command = "login username=test@email.com password=123456"
        service_command = Command(LOGIN_USER, {'username': 'test@email.com', 'password': '123456'})
        correct_token = hash('test@email.com' + str(hash('123456')))
        self.__parser.parse.return_value = service_command
        self.__user_login.login.return_value = correct_token
        service_runner = ServiceRunner(self.__parser, None, self.__user_login)
        token = service_runner.run(input_command)
        self.__parser.parse.assert_called_once_with(input_command)
        self.__user_login.login.assert_called_once_with('test@email.com', '123456')
        assert_that(token, equal_to(correct_token))
