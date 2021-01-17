import sys
from inventory_report.inventory.inventory_refactor import InventoryRefactor
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter


def main():
    if len(sys.argv) != 3:
        print("Verifique os argumentos", file=sys.stderr)
    
    if sys.argv[1].endswith(".csv"):
        data = InventoryRefactor(CsvImporter).import_data(
            sys.argv[1], sys.argv[2])

        print(data)
        return data
    
    if sys.argv[1].endswith(".json"):
        data = InventoryRefactor(JsonImporter).import_data(
            sys.argv[1], sys.argv[2])

        print(data)
        return data

    if sys.argv[1].endswith(".xml"):
        data = InventoryRefactor(XmlImporter).import_data(
            sys.argv[1], sys.argv[2])

        print(data)
        return data
