from collections import Counter
from datetime import date, datetime


class CompleteReport:
    @classmethod
    def generate(self, data):
        major_stock = ""
        nearest_expire = ""
        new_data = sorted(data, key=lambda e: e["data_de_fabricacao"])
        oldest = new_data[0]["data_de_fabricacao"]

        def fun(e):
            flake = datetime.strptime(e["data_de_validade"], '%Y-%m-%d')
            if flake.date() > date.today():
                return True
            return False
        filtered = list(filter(fun, data))
        filtered.sort(
            key=lambda e: e["data_de_validade"])
        nearest_expire = filtered[0]["data_de_validade"]
        new_list = []
        for e in data:
            new_list.append(e["nome_da_empresa"])
        stock_list = list(dict(Counter(new_list)).items())
        major_stock = sorted(
            stock_list, key=lambda x: x[1], reverse=True)[0][0]
        s1 = f"Data de fabricação mais antiga: {oldest}\n"
        s2 = f"Data de validade mais próxima: {nearest_expire}\n"
        s3 = "Empresa com maior quantidade de produtos estocados:"
        s4 = f" {major_stock}\n"
        s5 = "Produtos Estocados por empresa: \n"
        st = s1 + s2 + s3 + s4 + s5
        for i in range(len(stock_list)):
            st = st + f"- {stock_list[i][0]}: {stock_list[i][1]}\n"
        return st
# test_list = [
#         {
#             "id": 1,
#             "nome_do_produto": "CALENDULA OFFICINALIS FLOWERING TOP",
#             "nome_da_empresa": "Forces of Nature",
#             "data_de_fabricacao": "2020-07-04",
#             "data_de_validade": "2023-02-09",
#             "numero_de_serie": "FR48 2002 7680 97V4 W6FO LEBT 081",
#             "instrucoes_de_armazenamento": "in blandit ultrices enim",
#         },
#         {
#             "id": 2,
#             "nome_do_produto": "sodium ferric gluconate complex",
#             "nome_da_empresa": "sanofi-aventis U.S. LLC",
#             "data_de_fabricacao": "2020-05-31",
#             "data_de_validade": "2023-01-17",
#             "numero_de_serie": "SE95 2662 8860 5529 8299 2861",
#             "instrucoes_de_armazenamento": "duis bibendum morbi",
#         },
#         {
#             "id": 3,
#             "nome_do_produto": "Dexamethasone Sodium Phosphate",
#             "nome_da_empresa": "sanofi-aventis U.S. LLC",
#             "data_de_fabricacao": "2019-09-13",
#             "data_de_validade": "2023-02-13",
#             "numero_de_serie": "BA52 2034 8595 7904 7131",
#             "instrucoes_de_armazenamento": "morbi quis tortor id",
#         },
#         {
#             "id": 4,
#             "nome_do_produto": "Uricum acidum, Benzoicum acidum",
#             "nome_da_empresa": "Newton Laboratories, Inc.",
#             "data_de_fabricacao": "2019-11-08",
#             "data_de_validade": "2019-11-25",
#             "numero_de_serie": "FR38 9203 3060 400T QQ8B HHS0 Q46",
#             "instrucoes_de_armazenamento": "velit eu est congue elementum",
#         },
#     ]

# print(CompleteReport.generate(test_list))
