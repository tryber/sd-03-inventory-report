from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
from collections.abc import Iterable
from inventory_report.inventory.inventory_iterator import InventoryIterator


class InventoryRefactor(Iterable):
    def __init__(self, importer):
        self.importer = importer
        self.data = []

    def import_data(self, file_name, mode):
        self.data = self.importer.import_data(file_name)
        if mode == "simples":
            return SimpleReport.generate(self.data)
        return CompleteReport.generate(self.data)

    def __iter__(self):
        return InventoryIterator(self.data)
