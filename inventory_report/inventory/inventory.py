from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport
from xml.etree import ElementTree
import csv
import json


class Inventory:
    @staticmethod
    def parse_csv(path):
        rows = []
        with open(path) as file:
            prod_csv = csv.DictReader(file, delimiter=",", quotechar='"')
            for elem in prod_csv:
                rows.append(elem)
        return rows

    @staticmethod
    def parse_json(path):
        with open(path) as file:
            rows = json.load(file)
            return rows

    @staticmethod
    def parse_xml(path):
        root = ElementTree.parse(path).getroot()
        records = root.findall("record")
        rows = []
        for elem in records:
            temp_dict = {}
            for e in elem:
                temp_dict[e.tag] = e.text
            rows.append(temp_dict)
        return rows

    @staticmethod
    def import_data(path, type):
        data = []
        if path.endswith(".csv"):
            data = Inventory.parse_csv(path)
        elif path.endswith(".json"):
            data = Inventory.parse_json(path)
        else:
            data = Inventory.parse_xml(path)
        if type == "simples":
            return SimpleReport.generate(data)
        else:
            return CompleteReport.generate(data)
