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

    def import_data(self, path, generator_type):
        self.data = [*self.data, *self.importer.import_data(path)]
        generators = {
            "simples": SimpleReport.generate,
            "completo": CompleteReport.generate
        }
        return generators[generator_type](self.data)
