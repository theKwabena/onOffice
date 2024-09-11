from abc import ABC, abstractmethod

class BaseAPIService:

    @abstractmethod
    def get_estates(self):
        raise NotImplementedError


