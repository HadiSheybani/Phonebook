from Framework.command_generator import CommandGenerator

class Parser:
    def __init__(self, command_generator):
        self.__commands = ['create_user',]
        self.__command_generator = command_generator

    def parse(self, command_str):
        command_list = command_str.split(' ')
        instruction = command_list[0]
        if instruction not in self.__commands:
            raise ValueError("Wrong Commnad")
        command_index = self.__commands.index(instruction)
        return self.__create_command(command_index, command_list[1:])
        
        
    def __create_command(self, command_index, command_list):
        command_options = dict()
        for option in command_list:
            option_name, option_value = option.split('=')
            command_option[option_name] = option_value
        if (command_index == 0):
            return self.__command_generator.create_user(command_options)
