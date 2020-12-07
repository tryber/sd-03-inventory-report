from datetime import datetime
from collections import Counter


class CompleteReport:
    def __init__(self, data):
        self.data = data

    def generate(self):
        oldest_mfg_date = min([
            datetime.strptime(product["data_de_fabricacao"], "%Y-%m-%d").date()
            for product in self.data
        ])
        closest_exp_date = min([
            datetime.strptime(product["data_de_validade"], "%Y-%m-%d").date()
            for product in self.data
        ])
        all_companys = Counter([
            product["nome_da_empresa"] for product in self.data
        ])
        company_name = all_companys.most_common(1)[0]

        result = ""
        for company in all_companys:
            result = result + f"- {company}: {all_companys[company]}" + "\n"

        return(
            f"""Data de fabricação mais antiga: {oldest_mfg_date}
            Data de validade mais próxima: {closest_exp_date}
            Empresa com maior quantidade de produtos estocados: {
                company_name[0]
            }
            Produtos estocados por empresa:
            {result}"""
        )
