import pytest
from mock import Mock
from hamcrest import *
import sys
sys.path.append('../../')
from Framework import Parser
from Framework import CommandGenerator
from Framework import Command

class TestParser:
    def setup_method(self, method):
        self.command_generator = Mock(spec=CommandGenerator)
        self.parser = Parser(self.command_generator)
    
    def test_GivenAWrongCommandThenParserShouldRaiseWrongCommandException(self):
        command_generator = CommandGenerator()
        parser = Parser(command_generator)
        command = 'wrong command'
        try:
            command = parser.parse(command)
            assert False
        except ValueError:
            assert True
    
    def test_GivenACreateUserCommandThenParserShouldReturnCreateCommand(self):
        true_command = Command('create_user', dict())
        command = 'create_user'
        self.command_generator.create_user.return_value = true_command
        output_command = self.parser.parse(command)
        assert_that(output_command, equal_to(true_command))
    
