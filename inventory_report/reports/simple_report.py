from datetime import datetime


class SimpleReport:
    @classmethod
    def generate(cls, data):
        manufacturing_date = cls.get_manufacturing_date(data)
        due_date = cls.get_due_date(data)
        company = cls.get_company_name(data)
        report = (
            f"Data de fabricação mais antiga: {manufacturing_date}\n"
            f"Data de validade mais próxima: {due_date}\n"
            f"Empresa com maior quantidade de produtos estocados: {company}\n"
        )
        print(report)
        return report

    @classmethod
    def get_manufacturing_date(cls, data):
        manufacturing_date = data[0]["data_de_fabricacao"]
        for product in data:
            if datetime.strptime(
                product["data_de_fabricacao"], "%Y-%m-%d"
            ) < datetime.strptime(manufacturing_date, "%Y-%m-%d"):
                manufacturing_date = product["data_de_fabricacao"]
        return manufacturing_date

    @classmethod
    def get_due_date(cls, data):
        due_date = data[0]["data_de_validade"]
        for product in data:
            if datetime.strptime(
                product["data_de_validade"], "%Y-%m-%d"
            ) > datetime.now() and datetime.strptime(
                product["data_de_validade"], "%Y-%m-%d"
            ) < datetime.strptime(
                due_date, "%Y-%m-%d"
            ):
                due_date = product["data_de_validade"]
        return due_date

    @classmethod
    def get_companies_dict(cls, data):
        qty_products_per_company = {}
        for product in data:
            name = product["nome_da_empresa"]
            if name in qty_products_per_company:
                qty_products_per_company[name] += 1
            if name not in qty_products_per_company:
                qty_products_per_company[name] = 1
        return qty_products_per_company

    @classmethod
    def get_company_name(cls, data):
        company_with_more_products = {"name": "", "qty": 0}
        qty_products_per_company = cls.get_companies_dict(data)
        for company in qty_products_per_company.items():
            if company[1] > company_with_more_products["qty"]:
                company_with_more_products["qty"] = company[1]
                company_with_more_products["name"] = company[0]
        return company_with_more_products["name"]
