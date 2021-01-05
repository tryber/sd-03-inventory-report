import csv
from inventory_report.importer.importer import Importer


class CsvImporter(Importer):
    @classmethod
    def import_data(cls, path):
        if path.endswith(".csv"):
            product_list = []
            with open(path, mode="r") as file:
                products_csv = csv.DictReader(
                    file, delimiter=",", quotechar='"'
                )
                for item in products_csv:
                    product_list.append(item)
            return product_list
        else:
            raise ValueError("Arquivo inválido")


if __name__ == "__main__":
    print(CsvImporter.import_data("inventory_report/data/inventory.csv"))
