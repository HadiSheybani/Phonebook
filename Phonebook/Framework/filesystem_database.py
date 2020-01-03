from .database import Database
import json
import os

class FileSystemDatabase(Database):
    def __init__(self):
        self.database_dir = 'Phonebook/database/'
    
    def execute(self, query):
        commands = query.split('=')
        if (commands[0] == 'save'):
            self.__save(commands[1])
        if (commands[0] == 'get'):
            return self.__get(commands[1])

    def __save(self, data):
        user_data = json.loads(data)
        file_name = self.__generate_filename(user_data["username"])
        with open(file_name, 'w+') as file_writer:
            file_writer.write(data)

    def __generate_filename(self, username):
        return self.database_dir + username
    
    def __get(self, data):
        user_data = json.loads(data)
        file_name = self.__generate_filename(user_data["username"])
        data = ""
        if os.path.exists('Phonebook/database/test@email.com'):
            with open(file_name, 'r') as file_reader:
                data = file_reader.read()
        return data
        