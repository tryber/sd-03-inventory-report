import csv
import json
import xml.etree.ElementTree as ET
import re
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    @classmethod
    def import_data(cls, filepath, report_type):
        try:
            file_type = re.search(r'\.(.*)', filepath).group(1)
            fetch_type_handler = {
                'csv': cls.fetch_products_from_csv,
                'json': cls.fetch_products_from_json,
                'xml': cls.fetch_products_from_xml
            }
            product_list = fetch_type_handler[file_type](filepath)
        except FileNotFoundError:
            raise FileNotFoundError('Arquivo inexistente')
        else:
            if(report_type == 'simples'):
                return SimpleReport.generate(product_list)
            return CompleteReport.generate(product_list)

    @classmethod
    def fetch_products_from_csv(cls, filepath):
        with open(filepath, 'r', encoding='utf-8') as csv_file:
            data = csv.reader(csv_file, delimiter=",", quotechar='"')
            headers, *product_data = data
        product_list = []
        for products in product_data:
            product_list.append(
                {header: products[index]
                    for index, header in enumerate(headers)}
            )
        return product_list

    @classmethod
    def fetch_products_from_json(cls, filepath):
        with open(filepath, 'r', encoding='utf-8') as json_file:
            product_list = json.load(json_file)
        return product_list

    @classmethod
    def fetch_products_from_xml(cls, filepath):
        tree = ET.parse(filepath)
        root = tree.getroot()
        product_list = []
        for record_tag in root.findall('record'):
            product_list.append(
                {product.tag: product.text
                    for product in record_tag}
            )
        return product_list


print(Inventory.import_data('inventory_report/data/inventory.csv', 'completo'))
