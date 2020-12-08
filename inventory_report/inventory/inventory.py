import csv
import json
from xml.dom.minidom import parse


from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


def getNodeText(node):
    return node.firstChild.nodeValue


class Inventory:
    @classmethod
    def import_data(cls, path, format):
        list = []
        obj = {}
        if path.endswith(".csv"):
            with open(path, "r") as file:
                content = csv.reader(file, delimiter=",", quotechar='"')
                header, *data = content
                for element in data:
                    for i in range(len(header)):
                        obj[header[i]] = element[i]
                    list.append(obj)
                print(list)
            return list
        if path.endswith(".json"):
            with open(path) as file:
                list = json.load(file)
                print(list)
            return list
        if path.endswith(".xml"):
            doc = parse(path)
            records = doc.getElementsByTagName("record")
            for record in records:
                id = getNodeText(record.getElementsByTagName("id")[0])
                nome_do_produto = getNodeText(
                    record.getElementsByTagName("nome_do_produto")[0]
                )
                nome_da_empresa = getNodeText(
                    record.getElementsByTagName("nome_da_empresa")[0]
                )
                data_de_fabricacao = getNodeText(
                    record.getElementsByTagName("data_de_fabricacao")[0]
                )
                data_de_validade = getNodeText(
                    record.getElementsByTagName("data_de_validade")[0]
                )
                numero_de_serie = getNodeText(
                    record.getElementsByTagName("numero_de_serie")[0]
                )
                instrucoes_de_armazenamento = getNodeText(
                    record.getElementsByTagName("instrucoes_de_armazenamento")[
                        0
                    ]
                )
                obj = {
                    "id": id,
                    "nome_do_produto": nome_do_produto,
                    "nome_da_empresa": nome_da_empresa,
                    "data_de_fabricacao": data_de_fabricacao,
                    "data_de_validade": data_de_validade,
                    "numero_de_serie": numero_de_serie,
                    "instrucoes_de_armazenamento": instrucoes_de_armazenamento,
                }
                list.append(obj)
            if format == 'simples':
                return SimpleReport.generate(list)
            elif format == 'completo':
                return CompleteReport.generate(list)


# https://www.kite.com/python/docs/xml.dom.minidom.Document.firstChild
# https://mkyong.com/python/python-read-xml-file-dom-example/
