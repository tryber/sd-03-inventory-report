from inventory_report.importer.importer import Importer
import re
import json


class JsonImporter(Importer):
    @classmethod
    def import_data(cls, filepath):
        if not re.search('.json', filepath):
            raise ValueError('Arquivo inválido')
        try:
            with open(filepath, 'r', encoding='utf-8') as json_file:
                product_list = json.load(json_file)
        except FileNotFoundError:
            raise FileNotFoundError('Arquivo não encontrado')
        else:
            return product_list
