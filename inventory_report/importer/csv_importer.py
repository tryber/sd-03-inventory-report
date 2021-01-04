
from inventory_report.importer.importer import Importer
from inventory_report.inventory.inventory import Inventory


class CsvImporter(Importer):
    @classmethod
    def import_data(self, path):
        if (not self.verify_type(path, '.csv')):
            raise ValueError('Arquivo inválido')
        return Inventory.csv_method(path)
