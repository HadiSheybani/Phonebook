import pytest
from hamcrest import *
from mock import Mock
import mock
import sys
sys.path.append('../../')

from Framework import ServiceRunner
from Framework import Command
from UseCase import UserRepository

class TestServiceRunner:

    def test_GivenACreateUserCommandThenRunService(self):
        user_repository = Mock(spec=UserRepository)
        service_runner = ServiceRunner(user_repository)
        command = Command('create_user', {'name': 'hadi', 'email': 'test@email.com', 'password': '123456'})
        service_runner.run(command)
        user_repository.create_user.assert_called_once_with('hadi', 'test@email.com', '123456')
