

class Command:
    def __init__(self, instruction, option):
        self.__instruction = instruction
        self.__options = option
    
    @property
    def instruction(self):
        return self.__instruction
    
    @property
    def options(self):
        return self.__options