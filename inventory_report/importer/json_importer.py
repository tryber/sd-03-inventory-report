from inventory_report.importer.importer import Importer
from inventory_report.inventory.inventory import Inventory
import os


class JsonImporter(Importer):
    @staticmethod
    def import_data(path):
        file = os.path.basename(path)
        if (not file.endswith(".json")):
            raise ValueError('Arquivo inválido')
        return Inventory.parse_json(path)
