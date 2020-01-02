from Phonebook.Framework.initial_app import InitialApp
from Phonebook.Framework.command import Command

def app_run():
    phone_book = InitialApp()
    while True:
        try:
            input_command = input('>> ')
            if input_command == 'exit':
                break;
            phone_book.service_runner.run(input_command)
        except ValueError as error:
            print(error.args[0])