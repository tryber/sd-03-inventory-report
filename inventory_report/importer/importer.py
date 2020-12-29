from abc import ABC, abstractmethod
import os


class Importer(ABC):
    @abstractmethod
    def import_data(self):
        raise NotImplementedError

    @staticmethod
    def verify_type(path, type):
        file_name = os.path.basename(path)
        if (not file_name.endswith(type)):
            return False
        return True
