import sys
from inventory_report.inventory.inventory_refactor import InventoryRefactor
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter


def importInventory(path):

    data_type = path.split('.')[~0]
    inventories = {
        'csv': InventoryRefactor(CsvImporter),
        'json': InventoryRefactor(JsonImporter),
        'xml': InventoryRefactor(XmlImporter),
    }
    return inventories[data_type]


def main():
    if len(sys.argv) != 3:
        return print("Verifique os argumentos", file=sys.stderr)
    inventory = importInventory(sys.argv[1])
    report = inventory.import_data(sys.argv[1], sys.argv[2])
    print(report)


if __name__ == "__main__":
    main()
