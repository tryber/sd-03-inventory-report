import abc


class Importer:
    @abc.abstractmethod
    def import_data(self):
        raise NotImplementedError
