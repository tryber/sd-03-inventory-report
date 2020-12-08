from inventory_report.importer.importer import Importer
import json


class JsonImporter(Importer):
    def import_data(cls, filepath):
        if not filepath.endswith('.json'):
            raise ValueError('Arquivo inválido')
        with open(f"../{filepath}") as json_file:
            output = json.load(json_file)
        return output
