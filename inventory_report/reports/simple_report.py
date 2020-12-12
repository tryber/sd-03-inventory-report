from datetime import datetime
import collections


class SimpleReport:
    @classmethod
    def group_list_by_key(cls, listToGroup, key):
        data = [elem[key] for elem in listToGroup]
        grouped = collections.Counter(data)
        return grouped

    @staticmethod
    def older_validate_date(products):
        date_time_now = datetime.now().strftime("%Y-%m-%d")
        older_validate = "9999-99-99"
        for product in products:
            if older_validate > product["data_de_validade"] > date_time_now:
                older_validate = product["data_de_validade"]
        return older_validate

    @staticmethod
    def older_fabricate_date(products):
        older_fabricate = datetime.now().strftime("%Y-%m-%d")
        for product in products:
            if product["data_de_fabricacao"] < older_fabricate:
                older_fabricate = product["data_de_fabricacao"]
        return older_fabricate

    @staticmethod
    def grather_company_stock(data):
        grather_stock = {"name": "", "quantity": 0}
        for company in data:
            if grather_stock["quantity"] < len(company):
                grather_stock["quantity"] = len(company)
                grather_stock["name"] = company[0]["nome_da_empresa"]
        return grather_stock

    @classmethod
    def generate(cls, products):
        productsGroupedByName = cls.group_list_by_key(
            products, "nome_da_empresa"
        )

        stock = "Empresa com maior quantidade de produtos estocados:"
        date = "Data de fabricação mais antiga:"
        validate = "Data de validade mais próxima:"
        older_fabricate = cls.older_fabricate_date(products)
        older_validate = cls.older_validate_date(products)

        return f"""{date} {older_fabricate}
{validate} {older_validate}
{stock} {productsGroupedByName.most_common(1)[0][0]}
"""
