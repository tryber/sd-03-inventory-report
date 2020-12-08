from inventory_report.importer.importer import Importer
import xml.etree.ElementTree as ET


class XmlImporter(Importer):
    @staticmethod
    def import_data(file_name):
        if not file_name.endswith(".xml"):
            raise ValueError("Arquivo inválido")
        with open(file_name, "r") as file:
            root = ET.parse(file).getroot()
            return [
                {
                    "nome_da_empresa": record.find("nome_da_empresa").text,
                    "data_de_fabricacao": record.find(
                        "data_de_fabricacao"
                    ).text,
                    "data_de_validade": record.find("data_de_validade").text,
                    "id": record.find("id").text,
                    "nome_do_produto": record.find("nome_do_produto").text,
                    "numero_de_serie": record.find("numero_de_serie").text,
                    "instrucoes_de_armazenamento": record.find(
                        "instrucoes_de_armazenamento"
                    ).text,
                }
                for record in root.iter("record")
            ]
