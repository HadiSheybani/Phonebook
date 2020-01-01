from .database import Database

class FileSystemDatabase(Database):

    def execute(self, query):
        print('Filesystem Database query excute.')