from abc import ABC, abstractmethod

class QueryBuilder(ABC):

    @abstractmethod
    def save_user_query(self, user):
        pass