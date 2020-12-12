from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport
import csv
import os
import json
from parsel import Selector


class Inventory:
    @staticmethod
    def xml_method(path):
        dataParsed = []
        with open(path) as file:
            xml = Selector(text=file.read())
            data = xml.css("record").getall()
            for product in data:
                tag = Selector(product)
                dataParsed.append(
                    {
                        "id": tag.css("id::text").get(),
                        "nome_do_produto": tag.css(
                            "nome_do_produto::text"
                        ).get(),
                        "nome_da_empresa": tag.css(
                            "nome_da_empresa::text"
                        ).get(),
                        "data_de_fabricacao": tag.css(
                            "data_de_fabricacao::text"
                        ).get(),
                        "data_de_validade": tag.css(
                            "data_de_validade::text"
                        ).get(),
                        "numero_de_serie": tag.css(
                            "numero_de_serie::text"
                        ).get(),
                        "instrucoes_de_armazenamento": tag.css(
                            "instrucoes_de_armazenamento::text"
                        ).get(),
                    }
                )
        return dataParsed

    @staticmethod
    def csv_method(path):
        dataParsed = []
        with open(path) as file:
            reader = csv.DictReader(file, delimiter=",", quotechar='"')
            for elem in reader:
                dataParsed.append(elem)

        return dataParsed

    @staticmethod
    def json_method(path):
        with open(path, "r") as file:
            dataParsed = json.load(file)
        return dataParsed

    @classmethod
    def import_data(cls, filepath, reportType):
        file_name = os.path.basename(filepath)
        dataParsed = []
        if file_name.endswith(".csv"):
            dataParsed = cls.csv_method(filepath)
        elif file_name.endswith(".json"):
            dataParsed = cls.json_method(filepath)
        elif file_name.endswith(".xml"):
            dataParsed = cls.xml_method(filepath)

        if reportType == "simples":
            return SimpleReport.generate(dataParsed)
        else:
            return CompleteReport.generate(dataParsed)
