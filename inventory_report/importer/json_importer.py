from inventory_report.importer.importer import Importer
import json


class JsonImporter(Importer):
    @classmethod
    def import_data(cls, filename):
        if not filename.endswith(".json"):
            raise ValueError("Arquivo inválido")
        with open(filename) as json_file:
            conteudo = json_file.read()
            produtos = json.loads(conteudo)
        return produtos
