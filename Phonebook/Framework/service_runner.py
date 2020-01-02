from .command import Command
import Phonebook.Framework.command_instractions as cm_instruction

from Phonebook.UseCase.user_repository import UserRepository

class ServiceRunner:
    def __init__(self, parser, user_repository):
        self.__user_repository = user_repository
        self.__parser = parser
    
    def run(self, input_command):
        service_command = self.__parser.parse(input_command)
        if (service_command.instruction == cm_instruction.CREATE_USER):
            user = self.__user_repository.create_user(service_command.options['name']
                                                    , service_command.options['email']
                                                    , service_command.options['password'])