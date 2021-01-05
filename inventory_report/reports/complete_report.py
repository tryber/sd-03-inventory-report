from reports.simple_report import SimpleReport
from collections import Counter


class CompleteReport(SimpleReport):
    @classmethod
    def generate(cls, products):
        simple = super().generate(products)
        data = Counter(prod["nome_da_empresa"] for prod in products)
        storage_prod = "Produtos Estocados por empresa: \n"

        for key, value in data.items():
            storage_prod += f"- {key}, Inc.: {value}\n"

        return f"{simple}\n{storage_prod}"
