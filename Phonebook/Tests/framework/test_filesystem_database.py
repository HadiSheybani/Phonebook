import pytest
from hamcrest import *
import os
from Phonebook.Framework.filesystem_database import FileSystemDatabase

class TestFilesystemDatabase:

    def test_GivenAQueryToDatabaseThenCheckExecution(self):
        pass
        query = 'save={"name": "hadi", "email": "test@email.com"}'
        filesystem_database = FileSystemDatabase()
        filesystem_database.execute(query)
        assert os.path.exists('database/hadi_test@email.com')

