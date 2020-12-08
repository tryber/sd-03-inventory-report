from json import load
from datetime import datetime
import collections

test = [
        {
            "id": 1,
            "nome_do_produto": "CALENDULA OFFICINALIS FLOWERING TOP",
            "nome_da_empresa": "Forces of Nature",
            "data_de_fabricacao": "2020-07-04",
            "data_de_validade": "2023-02-09",
            "numero_de_serie": "FR48 2002 7680 97V4 W6FO LEBT 081",
            "instrucoes_de_armazenamento": "in blandit ultrices enim",
        },
        {
            "id": 2,
            "nome_do_produto": "sodium ferric gluconate complex",
            "nome_da_empresa": "sanofi-aventis U.S. LLC",
            "data_de_fabricacao": "2020-05-31",
            "data_de_validade": "2023-01-17",
            "numero_de_serie": "SE95 2662 8860 5529 8299 2861",
            "instrucoes_de_armazenamento": "duis bibendum morbi",
        },
        {
            "id": 3,
            "nome_do_produto": "Dexamethasone Sodium Phosphate",
            "nome_da_empresa": "sanofi-aventis U.S. LLC",
            "data_de_fabricacao": "2019-09-13",
            "data_de_validade": "2023-02-13",
            "numero_de_serie": "BA52 2034 8595 7904 7131",
            "instrucoes_de_armazenamento": "morbi quis tortor id",
        },
        {
            "id": 4,
            "nome_do_produto": "Uricum acidum, Benzoicum acidum",
            "nome_da_empresa": "Newton Laboratories, Inc.",
            "data_de_fabricacao": "2019-11-08",
            "data_de_validade": "2019-11-25",
            "numero_de_serie": "FR38 9203 3060 400T QQ8B HHS0 Q46",
            "instrucoes_de_armazenamento": "velit eu est congue elementum",
        },
    ]

class SimpleReport:
    @staticmethod
    def format_date(date):
        if isinstance(date, datetime):
            return date
        return datetime.strptime(date, "%Y-%m-%d")

    def give_earliest_due_date(self, doc, holder):
        due_date = self.format_date(doc["data_de_validade"])
        earlisest = self.format_date(holder["earliest_due_date"])
        print(f'{due_date=}')
        print(f'{earlisest=}')
        if (
            earlisest > due_date
            and due_date >= datetime.now()
        ):
            holder["earliest_due_date"] = due_date

    def give_earliest_production_date(self, doc, holder):
        production_date = self.format_date(doc["data_de_fabricacao"])
        earliest = self.format_date(holder["earliest_production_date"])
        if (
            earliest > production_date
        ):
            holder["earliest_production_date"] = production_date

    def count_company_products(self, doc, companies_stock):
        if companies_stock.get(doc["nome_da_empresa"]) is not None:
            companies_stock[doc["nome_da_empresa"]] += 1
        else:
            companies_stock[doc["nome_da_empresa"]] = 1

    def interate_over_data(self, data):
        companies_stock = {}
        holder = {
            "earliest_due_date": self.format_date(data[0]["data_de_validade"]),
            "earliest_production_date": self.format_date(
                data[0]["data_de_fabricacao"]
            ),
        }

        for doc in data:
            self.give_earliest_due_date(self, doc, holder)
            self.give_earliest_production_date(self, doc, holder)
            self.count_company_products(self, doc, companies_stock)

        greater_stock_name = collections.Counter(
            companies_stock
        ).most_common()[0][0]
        format_production = holder["earliest_production_date"].strftime(
            "%Y-%m-%d"
        )
        format_due = holder["earliest_due_date"].strftime("%Y-%m-%d")
        log = f"""Data de fabricação mais antiga: {format_production}
Data de validade mais próxima: {format_due}
Empresa com maior quantidade de produtos estocados: {greater_stock_name}
"""
        print(log)
        return log

    @classmethod
    def generate(self, data):
        return self.interate_over_data(self, data=data)


SimpleReport.generate(test)
