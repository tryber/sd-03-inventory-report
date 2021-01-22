from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import csv
import json
import xml


class Inventory:
    @staticmethod
    def csv_conversor(path):
        csv_data = []
        with open(path, mode="r") as file:
            reader = csv.DictReader(file)
            for r in reader:
                csv_data.append(r)
        return csv_data

    @staticmethod
    def json_conversor(path):
        json_data = []
        with open(path, mode="r") as file:
            reader = json.load(file)
            for r in reader:
                json_data.append(r)
        return json_data

    @staticmethod
    def xml_conversor(path):
        root = xml.etree.ElementTree.parse(path).getroot()
        records = root.findall("record")
        x = []
        for elem in records:
            temp_dict = {}
            for e in elem:
                temp_dict[e.tag] = e.text
            x.append(temp_dict)
        return x

    @classmethod
    def import_data(self, path, generate_type):
        data_type = path.split('.')[~0]
        print(data_type)
        conversors = {
            'csv': self.csv_conversor,
            'json': self.json_conversor,
            'xml': self.xml_conversor,
        }
        generators = {
            "simples": SimpleReport.generate,
            "completo": CompleteReport.generate
        }

        dic_data = conversors[data_type](path=path)
        return generators[generate_type](dic_data)
