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


test_list = [
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
print(CompleteReport.generate(test_list))