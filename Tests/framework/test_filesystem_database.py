import pytest
from hamcrest import *
import os
import sys
sys.path.append('../../')
from Framework import FileSystemDatabase

class TestFilesystemDatabase:

    def test_GivenAQueryToDatabaseThenCheckExecution(self):
        pass
        query = 'save={"name": "hadi", "email": "test@email.com"}'
        filesystem_database = FileSystemDatabase()
        filesystem_database.execute(query)
        assert os.path.exists('database/hadi_test@email.com')

