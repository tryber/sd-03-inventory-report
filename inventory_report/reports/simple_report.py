from datetime import date


def parse_list(product, closest, oldest, name_company):
    fabrication = date.fromisoformat(product["data_de_fabricacao"])
    validate = date.fromisoformat(product["data_de_validade"])
    if fabrication < date.fromisoformat(oldest):
        oldest = product["data_de_fabricacao"]
    if date.today() < validate < date.fromisoformat(closest):
        closest = product["data_de_validade"]
    company = product["nome_da_empresa"]
    name_company[company] = name_company.get(company, 0) + 1
    return closest, oldest


class SimpleReport:
    @staticmethod
    def generate(list):
        oldest = list[0]["data_de_fabricacao"]
        closest = list[0]["data_de_validade"]
        biggest_company = ""
        biggest_company_value = 0
        name_company = {}
        for product in list:
            closest, oldest = parse_list(
                product, closest, oldest, name_company
            )

        for company, quantity in name_company.items():
            if quantity > biggest_company_value:
                biggest_company_value = quantity
                biggest_company = company

        relatory = (
            f"Data de fabricação mais antiga: {oldest}\n"
            + f"Data de validade mais próxima: {closest}\n"
            + "Empresa com maior quantidade de produtos "
            + f"estocados: {biggest_company}\n"
        )
        return relatory
