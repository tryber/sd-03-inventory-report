from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    @classmethod
    def import_data(cls, path, reportType):
        products = cls.import_products(path)
        return cls.generate_report(products, reportType)

    @classmethod
    def import_products(cls, path):
        if path.endswith(".csv"):
            return CsvImporter.import_data(path)
        elif path.endswith(".json"):
            return JsonImporter.import_data(path)
        elif path.endswith(".xml"):
            return XmlImporter.import_data(path)

    @classmethod
    def generate_report(cls, products_list, reportType):
        if reportType == "simples":
            return SimpleReport.generate(products_list)
        else:
            return CompleteReport.generate(products_list)
