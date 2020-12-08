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
        s4 = f" {major_stock}\n\n"
        s5 = "Produtos Estocados por empresa: \n"
        st = s1 + s2 + s3 + s4 + s5
        for i in range(len(stock_list)):
            st = st + f"- {stock_list[i][0]}: {stock_list[i][1]}\n"
        return st
