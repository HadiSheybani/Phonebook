from Phonebook.Framework.console_parser import ConsoleParser
from Phonebook.Framework.command_generator import CommandGenerator
from Phonebook.Framework.service_runner import ServiceRunner
from Phonebook.UseCase.user_repository import UserRepository
from Phonebook.Adapter.user_data_access import UserDataAccess
from Phonebook.Framework.filesystem_querybuilder import FileSystemQueryBuilder
from Phonebook.Framework.filesystem_database import FileSystemDatabase
from Phonebook.UseCase.user_login import UserLogin

class InitialApp:
    def __init__(self):
        self.command_generator = CommandGenerator()
        self.parser = ConsoleParser(self.command_generator)
        self.query_builder = FileSystemQueryBuilder()
        self.database = FileSystemDatabase()
        self.user_data_access = UserDataAccess(self.query_builder, self.database)
        self.user_repository = UserRepository(self.user_data_access)
        self.user_login = UserLogin(self.user_repository)
        self.service_runner = ServiceRunner(self.parser, self.user_repository, self.user_login)