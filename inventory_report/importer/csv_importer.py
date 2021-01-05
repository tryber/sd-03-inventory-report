from inventory_report.importer.importer import Importer
import csv


class CsvImporter(Importer):
    @staticmethod
    def convert_csv_to_dict(path):
        array = []
        with open(path, mode="r") as file:
            reader = csv.DictReader(file)
            for r in reader:
                array.append(r)
        return array

    @classmethod
    def import_data(cls, path):
        if not path.endswith(".csv"):
            raise ValueError("Arquivo inválido")
        report = cls.convert_csv_to_dict(path)
        return report
