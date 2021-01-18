from xml.etree import ElementTree
from inventory_report.importer.importer import Importer


class XmlImporter(Importer):
    @classmethod
    def import_data(cls, path):
        if not path.endswith(".xml"):
            raise ValueError("Arquivo inválido")
        # Reference:
        # https://stackabuse.com/reading-and-writing-xml-files-in-python/
        root = ElementTree.parse(path).getroot()
        products_list = []
        for elem in root:
            product = {}
            for subelem in elem:
                product[subelem.tag] = subelem.text
            products_list.append(product)
        return products_list
