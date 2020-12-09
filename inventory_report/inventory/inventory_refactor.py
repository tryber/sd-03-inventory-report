from inventory_report.inventory.inventory_iterator import InventoryIterator
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter
from collections.abc import Iterable


class InventoryRefactor(Iterable):
    def __init__(self, importer):
        self.importer = importer
        self.data = []

    @staticmethod
    def treatcsv(path):
        return CsvImporter(path)

    @staticmethod
    def treatxml(path):
        return XmlImporter(path)

    @staticmethod
    def call_report(rep_type, output):
        if rep_type == 'simples':
            return(SimpleReport.generate(output))
        elif rep_type == 'completo':
            return(CompleteReport.generate(output))
        else:
            return('Opção inválida')

    @classmethod
    def import_data(self, file_path, report_type):
        output = []
        if (file_path.endswith(".csv")):
            output = InventoryRefactor.treatcsv(file_path)
        elif (file_path.endswith(".json")):
            with open(file_path) as json_file:
                output = JsonImporter(json_file)
        elif (file_path.endswith(".xml")):
            output = InventoryRefactor.treatxml(file_path)

        return InventoryRefactor.call_report(report_type, output)

    def __iter__(self):
        return InventoryIterator(self.data)
