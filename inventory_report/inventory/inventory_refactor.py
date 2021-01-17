from collections.abc import Iterable
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.inventory.inventory_report import IventoryIterator


class InventoryRefactor(Iterable):
    @classmethod
    def __init__ (cls, path):
        self.data = []
        self.importer = importer

    def __iter__(self):
        return InventoryIterator(self.data)

    @classmethod
    def import_data(self, path, choice):
        self.data = [*self.data, *self.importer.import_data(path)]
        if choice == "simples":
            return SimpleReport.generate(self.data)
        else:
            return CompleteReport.generate(self.data)
