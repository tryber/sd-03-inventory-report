import csv
from inventory_report.importer.importer import Importer


class CsvImporter(Importer):
    @staticmethod
    def import_data(file_name):
        if not file_name.endswith(".csv"):
            raise ValueError("Arquivo inválido")
        with open(file_name, "r") as file:
            read = csv.DictReader(file, delimiter=",")
            return [
                {
                    "id": row["id"],
                    "nome_da_empresa": row["nome_da_empresa"],
                    "data_de_fabricacao": row["data_de_fabricacao"],
                    "data_de_validade": row["data_de_validade"],
                    "nome_do_produto": row["nome_do_produto"],
                    "numero_de_serie": row["numero_de_serie"],
                    "instrucoes_de_armazenamento": row[
                        "instrucoes_de_armazenamento"
                    ],
                }
                for row in read
            ]


# print(CsvImporter.import_data('inventory_report/data/inventory.csv'))
