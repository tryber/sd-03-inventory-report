import json
from inventory_report.importer.importer import Importer


class JsonImporter(Importer):
    @classmethod
    def import_data(cls, path):
        if not path.endswith(".json"):
            raise ValueError("Arquivo inválido")
        with open(path) as file:
            return(json.load(file))


if __name__ == "__main__":
    print(JsonImporter.import_data('inventory_report/data/inventory.json'))
