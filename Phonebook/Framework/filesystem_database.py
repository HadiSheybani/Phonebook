from .database import Database
import json

class FileSystemDatabase(Database):
    def __init__(self):
        self.database_dir = 'database/'
    
    def execute(self, query):
        commands = query.split('=')
        if (commands[0] == 'save'):
            self.__save(commands[1])
    
    def __save(self, data):
        user_data = json.loads(data)
        file_name = self.__generate_filename(user_data['name'], user_data['email'])
        with open(file_name, 'w+') as file_writer:
            file_writer.write(data)

    def __generate_filename(self, name, email):
        return self.database_dir + name + '_' + email