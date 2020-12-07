from datetime import datetime

teste = [
    {
        "id": "1",
        "nome_do_produto": "Nicotine Polacrilex",
        "nome_da_empresa": "Target Corporation",
        "data_de_fabricacao": "2020-02-18",
        "data_de_validade": "2022-09-17",
        "numero_de_serie": "CR25 1551 4467 2549 4402 1",
        "instrucoes_de_armazenamento": "instrucao 1",
    },
    {
        "id": "2",
        "nome_do_produto": "fentanyl citrate",
        "nome_da_empresa": "Galena Biopharma",
        "data_de_fabricacao": "2019-12-06",
        "data_de_validade": "2022-12-25",
        "numero_de_serie": "FR29 5951 7573 74OY XKGX 6CSG D20",
        "instrucoes_de_armazenamento": "instrucao 2",
    },
    {
        "id": "3",
        "nome_do_produto": "fentanyl citrate",
        "nome_da_empresa": "Galena Biopharma",
        "data_de_fabricacao": "2019-12-06",
        "data_de_validade": "2022-12-25",
        "numero_de_serie": "FR29 5951 7573 74OY XKGX 6CSG D20",
        "instrucoes_de_armazenamento": "instrucao 2",
    },
]


class SimpleReport:
    @classmethod
    def generate(cls, prod):
        today = datetime.today()
        manufactured_list = [elem["data_de_fabricacao"] for elem in prod]
        valid_list = [
            elem["data_de_validade"]
            for elem in prod
            if today < datetime.strptime(elem["data_de_validade"], "%Y-%m-%d")
        ]
        company_list = [elem["nome_da_empresa"] for elem in prod]
        company_stock = [
            {"name": company, "quantity": company_list.count(company)}
            for company in set(company_list)
        ]
        enterprise = {"name": "", "quantity": 0}
        for elem in company_stock:
            if elem["quantity"] > enterprise["quantity"]:
                enterprise = elem
        return f"""Data de fabricação mais antiga: {min(manufactured_list)}
Data de validade mais próxima: {min(valid_list)}
Empresa com maior quantidade de produtos estocados: {enterprise["name"]}
"""


if __name__ == "__main__":
    SimpleReport.generate(teste)
