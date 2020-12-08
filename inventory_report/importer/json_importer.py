import json
from inventory_report.importer.importer import Importer


class JsonImporter(Importer):
    @staticmethod
    def import_data(file_name):
        if not file_name.endswith('.json'):
            raise ValueError("Arquivo inválido")
        with open(file_name, "r") as file:
            return json.load(file)
