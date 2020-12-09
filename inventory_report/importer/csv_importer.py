import csv
from inventory_report.importer.importer import Importer


class CsvImporter(Importer):
    @classmethod
    def import_data(cls, path):
        if not path.endswith(".csv"):
            raise ValueError("Arquivo inválido")
        list = []
        with open(path, "r") as file:
            content = csv.reader(file, delimiter=",", quotechar='"')
            header, *data = content
            for element in data:
                obj = {}
                for i in range(len(header)):
                    teste = header[i]
                    obj[teste] = element[i]
                list.append(obj)
        return list
