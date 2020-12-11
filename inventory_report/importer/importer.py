from abc import ABC, abstractmethod


class Importer(ABC):
    @abstractmethod
    def xablau(self):
        raise NotImplementedError
