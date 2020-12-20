from datetime import datetime
from collections import Counter


class CompleteReport:
    @staticmethod
    def generate(dict):
        today = datetime.today()
        # https://stackoverflow.com/questions/5320871/in-list-of-dicts-find-min-value-of-a-common-dict-field
        min_fabricate_date = min(dict, key=lambda x: x['data_de_fabricacao'])
        dates_from_today = []
        for elem in dict:
            date = datetime.strptime(elem["data_de_validade"], "%Y-%m-%d")
            if date > today:
                dates_from_today.append(date.date())
        near_date = min([
            elem
            for elem in dates_from_today
        ])
        company_list = Counter([
            product["nome_da_empresa"] for product in dict
        ])
        company_with_most_products = company_list.most_common(1)[0]

        phrase = ""
        for company in company_list:
            phrase = phrase + f"- {company}: {company_list[company]}\n"
        return (f'Data de fabricação mais antiga:'
                f' {min_fabricate_date["data_de_fabricacao"]}\n'
                f'Data de validade mais próxima: '
                f'{near_date}\n'
                f'Empresa com maior quantidade de produtos estocados: '
                f'{company_with_most_products[0]}\n\n'
                f'Produtos Estocados por empresa: \n'
                f"{phrase}"
                )
