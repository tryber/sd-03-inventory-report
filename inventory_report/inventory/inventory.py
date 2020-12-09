from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport
import xml.etree.ElementTree as ET
import json
import csv


class Inventory:
    def __init__(self, file_path, report_type):
        self.file_path = file_path
        self.report_type = report_type

    @staticmethod
    def treatcsv(path):
        with open(f"../{path}") as csv_file:
            csv_dict = csv.DictReader(csv_file, delimiter=",")
            output = []
            for dict in csv_dict:
                output.append(dict)
            return output

    @staticmethod
    def treatxml(path):
        with open(f"../{path}") as xml_file:
            root = ET.parse(xml_file).getroot()
            records = root.findall('record')
            output = []
            for record in records:
                dictionary = {}
                for element in record:
                    dictionary[element.tag] = element.text
                output.append(dictionary)
            return output

    @classmethod
    def import_data(self, file_path, report_type):

        if (file_path.endswith(".csv")):
            output = Inventory.treatcsv(file_path)
        elif (file_path.endswith(".json")):
            with open(f"../{file_path}") as json_file:
                output = json.load(json_file)
        elif (file_path.endswith(".xml")):
            output = Inventory.treatxml(file_path)

        if report_type == 'simples':
            return(SimpleReport.generate(output))
        elif report_type == 'completo':
            return(CompleteReport.generate(output))
        else:
            return('Opção inválida')
