from abc import abstractmethod


class Database():

    @abstractmethod
    def execute(self, query):
        pass