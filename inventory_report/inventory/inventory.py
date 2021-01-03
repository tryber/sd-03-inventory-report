from os import path
from parsel import Selector
import csv
import json
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    @staticmethod
    def xml_importer(self, filepath):
        if path.splitext(filepath)[1] != '.xml':
            raise ValueError('Arquivo inválido')
        new_list = []
        with open(filepath) as file:
            content = Selector(text=file.read())
            data = content.css('record').getall()
            for item in data:
                new = Selector(item)
                new_list.append({
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
        return new_list

    @staticmethod
    def csv_importer(self, filepath):
        if path.splitext(filepath)[1] != '.csv':
            raise ValueError('Arquivo inválido')
        new_list = []
        with open(filepath) as file:
            reader = csv.reader(file, delimiter=",", quotechar='"')
            header, *data = reader
            for row in data:
                current = dict()
                for i in range(len(row)):
                    current[header[i]] = row[i]
                new_list.append(current)
        return new_list

    @staticmethod
    def json_importer(self, filepath):
        if path.splitext(filepath)[1] != '.json':
            raise ValueError('Arquivo inválido')
        new_list = []
        with open(filepath) as file:
            new_list = json.load(file)
        return new_list

    @classmethod
    def import_data(self, filepath, reportType):
        dataParsed = []
        if filepath.endswith(".csv"):
            dataParsed = self.csv_importer(self, filepath)
        elif filepath.endswith(".json"):
            dataParsed = self.json_importer(self, filepath)
        elif filepath.endswith(".xml"):
            dataParsed = self.xml_importer(self, filepath)

        if reportType == "simples":
            return SimpleReport.generate(dataParsed)
        else:
            return CompleteReport.generate(dataParsed)
