from inventory_report.importer.importer import Importer
import csv
from os import path


class CsvImporter(Importer):
    @classmethod
    def import_data(x, filepath):
        ext = path.splitext(filepath)[1]
        new_list = []
        if ext == '.csv':
            with open(filepath) as file:
                reader = csv.reader(file, delimiter=",", quotechar='"')
                header, * data = reader
                for row in data:
                    current = dict()
                    for i in range(len(row)):
                        current[header[i]] = row[i]
                    new_list.append(current)
            return new_list
        else:
            raise ValueError("Arquivo inválido")
