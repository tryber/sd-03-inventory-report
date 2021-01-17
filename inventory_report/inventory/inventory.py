import csv
import json
import xml.etree.ElementTree as ET
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    @classmethod
    def csv_converter(cls, path):
        with open(path, "r") as file:
            csv_dict = csv.DictReader(file)
            data = [value for value in csv_dict]

        return data

    @classmethod
    def json_converter(cls, path):
        with open(path, "r") as file:
            json_dict = json.load(file)
            data = [value for value in json_dict]

        return data

    @classmethod
    def xml_converter(cls, path):
        tree = ET.parse(path)
        root = tree.getroot().findall('record')
        data = []
        for elem in root:
            new_dict = {}
            for item in elem:
                new_dict[item.tag] = item.text
            data.append(new_dict)
        return data

    @classmethod
    def get_type(cls, path):
        data = []
        if path.endswith(".csv"):
            data = cls.csv_converter(path)
        elif path.endswith(".json"):
            data = cls.json_converter(path)
        else:
            data = cls.xml_converter(path)

        return data

    @classmethod
    def import_data(cls, path, choice):
        data = cls.csv_converter(path)

        if choice == "simples":
            return SimpleReport.generate(data)
        else:
            return CompleteReport.generate(data)
