import csv
import json
import xml.etree.ElementTree as ET
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    @classmethod
    def converter_csv(cls, path):
        with open(path, "r") as file:
            csv_dict = csv.DictReader(file)
            data = [value for value in csv_dict]
        return data

    @classmethod
    def converter_json(cls, path):
        with open(path, "r") as file:
            json_dict = json.load(file)
            data = [value for value in json_dict]
        return data

    @classmethod
    def converter_xml(cls, path):
        tree = ET.parse(path)
        root = tree.getroot().findall('record')
        data = []
        for elem in root:
            dicionario = {}
            for item in elem:
                dicionario[item.tag] = item.text
            data.append(dicionario)

        return data

    @classmethod
    def converter(cls, path):
        data = []
        if path.endswith(".csv"):
            data = cls.converter_csv(path)
        if path.endswith(".json"):
            data = cls.converter_json(path)
        if path.endswith(".xml"):
            data = cls.converter_xml(path)
        return data

    @classmethod
    def import_data(cls, path, choice):
        data = cls.converter(path)

        if choice == "simples":
            return SimpleReport.generate(data)

        return CompleteReport.generate(data)
