from inventory_report.importer.importer import Importer
from inventory_report.inventory.inventory import Inventory


class XmlImporter(Importer):
    @classmethod
    def import_data(self, path):
        if (not self.verify_type(path, '.xml')):
            raise ValueError('Arquivo inválido')
        return Inventory.xml_method(path)
