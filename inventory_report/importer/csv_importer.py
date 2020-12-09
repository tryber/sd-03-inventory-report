from inventory_report.importer.importer import Importer
import csv


class CsvImporter(Importer):
    @classmethod
    def import_data(cls, filename):
        if not filename.endswith(".csv"):
            raise ValueError("Arquivo inválido")
        produtos = []
        with open(filename) as file:
            leitor = csv.DictReader(file, delimiter=",", quotechar='"')
            for el in leitor:
                produtos.append(el)
        return produtos
