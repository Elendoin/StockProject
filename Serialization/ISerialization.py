from abc import ABC, abstractmethod

class Serialization(ABC):
    @abstractmethod
    def Serialize(self, data, name):
        pass