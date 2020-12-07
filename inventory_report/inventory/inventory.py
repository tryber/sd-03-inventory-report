import csv
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    @staticmethod
    def import_data(file_name, mode):
        with open(file_name, "r") as file:
            read = csv.DictReader(file, delimiter=",")
            data = []
            for row in read:
                data.append({
                  "nome_da_empresa": row['nome_da_empresa'],
                  "data_de_fabricacao": row['data_de_fabricacao'],
                  "data_de_validade": row['data_de_validade']
                })
            if mode == "simples":
                return SimpleReport.generate(data)
            if mode == "completo":
                return CompleteReport.generate(data)
