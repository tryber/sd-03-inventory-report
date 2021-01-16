from datetime import datetime


class SimpleReport:

    @classmethod
    def generate(cls, data):
        fabricacao = cls.get_fabricacao(data)
        vencimento = cls.get_vencimento(data)
        empresa = cls.get_empresa(data)
        report = (
            f"Data de fabricação mais antiga: {fabricacao}\n"
            f"Data de validade mais próxima: {vencimento}\n"
            f"Empresa com maior quantidade de produtos estocados: {empresa}\n"
        )
        return report

    @classmethod
    def get_fabricacao(cls, data):
        fabricacao = data[0]["data_de_fabricacao"]

        for produto in data:
            if datetime.strptime(
                produto["data_de_fabricacao"], "%Y-%m-%d"
            ) < datetime.strptime(fabricacao, "%Y-%m-%d"):
                fabricacao = produto["data_de_fabricacao"]

        return fabricacao

    @classmethod
    def get_vencimento(cls, data):
        vencimento = data[0]["data_de_validade"]

        for produto in data:
            if datetime.strptime(
                produto["data_de_validade"], "%Y-%m-%d"
            ) > datetime.now() and datetime.strptime(
                produto["data_de_validade"], "%Y-%m-%d"
            ) < datetime.strptime(
                vencimento, "%Y-%m-%d"
            ):
                vencimento = produto["data_de_validade"]

        return vencimento

    @classmethod
    def get_produtos_por_empresa(cls, data):
        qtd_produtos_por_empresa = {}

        for produto in data:
            name = produto["nome_da_empresa"]
            if name in qtd_produtos_por_empresa:
                qtd_produtos_por_empresa[name] += 1
            if name not in qtd_produtos_por_empresa:
                qtd_produtos_por_empresa[name] = 1

        return qtd_produtos_por_empresa

    @classmethod
    def get_empresa(cls, data):
        empresa_com_mais_produtos = {"name": "", "qtd": 0}
        qtd_produtos_por_empresa = cls.get_produtos_por_empresa(data)

        for empresa in qtd_produtos_por_empresa.items():
            if empresa[1] > empresa_com_mais_produtos["qtd"]:
                empresa_com_mais_produtos["qtd"] = empresa[1]
                empresa_com_mais_produtos["name"] = empresa[0]

        return empresa_com_mais_produtos["name"]
