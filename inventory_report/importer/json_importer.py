from inventory_report.importer.importer import Importer
from os import path
import json


class JsonImporter(Importer):
    @classmethod
    def import_data(self, filepath):
        if path.splitext(filepath)[1] != '.json':
            raise ValueError('Arquivo inválido')
        new_list = []
        with open(filepath) as file:
            new_list = json.load(file)
        return new_list
