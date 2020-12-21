from inventory_report.importer.importer import Importer
from inventory_report.inventory.inventory import Inventory


class JsonImporter(Importer):
    @classmethod
    def import_data(self, path):
        if (not self.verify_type(path, '.json')):
            raise ValueError('Arquivo inválido')
        return Inventory.json_method(path)
