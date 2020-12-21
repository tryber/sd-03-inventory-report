from inventory_report.importer.importer import Importer


class XmlImporter(Importer):
    def import_data(self, path):
        print("importing")
