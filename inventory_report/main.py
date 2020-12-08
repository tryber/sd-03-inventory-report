import sys
from inventory_report.inventory.inventory_refactor import InventoryRefactor
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter


def get_inventory(file_name):
    if file_name.endswith(".json"):
        inventory = InventoryRefactor(JsonImporter)
    elif file_name.endswith(".csv"):
        inventory = InventoryRefactor(CsvImporter)
    elif file_name.endswith(".xml"):
        inventory = InventoryRefactor(XmlImporter)

    return inventory


def main():
    if len(sys.argv) != 3:
        return print("Verifique os argumentos", file=sys.stderr)
    _, file_name, mode, *_ = sys.argv

    inventory = get_inventory(file_name)
    inventory.import_data(file_name)
    print(inventory.generate(mode))
