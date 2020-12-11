from abc import ABC, abstractmethod
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter


class Importer(ABC):
    @abstractmethod
    def CsvImporter(self):
        raise NotImplementedError

    @abstractmethod
    def JsonImporter(self):
        raise NotImplementedError

    @abstractmethod
    def XmlImporter(self):
        raise NotImplementedError
