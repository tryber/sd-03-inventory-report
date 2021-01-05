from inventory_report.importer.importer import Importer
import xml


class XmlImporter(Importer):
    @staticmethod
    def convert_xml_to_dict(path):
        root = xml.etree.ElementTree.parse(path).getroot()
        records = root.findall("record")
        records_list = []
        for elem in records:
            temp_dict = {}
            for e in elem:
                temp_dict[e.tag] = e.text
            records_list.append(temp_dict)
        return records_list

    @classmethod
    def import_data(cls, path):
        if not path.endswith(".xml"):
            raise ValueError("Arquivo inválido")
        report = cls.convert_xml_to_dict(path)
        return report
