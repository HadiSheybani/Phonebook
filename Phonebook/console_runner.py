from Phonebook.Framework.initial_app import InitialApp
from Phonebook.Framework.command import Command

def app_run():
    phone_book = InitialApp()
    login_token = 0
    while True:
        try:
            if login_token == 0:
                input_command = input('>> ')
                if input_command == 'exit':
                    break;
                if (input_command.split(' ')[0] == 'login_user'):
                    login_token = phone_book.service_runner.run(input_command)
                else:
                    phone_book.service_runner.run(input_command)
            else:
                input_command = input(str(login_token)+ ' >> ')
                if input_command == 'exit':
                    break;
                if (input_command.split(' ')[0] == 'login_user'):
                    continue;
                phone_book.service_runner.run(input_command)
        except ValueError as error:
            print(error.args[0])