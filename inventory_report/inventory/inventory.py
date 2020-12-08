from os import path
import json
from parsel import Selector
import csv
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    @staticmethod
    def csv_parser(filepath, data_list):
        with open(filepath) as file:
            reader = csv.reader(file, delimiter=",", quotechar='"')
            header, *data = reader
            for row in data:
                current = dict()
                for i in range(len(row)):
                    current[header[i]] = row[i]
                data_list.append(current)

    @staticmethod
    def xml_parser(filepath, data_list):
        with open(filepath) as file:
            content = Selector(text=file.read())
            data = content.css('record').getall()
            for item in data:
                new = Selector(item)
                data_list.append({
                    'id': new.css('id::text').get(),
                    'nome_do_produto': new.css('nome_do_produto::text').get(),
                    'nome_da_empresa': new.css('nome_da_empresa::text').get(),
                    'data_de_fabricacao': new.css(
                        'data_de_fabricacao::text').get(),
                    'data_de_validade': new.css(
                        'data_de_validade::text').get(),
                    'numero_de_serie': new.css('numero_de_serie::text').get(),
                    'instrucoes_de_armazenamento': new.css(
                        'instrucoes_de_armazenamento::text').get()
                })

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
