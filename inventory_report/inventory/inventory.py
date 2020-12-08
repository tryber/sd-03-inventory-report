import csv
from reports.simple_report import SimpleReport

base = "inventory_report/data/inventory.csv"
simple = SimpleReport


class inventory:
    @classmethod
    def import_data(self, base, simple):
        self.base = base
        self.simple = simple
        try:
            if not self.base.endswith(".csv"):
                raise ValueError("Arquivo invalido")
            with open(base, "r") as file:
                file = csv.DictReader(file, delimiter=";")
        except FileNotFoundError:
            raise ValueError("Arquivo invalido")
        else:
            return simple(file)
