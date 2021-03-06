from abc import abstractmethod

class QueryBuilder():

    @abstractmethod
    def save_user_query(self, user):
        pass

    @abstractmethod
    def get_user_query(self, username):
        pass