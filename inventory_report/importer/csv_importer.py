from inventory_report.importer.importer import Importer
from os import path
import csv


class CsvImporter(Importer):
    @classmethod
    def import_data(self, filepath):
        if path.splitext(filepath)[1] != '.csv':
            raise ValueError('Arquivo inválido')
        new_list = []
        with open(filepath) as file:
            reader = csv.reader(file, delimiter=",", quotechar='"')
            header, *data = reader
            for row in data:
                current = dict()
                for i in range(len(row)):
                    current[header[i]] = row[i]
                new_list.append(current)
        return new_list
