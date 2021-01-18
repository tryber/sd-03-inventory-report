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

    def import_data(self, path, reportType):
        self.data = [*self.data, *self.importer.import_data(path)]
        return self.generate_report(self.data, reportType)

    @classmethod
    def generate_report(cls, products_list, reportType):
        if reportType == "simples":
            return SimpleReport.generate(products_list)
        else:
            return CompleteReport.generate(products_list)
