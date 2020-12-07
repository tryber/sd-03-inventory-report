from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import csv

class Inventory:
    def __init__(self, file_path, report_type):
        self.file_path = file_path
        self.report_type = report_type

    @classmethod
    def import_data(self, file_path, report_type):
        with open(file_path) as csv_file:
            csv_dict = csv.DictReader(csv_file, delimiter=",")

        if report_type == 'simples':
            SimpleReport(csv_dict).generate()
        elif report_type == 'completo':
            CompleteReport(csv_dict).generate()
        else:
            return('Opção inválida')

# Inventory.import_data('../data/inventory.csv', 'simples')