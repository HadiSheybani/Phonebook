from .contact import Contact

class User:
    def __init__(self, name, email, username, pass_hash):
        self.__name = name
        self.__email = email
        self.__username = username
        self.__pass_hash = pass_hash
        self.__contacts = list()

    @property
    def name(self):
        return self.__name

    @property
    def email(self):
        return self.__email

    @property
    def username(self):
        return self.__username

    @property
    def pass_hash(self):
        return self.__pass_hash
    
    @name.setter
    def name(self, name):
        self.__name = name
    
    @email.setter
    def email(self, email):
        self.__email = email

    @username.setter
    def username(self, username):
        self.__username = username

    @pass_hash.setter
    def pass_hash(self, pass_hash):
        self.pass_hash = pass_hash

    @property
    def contacts(self):
        return self.__contacts
    
    @contacts.setter
    def contacts(self, contacts):
        self.__contacts = contacts
