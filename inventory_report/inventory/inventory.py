import csv
import json
import xml.etree.ElementTree as ET
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    @staticmethod
    def csv_reader(file_name):
        with open(file_name, "r") as file:
            read = csv.DictReader(file, delimiter=",")
            return [
                {
                    "nome_da_empresa": row["nome_da_empresa"],
                    "data_de_fabricacao": row["data_de_fabricacao"],
                    "data_de_validade": row["data_de_validade"],
                }
                for row in read
            ]

    @classmethod
    def import_data(cls, file_name, mode):
        if file_name.endswith(".csv"):
            data = cls.csv_reader(file_name)
        elif file_name.endswith(".json"):
            data = cls.json_reader(file_name)
        elif file_name.endswith(".xml"):
            data = cls.xml_reader(file_name)

        if mode == "simples":
            return SimpleReport.generate(data)
        return CompleteReport.generate(data)


if __name__ == "__main__":
    print(
        Inventory.import_data(
            "inventory_report/data/inventory.xml", "completo"
        )
    )
