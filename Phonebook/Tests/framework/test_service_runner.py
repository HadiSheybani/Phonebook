import pytest
from hamcrest import *
from mock import Mock
import mock
from Phonebook.Framework.service_runner import ServiceRunner
from Phonebook.Framework.command import Command
from Phonebook.UseCase.user_repository import UserRepository
from Phonebook.Framework.parser import Parser

class TestServiceRunner:

    def test_GivenACreateUserCommandThenRunService(self):
        parser = Mock(spec=Parser)
        user_repository = Mock(spec=UserRepository)
        input_command = "create_user name=hadi email=test@email.com password=123456"
        service_command = Command('create_user', {'name': 'hadi', 'email': 'test@email.com', 'password': '123456'})
        parser.parse.return_value = service_command
        service_runner = ServiceRunner(parser, user_repository)
        service_runner.run(input_command)
        parser.parse.assert_called_once_with(input_command)
        user_repository.create_user.assert_called_once_with('hadi', 'test@email.com', '123456')
