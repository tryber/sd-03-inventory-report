from collections.abc import Iterable
from inventory_report.inventory.inventory_iterator import InventoryIterator
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class InventoryRefactor(Iterable):
    def __init__(self, importer):
        self.data = []
        self.importer = importer

    def __iter__(self):
        return InventoryIterator(self.data)

    def import_data(self, path, format):
        self.data.extend(self.importer.import_data(path))
        return self.generate_report(self.data, format)

    @classmethod
    def generate_report(cls, list, format):
        if format == "simples":
            return SimpleReport.generate(list)
        elif format == "completo":
            return CompleteReport.generate(list)
