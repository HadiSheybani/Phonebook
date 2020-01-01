import abc


class Database:

    @abc.abstractmethod
    def execute(self, query):
        pass