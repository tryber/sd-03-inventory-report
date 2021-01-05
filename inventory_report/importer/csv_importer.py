from importer.importer import Importer
import csv


class CsvImporter(Importer):
    @classmethod
    def csv_importer(cls, file):
        all_products = []
        with open(file) as products:
            csv_products = csv.DictReader(
                products, delimiter=",", quotechar='"'
            )
            for row in csv_products:
                all_products.append(dict(row))
        return all_products

    @classmethod
    def import_data(cls, file):
        if not file.endswith(".csv"):
            raise ValueError("Arquivo inválido")
        return cls.csv_importer(file)
