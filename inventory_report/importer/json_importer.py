from inventory_report.importer.importer import Importer
import json


class JsonImporter(Importer):
    @staticmethod
    def convert_json_to_dict(path):
        array = []
        with open(path, mode="r") as file:
            reader = json.load(file)
            for r in reader:
                array.append(r)
        return array

    @classmethod
    def import_data(cls, path):
        if not path.endswith(".json"):
            raise ValueError("Arquivo inválido")
        report = cls.convert_json_to_dict(path)
        return report
