from inventory_report.importer.importer import Importer
import xml.etree.ElementTree as ET
from os import path


class XmlImporter(Importer):
    @classmethod
    def import_data(x, filepath):
        ext = path.splitext(filepath)[1]
        new_list = []
        if ext == '.xml':
            with open(filepath) as file:
                mydoc = ET.parse(file).getroot()
            for elem in mydoc:
                dict = {}
                for i in elem:
                    dict[i.tag] = i.text
                new_list.append(dict)
            return new_list
        else:
            raise ValueError("Arquivo inválido")
