import sys
from inventory_report.inventory.inventory_refactor import InventoryRefactor
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter


def importInventory(name):
    if name.endswith(".csv"):
        print('CSV')
        return InventoryRefactor(CsvImporter)
    if name.endswith(".json"):
        print('JSON')
        return InventoryRefactor(JsonImporter)
    if name.endswith(".xml"):
        return InventoryRefactor(XmlImporter)


def main():
    if len(sys.argv) != 3:
        return print("Verifique os argumentos", file=sys.stderr)
    inventory = importInventory(sys.argv[1])
    report = inventory.import_data(sys.argv[1], sys.argv[2])
    print(report)


if __name__ == "__main__":
    main()
