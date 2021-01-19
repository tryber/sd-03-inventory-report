import sys
import re
from inventory_report.inventory.inventory_refactor import InventoryRefactor
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter


def main():
    try:
        if(len(sys.argv) < 3):
            raise EOFError
    except EOFError:
        print("Verifique os argumentos", file=sys.stderr)
    else:
        filepath = sys.argv[1]
        report_type = sys.argv[2]
        file_type = re.search(r'\.(.*)', filepath).group(1)
        importer_handler = {
            "csv": InventoryRefactor(CsvImporter),
            "json": InventoryRefactor(JsonImporter),
            "xml": InventoryRefactor(XmlImporter)
        }
        instance = importer_handler[file_type]
        report = instance.import_data(filepath, report_type)
        return print(report)
