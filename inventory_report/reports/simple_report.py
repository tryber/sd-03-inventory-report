from datetime import datetime, date
from collections import Counter


class SimpleReport:
    @classmethod
    def generate(self, data):
        company = []
        data.sort(key=lambda el: el["data_de_fabricacao"])
        old_fab = data[0]["data_de_fabricacao"]

        def val_date(el):
            date_format = datetime.strptime(el["data_de_validade"], '%Y-%m-%d')
            if date.today() < date_format.date():
                return True
            return False

        filt = list(filter(val_date, data))
        filt.sort(
            key=lambda el: el["data_de_validade"])
        validate = filt[0]["data_de_validade"]

        for el in data:
            company.append(el["nome_da_empresa"])
        dictionary = dict(Counter(company))

        larger_stock = sorted(
            dictionary.items(), key=lambda el: el[1], reverse=True)[0][0]

        str_old = f"Data de fabricação mais antiga: {old_fab}\n"
        str_val = f"Data de validade mais próxima: {validate}\n"
        str_rel = "Empresa com maior quantidade de produtos estocados:"
        str_stock = f" {larger_stock}\n"

        res = str_old + str_val + str_rel + str_stock
        return res
