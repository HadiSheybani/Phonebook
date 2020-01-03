from .command import Command
import Phonebook.Framework.command_instractions as cm_instruction

from Phonebook.UseCase.user_repository import UserRepository
from Phonebook.UseCase.user_login import UserLogin

class ServiceRunner:
    def __init__(self, parser, user_repository, user_login):
        self.__user_repository = user_repository
        self.__parser = parser
        self.__user_login = user_login
    
    def run(self, input_command):
        service_command = self.__parser.parse(input_command)
        if (service_command.instruction == cm_instruction.CREATE_USER):
            user = self.__user_repository.create_user(service_command.options['name']
                                                    , service_command.options['email']
                                                    , service_command.options['password'])
        if (service_command.instruction == cm_instruction.LOGIN_USER):
            return self.__user_login.login(service_command.options['username'], service_command.options['password'])