import sys
from inventory_report.inventory.inventory_refactor import InventoryRefactor
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter


def main():
    try:
        _, file_name, mode = sys.argv
    except ValueError:
        return print("Verifique os argumentos", file=sys.stderr)

    if file_name.endswith(".json"):
        inventory = InventoryRefactor(JsonImporter)
    elif file_name.endswith(".csv"):
        inventory = InventoryRefactor(CsvImporter)
    elif file_name.endswith(".xml"):
        inventory = InventoryRefactor(XmlImporter)

    inventory.import_data(file_name)
    print(inventory.generate(mode))
