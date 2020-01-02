import pytest
from mock import Mock
from hamcrest import *
from Phonebook.Framework.console_parser import ConsoleParser
from Phonebook.Framework.command_generator import CommandGenerator
from Phonebook.Framework.command import Command

class TestParser:
    def setup_method(self, method):
        self.command_generator = Mock(spec=CommandGenerator)
        self.parser = ConsoleParser(self.command_generator)
    
    def test_GivenAWrongCommandThenParserShouldRaiseWrongCommandException(self):
        command = 'wrong command'
        try:
            command = self.parser.parse(command)
            assert False
        except ValueError:
            assert True
    
    def test_GivenACreateUserCommandThenParserShouldReturnCreateCommand(self):
        true_command = Command('create_user', dict())
        command = 'create_user'
        self.command_generator.create_user.return_value = true_command
        output_command = self.parser.parse(command)
        assert_that(output_command, equal_to(true_command))
