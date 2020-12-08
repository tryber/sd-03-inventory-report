# -*- coding: utf-8 -*-

from collections import Counter
from datetime import date, datetime


class SimpleReport:
    @classmethod
    def generate(self, data):
        data.sort(key=lambda e: e["data_de_fabricacao"])
        oldest = data[0]["data_de_fabricacao"]
        nearest_expire = ""
        major_stock = ""
        new_list = []

        def check_validation_date(val):
            flake = datetime.strptime(val["data_de_validade"], "%Y-%m-%d")
            if flake.date() > date.today():
                return True
            return False

        filtered = filter(check_validation_date, data)
        filtered_list = list(filtered)
        filtered_list.sort(key=lambda e: e["data_de_validade"])
        nearest_expire = filtered_list[0]["data_de_validade"]

        for element in data:
            new_list.append(element["nome_da_empresa"])

        dict_data = dict(Counter(new_list))
        major_stock = sorted(
            dict_data.items(), key=lambda x: x[1], reverse=True
        )[0][0]

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

        return (
            oldest_fabrication_string
            + nearest_expire_string
            + major_stock_string
            )
