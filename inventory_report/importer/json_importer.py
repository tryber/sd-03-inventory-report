from importer.importer import Importer
import json


class JsonImporter(Importer):
    @classmethod
    def json_importer(cls, file):
        all_products = []
        with open(file) as products:
            json_products = json.load(products)
            for prod in json_products:
                all_products.append(prod)
        return all_products

    @classmethod
    def import_data(cls, file):
        if not file.endswith(".json"):
            raise ValueError("Arquivo inválido")
        return cls.json_importer(file)
