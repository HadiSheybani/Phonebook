from .command import Command
from .command_instractions import *

class CommandGenerator:

    def create_user(self, command_option):
        if "name" not in command_option:
            raise ValueError("Please Enter Your Name")
        if "email" not in command_option:
            raise ValueError("Please Enter Your Email")
        if "password" not in command_option:
            raise ValueError("Please Enter Your Password")
        return Command(CREATE_USER, command_option)