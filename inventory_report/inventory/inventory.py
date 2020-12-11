from os import path
import csv
import json
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import xml.etree.ElementTree as ET


class Inventory:
    @staticmethod
    def csv_parser(filepath, data_list):
        with open(filepath) as file:
            reader = csv.reader(file, delimiter=",", quotechar='"')
            header, * data = reader
            for row in data:
                current = dict()
                for i in range(len(row)):
                    current[header[i]] = row[i]
                data_list.append(current)
    

    @staticmethod
    def xml_parser(filepath, data_list):
        with open(filepath) as file:
            mydoc = ET.parse(file).getroot()
        for elem in mydoc:
            dict = {}
            for i in elem:
                dict[i.tag] = i.text
            data_list.append(dict)

    @classmethod
    def import_data(self, filepath, report):
        ext = path.splitext(filepath)[1]
        new_list = []
        if ext == '.csv':
            Inventory.csv_parser(filepath, new_list)
        elif ext == '.json':
            with open(filepath) as file:
                new_list = json.load(file)
        elif ext == '.xml':
            Inventory.xml_parser(filepath, new_list)
        if report == 'simples':
            return SimpleReport.generate(new_list)
        else:
            return CompleteReport.generate(new_list)


