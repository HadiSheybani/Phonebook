from .command import Command
from .command_instractions import *

class CommandGenerator:

    def create_user(self, command_option):
        return Command(CREATE_USER, command_option)