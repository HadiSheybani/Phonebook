from .querybuilder import QueryBuilder
import json
import sys
sys.path.append('../')
from Entity import User
from Entity import Contact

class FileSystemQueryBuilder(QueryBuilder):

    def save_user_query(self, user):
        user_data = dict()
        user_data['name'] = user.name
        user_data['email'] = user.email
        user_data['username'] = user.username
        user_data['pass_hash'] = user.pass_hash
        user_contacts = list()
        contacts = user.contacts
        for contact in contacts:
            contact_data = dict()
            contact_data['first_name'] = contact.first_name()
            contact_data['last_name'] = contact.last_name()
            contact_data['phone_numbers'] = contact.phone_numbers()
            contact_data['description'] = contact.description()
            user_contacts.append(contact_data)
        user_data['contacts'] = user_contacts
        query = json.dumps(user_data)
        query = 'save ' + query
        return query