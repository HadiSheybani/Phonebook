import pytest
from hamcrest import *
import os
from Phonebook.Framework.filesystem_database import FileSystemDatabase

class TestFilesystemDatabase:
    def setup_method(self, method):
        self.__filesystem_database = FileSystemDatabase()
    
    def test_GivenAQueryToDatabaseThenCheckExecution(self):
        query = 'save={"name": "hadi", "email": "test@email.com", "username": "test@email.com"}'
        self.__filesystem_database.execute(query)
        assert os.path.exists('Phonebook/database/test@email.com')
    
    def test_GivenAGetQueryToDatabaseThenDatabaseShouldReturnUserData(self):
        correct_user = '{"name": "hadi", "email": "test@email.com", "username": "test@email.com"}'
        query = 'get={"username": "test@email.com"}'
        user = self.__filesystem_database.execute(query)
        assert_that(user, equal_to(correct_user))
