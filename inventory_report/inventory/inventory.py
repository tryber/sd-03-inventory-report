from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import csv
import json
import xml


class Inventory:
    @staticmethod
    def convert_csv_to_dict(path):
        array = []
        with open(path, mode="r") as file:
            reader = csv.DictReader(file)
            for r in reader:
                array.append(r)
        return array

    @staticmethod
    def convert_json_to_dict(path):
        array = []
        with open(path, mode="r") as file:
            reader = json.load(file)
            for r in reader:
                array.append(r)
        return array

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
    def covert_data_to_dict(cls, path):
        report = ""
        if path.endswith(".csv"):
            report = cls.convert_csv_to_dict(path)

        if path.endswith(".json"):
            report = cls.convert_json_to_dict(path)

        if path.endswith(".xml"):
            report = cls.convert_xml_to_dict(path)

        return report

    @classmethod
    def import_data(cls, path, report_type):
        report = cls.covert_data_to_dict(path)

        if report_type == "simples":
            return SimpleReport.generate(data=report)
        if report_type == "completo":
            return CompleteReport.generate(data=report)


Inventory.import_data("inventory_report/data/inventory.csv", "simple")
