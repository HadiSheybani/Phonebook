import pytest
from hamcrest import *

from Phonebook.Framework.command_generator import CommandGenerator
from Phonebook.Framework.command import Command

class TestCommandGenerator:
    def setup_method(self, method):
        self.__command_generator = CommandGenerator()

    def test_GivenACommandListToCreateUserThenCommandGeneratorShouldReturnValidCommand(self):
        command_options = {'name': 'hadi', 'email': 'test@email.com', 'password': '123456'}
        true_command = Command('create_user', command_options)
        output_command = self.__command_generator.create_user(command_options)
        assert_that(output_command.instruction, equal_to(true_command.instruction))
        assert_that(output_command.options, equal_to(true_command.options))

    def test_GivenCommandOptionWithouNameToCreateUserThenCommandGeneratorShouldRaiseAValueError(self):
        command_options = {'email': 'test@email.com', 'password': '123456'}
        try:
            output_command = self.__command_generator.create_user(command_options)
            assert False
        except ValueError as error:
            assert_that(error.args[0], equal_to("Please Enter Your Name"))
        else:
            assert False

    def test_GivenCommandOptionWithoutEmailToCreateUserThenCommandGeneratorShouldRaiseAValueError(self):
        command_options = {'name': 'hadi', 'password': '123456'}
        try:
            output_command = self.__command_generator.create_user(command_options)
            assert False
        except ValueError as error:
            assert_that(error.args[0], equal_to("Please Enter Your Email"))
        else:
            assert False

    def test_GivenCommandOptionWithoutPasswordToCreateUserThenCommandGeneratorShouldRaiseAValueError(self):
        command_options = {'name': 'hadi', 'email': 'test@email.com',}
        try:
            output_command = self.__command_generator.create_user(command_options)
            assert False
        except ValueError as error:
            assert_that(error.args[0], equal_to("Please Enter Your Password"))
        else:
            assert False