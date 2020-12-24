from inventory_report.importer.importer import Importer
from inventory_report.inventory.inventory import Inventory
import os


class CsvImporter(Importer):
    @staticmethod
    def import_data(path):
        file = os.path.basename(path)
        if (not file.endswith(".csv")):
            raise ValueError('Arquivo inválido')
        return Inventory.parse_csv(path)
