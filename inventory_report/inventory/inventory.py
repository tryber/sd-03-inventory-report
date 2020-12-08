from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import csv
import json
import xml.etree.ElementTree as ET


class Inventory:
    def __init__(self, file_path, report_type):
        self.file_path = file_path
        self.report_type = report_type

    @classmethod
    def import_data(self, file_path, report_type):

        if (file_path.endswith(".csv")):
            with open(file_path) as csv_file:
                csv_dict = csv.DictReader(csv_file, delimiter=",")
                output = []
                for dict in csv_dict:
                    output.append(dict)

        if (file_path.endswith(".json")):
            with open(file_path) as json_file:
                output = json.load(json_file)

        if (file_path.endswith(".xml")):
            with open(file_path) as xml_file:
                root = ET.parse(xml_file).getroot()
                records = root.findall('record')
                output = []
                for record in records:
                    dictionary = {}
                    for element in record:
                        dictionary[element.tag] = element.text
                    output.append(dictionary)

        if report_type == 'simples':
            return(SimpleReport.generate(output))
        elif report_type == 'completo':
            return(CompleteReport.generate(output))
        else:
            return('Opção inválida')
