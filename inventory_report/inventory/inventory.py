import re
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter


class Inventory:
    @classmethod
    def import_data(cls, filepath, report_type):
        try:
            file_type = re.search(r'\.(.*)', filepath).group(1)
            fetch_type_handler = {
                'csv': CsvImporter.import_data,
                'json': JsonImporter.import_data,
                'xml': XmlImporter.import_data
            }
            product_list = fetch_type_handler[file_type](filepath)
        except FileNotFoundError:
            raise FileNotFoundError('Arquivo inexistente')
        else:
            if(report_type == 'simples'):
                return SimpleReport.generate(product_list)
            return CompleteReport.generate(product_list)
