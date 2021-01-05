from datetime import datetime
from operator import itemgetter
from collections import Counter


class SimpleReport:
    @classmethod
    def generate(cls, products):
        oldest_fabrication = min(
            products, key=itemgetter("data_de_fabricacao")
        )["data_de_fabricacao"]
        nearest_shelf_life = min(
            [
                prod
                for prod in products
                if prod["data_de_validade"]
                >= datetime.now().strftime("%Y-%m-%d")
            ],
            key=itemgetter("data_de_validade"),
        )["data_de_validade"]
        most_products_company_name = max(
            Counter(prod["nome_da_empresa"] for prod in products)
        )
        result = ""
        result += f"Data de fabricação mais antiga: {oldest_fabrication}\n"
        result += f"Data de validade mais próxima: {nearest_shelf_life}\n"
        result += f"Empresa com maior quantidade de produtos estocados: {most_products_company_name}\n"
        return result
