

class Contact:
    def __init__(self, first_name, last_name):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__phone_numbers = dict()
        self.__description = ''

    @property
    def first_name(self):
        return self.first_name

    @property
    def last_name(self):
        return self.last_name
    
    @property
    def phone_numbers(self):
        return self.__phone_numbers
    
    @property
    def description(self):
        return self.__description

    @first_name.setter
    def first_name(self, first_name):
        self.__first_name = first_name
    
    @last_name.setter
    def last_name(self, last_name):
        self.__last_name = last_name

    @description.setter
    def description(self, description):
        self.__description = description
    
    def addPhone(self, phone, name=''):
        if name == '':
            self.__phone_numbers['phone' + len(self.__phone_numbers)] = phone
        else:
            self.__phone_numbers[name] = phone