from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter


class Inventory:

    @classmethod
    def import_data(cls, path, format):
        report = cls.generate_list(path)
        return cls.generate_report(report, format)

    @classmethod
    def generate_list(cls, path):
        if path.endswith(".csv"):
            return CsvImporter.import_data(path)
        elif path.endswith(".json"):
            return JsonImporter.import_data(path)
        elif path.endswith(".xml"):
            return XmlImporter.import_data(path)

    @classmethod
    def generate_report(cls, list, format):
        if format == "simples":
            return SimpleReport.generate(list)
        elif format == "completo":
            return CompleteReport.generate(list)


# https://www.kite.com/python/docs/xml.dom.minidom.Document.firstChild
# https://mkyong.com/python/python-read-xml-file-dom-example/
