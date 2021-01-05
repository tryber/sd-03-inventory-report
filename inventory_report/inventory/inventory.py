from collections.abc import Iterable
from reports.simple_report import SimpleReport
from reports.complete_report import CompleteReport
from inventory.inventory_iterator import InventoryIterator


class Inventory(Iterable):
    def __init__(self, importer):
        self.data = []
        self.importer = importer

    def __iter__(self):
        return InventoryIterator(self.data)

    @classmethod
    def generate_report(cls, file, request_type):
        if request_type == "simples":
            return SimpleReport.generate(file)
        if request_type == "completo":
            return CompleteReport.generate(file)

    def import_data(self, file, request_type):
        self.data = self.importer.import_data(file)
        return self.generate_report(self.data, request_type)
