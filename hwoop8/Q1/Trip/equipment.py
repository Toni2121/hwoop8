from abc import ABC, abstractmethod


class Equipment(ABC):
    @abstractmethod
    def get_weight(self):
        pass
