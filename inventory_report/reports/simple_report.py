from datetime import datetime
import collections


class SimpleReport:
    @staticmethod
    def format_date(date):
        if isinstance(date, datetime):
            return date
        return datetime.strptime(date, "%Y-%m-%d")

    @classmethod
    def give_earliest_due_date(cls, doc, holder):
        due_date = cls.format_date(doc["data_de_validade"])
        earlisest = cls.format_date(holder["earliest_due_date"])
        if earlisest > due_date and due_date >= datetime.now():
            holder["earliest_due_date"] = due_date

    @classmethod
    def give_earliest_production_date(cls, doc, holder):
        production_date = cls.format_date(doc["data_de_fabricacao"])
        earliest = cls.format_date(holder["earliest_production_date"])
        if earliest > production_date:
            holder["earliest_production_date"] = production_date

    @classmethod
    def count_company_products(cls, holder, companies_stock):
        if companies_stock.get(holder["nome_da_empresa"]) is not None:
            companies_stock[holder["nome_da_empresa"]] += 1
        else:
            companies_stock[holder["nome_da_empresa"]] = 1

    @classmethod
    def interate_over_data(cls, data):
        companies_stock = {}
        holder = {
            "earliest_due_date": cls.format_date(data[0]["data_de_validade"]),
            "earliest_production_date": cls.format_date(
                data[0]["data_de_fabricacao"]
            ),
        }

        for doc in data:
            cls.give_earliest_due_date(doc=doc, holder=holder)
            cls.give_earliest_production_date(doc, holder)
            cls.count_company_products(doc, companies_stock)

        greater_stock_name = collections.Counter(
            companies_stock
        ).most_common()[0][0]
        format_production = holder["earliest_production_date"].strftime(
            "%Y-%m-%d"
        )
        format_due = holder["earliest_due_date"].strftime("%Y-%m-%d")
        return {
            "production": format_production,
            "due": format_due,
            "companies": format_due,
            "bigger_stock": greater_stock_name,
            "companies_stock": companies_stock,
        }

    @classmethod
    def generate(cls, data):
        logs = cls.interate_over_data(data=data)
        return f"""Data de fabricação mais antiga: {logs['production']}
Data de validade mais próxima: {logs['due']}
Empresa com maior quantidade de produtos estocados: {logs['bigger_stock']}
"""
