from inventory_report.importer.importer import Importer
from csv import DictReader


class CsvImporter(Importer):

    @classmethod
    def import_data(cls, path):
        if not path.endswith(".csv"):
            raise ValueError("Arquivo inválido")
        products_list = []
        with open(path) as file:
            csv_reader = DictReader(file, delimiter=",", quotechar='"')
            for product in csv_reader:
                products_list.append(product)
        return products_list
