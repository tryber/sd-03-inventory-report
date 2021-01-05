from datetime import datetime
from collections import Counter


class SimpleReport:
    @staticmethod
    def company_counter(self, prodList):
        companies = [elem["nome_da_empresa"] for elem in prodList]
        companies_counter = Counter(companies)
        return companies_counter

    @classmethod
    def generate(cls, products):
        today = datetime.today()
        manufactured_list = [elem["data_de_fabricacao"] for elem in products]
        valid_list = [
            elem["data_de_validade"]
            for elem in products
            if today < datetime.strptime(elem["data_de_validade"], "%Y-%m-%d")
        ]
        company_stock = cls.company_counter(cls, products).most_common(1)[0][
            0
        ]
        return f"""Data de fabricação mais antiga: {min(manufactured_list)}
Data de validade mais próxima: {min(valid_list)}
Empresa com maior quantidade de produtos estocados: {company_stock}
"""
