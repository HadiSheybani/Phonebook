import pytest
from hamcrest import *
import json
from Phonebook.Framework.filesystem_querybuilder import FileSystemQueryBuilder
from Phonebook.Entity.user import User
from Phonebook.Entity.contact import Contact

class TestFileSystemQueryBuilder:

    def setup_method(self, method):
        self.filesystem_querybuilder = FileSystemQueryBuilder()
    
    def test_GivenAUserThenCheckOutputJsonString(self):
        contact = Contact('negar', 'sharifi')
        user = User('hadi', 'test@email.com', 'test@email.com', 'pass_hash')
        user.contacts.append(contact)
        correct_query = json.dumps({'name': user.name
                                    , 'email': user.email
                                    , 'username': user.username
                                    , 'pass_hash': user.pass_hash
                                    , 'contacts': [{'first_name': contact.first_name
                                                    , 'last_name': contact.last_name
                                                    , 'phone_numbers': contact.phone_numbers
                                                    , 'description': contact.description}]})
        query = self.filesystem_querybuilder.save_user_query(user)
        assert_that(query, equal_to('save=' + correct_query))
    
    def test_GivenUsernameThenQueyrBuilderShouldReturnGetUserQuery(self):
        username = 'test@email.com'
        correct_query = json.dumps({'username': username})
        query = self.filesystem_querybuilder.get_user_query(username)
        assert_that(query, equal_to('get=' + correct_query))

