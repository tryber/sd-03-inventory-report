from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import csv
import json


class Inventory:
    def __init__(self, file_path, report_type):
        self.file_path = file_path
        self.report_type = report_type

    @classmethod
    def import_data(self, file_path, report_type):
        if (file_path.endswith(".csv")):
            with open(file_path) as csv_file:
                csv_dict = csv.DictReader(csv_file, delimiter=",")
                csv_react = []
                for dict in csv_dict:
                    csv_react.append(dict)
                if report_type == 'simples':
                    print(SimpleReport(csv_react).generate())
                elif report_type == 'completo':
                    print(CompleteReport(csv_react).generate())
                else:
                    return('Opção inválida')
        if (file_path.endswith(".json")):
            with open(file_path) as json_file:
                j_file = json.load(json_file)
                if report_type == 'simples':
                    print(SimpleReport(j_file).generate())
                elif report_type == 'completo':
                    print(CompleteReport(j_file).generate())
                else:
                    return('Opção inválida')


# Inventory.import_data('../data/inventory.json', 'simples')
