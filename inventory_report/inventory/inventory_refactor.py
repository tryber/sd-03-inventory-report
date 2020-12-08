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

    def import_data(self, file_path, report_type):
        if (file_path.endswith(".csv")):
            self.data = CsvImporter(file_path)

        if (file_path.endswith(".json")):
            self.data = JsonImporter(file_path)

        if (file_path.endswith(".xml")):
            self.data = XmlImporter(file_path)

        if report_type == 'simples':
            return(SimpleReport.generate(self.data))
        elif report_type == 'completo':
            return(CompleteReport.generate(self.data))
        else:
            return('Opção inválida')

    def __iter__(self):
        return InventoryIterator(self.data)
