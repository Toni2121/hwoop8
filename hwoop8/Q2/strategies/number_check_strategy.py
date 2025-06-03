from abc import ABC, abstractmethod


class NumberCheckStrategy(ABC):
    @abstractmethod
    def check(self, number):
        pass

    @abstractmethod
    def get_name(self):
        pass
