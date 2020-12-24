from datetime import datetime
from collections import Counter


class SimpleReport:
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
        more_times_appear = Counter([
            elem["nome_da_empresa"] for elem in dict
                                      ]).most_common(1)[0]
        return (f'Data de fabricação mais antiga:'
                f' {min_fabricate_date["data_de_fabricacao"]}\n'
                f'Data de validade mais próxima: '
                f'{near_date}\n'
                f'Empresa com maior quantidade de produtos estocados: '
                f'{more_times_appear[0]}\n'
                )
