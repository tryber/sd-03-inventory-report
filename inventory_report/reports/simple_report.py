from datetime import datetime
from collections import Counter


class SimpleReport:
    @classmethod
    def generate(self, products_data):
        min_fabrication_date = min([prod["data_de_fabricacao"]
                                    for prod in products_data])
        min_validation_time = min([
            prod["data_de_validade"]
            for prod in products_data
            if datetime.now()
            < datetime.strptime(prod["data_de_validade"], '%Y-%m-%d')
        ])

        max_company = Counter([prod["nome_da_empresa"]
                               for prod in products_data]).most_common(1)[0][0]

        return f"""Data de fabricação mais antiga: {min_fabrication_date}
Data de validade mais próxima: {min_validation_time}
Empresa com maior quantidade de produtos estocados: {max_company}
"""


