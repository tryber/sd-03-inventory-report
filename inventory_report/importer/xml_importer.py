from importer.importer import Importer
import xml.etree.ElementTree as ET


class XmlImporter(Importer):
    @classmethod
    def xml_importer(cls, file):
        root = ET.parse(file).getroot()
        all_products = []
        for record in root.findall("record"):
            product = {}
            for child in record.getchildren():
                product[child.tag] = child.text.strip()
            all_products.append(product)
        return all_products

    @classmethod
    def import_data(cls, file):
        if not file.endswith(".xml"):
            raise ValueError("Arquivo inválido")
        return cls.xml_importer(file)
