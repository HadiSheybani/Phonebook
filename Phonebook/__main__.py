import sys
import pytest
from .console_runner import app_run

def main():
    if sys.argv[1] == "runtests":
        pytest.main(['-v', '-x', 'Phonebook/Tests'])
    if sys.argv[1] == 'runapp':
        app_run()


if __name__ == "__main__":
    main()