from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
from collections.abc import Iterable
from inventory_report.inventory.inventory_iterator import InventoryIterator


class InventoryRefactor(Iterable):
    def __init__(self, importer):
        self.importer = importer
        self.data = []

    def import_data(self, file_name):
        self.data += self.importer.import_data(file_name)

    def generate(self, mode):
        if mode == "simples":
            relatory = SimpleReport.generate(self.data)
        elif mode == "completo":
            relatory = CompleteReport.generate(self.data)
        return relatory

    def __iter__(self):
        return InventoryIterator(self.data)
