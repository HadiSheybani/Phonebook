import sys
import pytest

if __name__ == "__main__":
    if sys.argv[1] == "runtests":
        pytest.main(['-v', '-x', 'Phonebook/Tests'])
    pass