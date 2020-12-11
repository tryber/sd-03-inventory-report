from inventory_report.importer.importer import Importer
import json
from os import path


class JsonImporter(Importer):
    @classmethod
    def import_data(x, filepath):
        ext = path.splitext(filepath)[1]
        new_list = []
        if ext == '.json':
            with open(filepath) as file:
                new_list = json.load(file)
            return new_list
        else:
            raise ValueError("Arquivo inválido")