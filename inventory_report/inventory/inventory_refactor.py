from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.inventory.inventory_iterator import InventoryIterator
from collections.abc import Iterable


class InventoryRefactor(Iterable):
    def __init__(self, importer):
        self.importer = importer
        self.data = []

    def __iter__(self):
        return InventoryIterator(self.data)

    def import_data(self, filepath, report_type):
        try:
            product_list = self.importer.import_data(filepath)
            self.data.extend(product_list)
        except FileNotFoundError:
            raise FileNotFoundError('Arquivo inexistente')
        else:
            if(report_type == 'simples'):
                return SimpleReport.generate(product_list)
            return CompleteReport.generate(product_list)
