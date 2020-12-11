from abc import ABC, abstractmethod


class Importer(ABC):
    @abstractmethod
    def importer(self):
        pass
