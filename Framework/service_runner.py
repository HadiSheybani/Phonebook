import sys
sys.path.append('../')
from .command import Command
from .command_instractions import *

from UseCase import UserRepository

class ServiceRunner:
    def __init__(self, user_repository):
        self.__user_repository = user_repository
    
    def run(self, command):
        if (command.instruction == CREATE_USER):
            user = self.__user_repository.create_user(command.options['name'], command.options['email'], command.options['password'])