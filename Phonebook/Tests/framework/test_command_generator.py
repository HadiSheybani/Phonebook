import pytest
from hamcrest import *

from Phonebook.Framework.command_generator import CommandGenerator
from Phonebook.Framework.command import Command

class TestCommandGenerator:

    def test_GivenACommandListToCreateUserThenCommandGeneratorShouldReturnValidCommand(self):
        command_generator = CommandGenerator()
        command_options = {'name': 'hadi', 'email': 'test@email.com', 'password': '123456'}
        true_command = Command('create_user', command_options)
        output_command = command_generator.create_user(command_options)
        assert_that(output_command.instruction, equal_to(true_command.instruction))
        assert_that(output_command.options, equal_to(true_command.options))