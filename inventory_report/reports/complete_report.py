from inventory_report.reports.simple_report import SimpleReport
from collections import Counter


class CompleteReport(SimpleReport):

    @classmethod
    def generate(self, products_data):
        simple_report = super().generate(products_data)
        products_dist = Counter([prod["nome_da_empresa"]
                                for prod in products_data])

        prefix = "\nProdutos Estocados por empresa: \n"
        for name, value in products_dist.items():
            prefix += f"- {name}: {value}\n"
        return simple_report + prefix
