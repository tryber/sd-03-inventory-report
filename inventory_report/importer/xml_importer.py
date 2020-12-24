from inventory_report.importer.importer import Importer
from inventory_report.inventory.inventory import Inventory
import os


class XmlImporter(Importer):
    @staticmethod
    def import_data(path):
        file = os.path.basename(path)
        if (not file.endswith(".xml")):
            raise ValueError('Arquivo inválido')
        return Inventory.parse_xml(path)
