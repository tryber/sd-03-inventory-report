# -*- coding: utf-8 -*-

from datetime import datetime, date
from collections import Counter


class CompleteReport:
    @classmethod
    def generate(self, data):
        company = []
        sort_data = sorted(data, key=lambda el: el["data_de_fabricacao"])
        oldest = sort_data[0]["data_de_fabricacao"]

        def check_validation_date(val):
            formated = datetime.strptime(val["data_de_validade"], '%Y-%m-%d')
            if formated.date() > date.today():
                return True
            return False

        filt = list(filter(check_validation_date, data))
        filt.sort(key=lambda el: el["data_de_validade"])
        nearest_expire = filt[0]["data_de_validade"]

        for el in data:
            company.append(el["nome_da_empresa"])
        company_dict = list(dict(Counter(company)).items())

        major_stock = sorted(
            company_dict, key=lambda el: el[1], reverse=True)[0][0]

        oldest_fabrication_string = (
            "Data de fabricação mais antiga: {} \n".format(oldest)
        )

        nearest_expire_string = (
            "Data de validade mais próxima: {} \n".format(nearest_expire)
        )
        major_stock_string = (
            "Empresa com maior quantidade"
            + " de produtos estocados:"
            + " {}\n".format(major_stock)
            )

        stock_for_company_string = "Produtos Estocados por empresa: \n"

        res = (
            oldest_fabrication_string
            + nearest_expire_string
            + major_stock_string
            + stock_for_company_string
            )

        for i in range(len(company_dict)):
            res += "- {}: {}\n".format(company_dict[i][0], company_dict[i][1])

        return res
