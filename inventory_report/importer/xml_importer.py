from inventory_report.importer.importer import Importer
from xml.etree import ElementTree


class XmlImporter(Importer):
    @classmethod
    def import_data(cls, path):
        if not path.endswith(".xml"):
            raise ValueError("Arquivo inválido")
        root = ElementTree.parse(path).getroot()
        records = root.findall("record")
        records_list = []
        for item in records:
            temp_dict = {}
            for e in item:
                temp_dict[e.tag] = e.text
                records_list.append(temp_dict)
            return records_list


if __name__ == "__main__":
    print(XmlImporter.import_data("inventory_report/data/inventory.xml"))
