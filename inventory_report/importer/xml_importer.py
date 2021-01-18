from inventory_report.importer.importer import Importer
import xml.etree.ElementTree as ET
import re


class XmlImporter(Importer):
    @classmethod
    def import_data(cls, filepath):
        if not re.search('.xml', filepath):
            raise ValueError('Arquivo inválido')
        try:
            tree = ET.parse(filepath)
        except FileNotFoundError:
            raise FileNotFoundError('Arquivo não encontrado')
        else:
            root = tree.getroot()
            product_list = []
            for record_tag in root.findall('record'):
                product_list.append(
                    {product.tag: product.text
                        for product in record_tag}
                )
            return product_list
