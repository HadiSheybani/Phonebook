from Phonebook.Framework.console_parser import ConsoleParser
from Phonebook.Framework.command_generator import CommandGenerator
from Phonebook.Framework.service_runner import ServiceRunner
from Phonebook.UseCase.user_repository import UserRepository
from Phonebook.Adapter.user_data_access import UserDataAccess
from Phonebook.Framework.filesystem_querybuilder import FileSystemQueryBuilder
from Phonebook.Framework.filesystem_database import FileSystemDatabase

class InitialApp:
    def __init__(self):
        self.command_generator = CommandGenerator()
        self.parser = ConsoleParser(command_generator)
        self.query_builder = FileSystemQueryBuilder()
        self.database = FileSystemDatabase()
        self.user_data_access = UserDataAccess(query_builder, database)
        self.user_repository = UserRepository(user_data_access)
        self.service_runner = ServiceRunner(self.parser, self.user_repository)