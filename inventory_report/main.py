import sys
from inventory_report.inventory.inventory_refactor import InventoryRefactor
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter


def main():

    if len(sys.argv) != 3:
        print("Verifique os argumentos", file=sys.stderr)
    else:
        inventory = ''
        if sys.argv[1].endswith(".csv"):
            print('CSV')
            inventory = InventoryRefactor(CsvImporter)
        elif sys.argv[1].endswith(".json"):
            print('JSON')
            inventory = InventoryRefactor(JsonImporter)
        elif sys.argv[1].endswith(".xml"):
            inventory = InventoryRefactor(XmlImporter)
        report = inventory.import_data(sys.argv[1], sys.argv[2])
        print(report)


if __name__ == "__main__":
    main()
