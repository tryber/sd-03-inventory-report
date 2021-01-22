from inventory_report.importer.importer import Importer
from inventory_report.inventory.inventory import Inventory


class XmlImporter(Importer):
    @classmethod
    def import_data(self, path):
        if path.endswith(".xml"):
            return Inventory.xml_conversor(path)
        raise ValueError("Arquivo inválido")
