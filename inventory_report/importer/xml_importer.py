from inventory_report.importer.importer import Importer
from xml.etree import ElementTree


class XmlImporter(Importer):
    @classmethod
    def import_data(cls, filename):
        if not filename.endswith(".xml"):
            raise ValueError("Arquivo inválido")
        root = ElementTree.parse(filename).getroot()
        records = root.findall("record")
        produtos = []
        for elemento in records:
            dicionario = {}
            for i in elemento:
                dicionario[i.tag] = i.text
            produtos.append(dicionario)
        return produtos
