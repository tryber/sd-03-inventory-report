from inventory_report.importer.importer import Importer
from inventory_report.inventory.inventory import Inventory


class JsonImporter(Importer):
    @classmethod
    def import_data(self, path):
        if path.endswith(".json"):
            return Inventory.json_conversor(path)
        raise ValueError("Arquivo inválido")
