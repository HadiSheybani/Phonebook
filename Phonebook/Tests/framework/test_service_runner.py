import pytest
from hamcrest import *
from mock import Mock
import mock
from Phonebook.Framework.service_runner import ServiceRunner
from Phonebook.Framework.command import Command
from Phonebook.UseCase.user_repository import UserRepository

class TestServiceRunner:

    def test_GivenACreateUserCommandThenRunService(self):
        user_repository = Mock(spec=UserRepository)
        service_runner = ServiceRunner(user_repository)
        command = Command('create_user', {'name': 'hadi', 'email': 'test@email.com', 'password': '123456'})
        service_runner.run(command)
        user_repository.create_user.assert_called_once_with('hadi', 'test@email.com', '123456')
