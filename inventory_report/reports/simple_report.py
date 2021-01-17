from datetime import datetime, date


class SimpleReport:
    @classmethod
    def get_data_de_fabricacao(cls):
        cls.older = ''
        for value in cls.stock:
            if cls.older == '':
                cls.older = value["data_de_fabricacao"]
            elif (
                datetime.strptime(cls.older, "%Y-%m-%d")
                > datetime.strptime(value["data_de_fabricacao"], "%Y-%m-%d")
            ):
                cls.older = value["data_de_fabricacao"]

    @classmethod
    def get_data_de_validade(cls):
        cls.closer = ''
        for value in cls.stock:
            if (
                datetime
                .strptime(date.today().strftime("%Y-%m-%d"), "%Y-%m-%d")
                < datetime.strptime(value["data_de_validade"], "%Y-%m-%d")
            ):
                if cls.closer == '':
                    cls.closer = value["data_de_validade"]
                elif (
                    datetime.strptime(cls.closer, "%Y-%m-%d")
                    > datetime.strptime(value["data_de_validade"], "%Y-%m-%d")
                ):
                    cls.closer = value["data_de_validade"]

    @classmethod
    def get_nome_da_empresa(cls):
        cls.cn = ''
        empresas = []
        counter = 0
        for value in cls.stock:
            empresas.append(value["nome_da_empresa"])
        for empresa in empresas:
            repeticoes = empresas.count(empresa)
            if repeticoes > counter:
                counter = repeticoes
                cls.cn = empresa

    @classmethod
    def generate(cls, stock):
        cls.stock = stock
        cls.get_data_de_fabricacao()
        cls.get_data_de_validade()
        cls.get_nome_da_empresa()
        return (
            f"Data de fabricação mais antiga: {cls.older}\n"
            f"Data de validade mais próxima: {cls.closer}\n"
            f"Empresa com maior quantidade de produtos estocados: {cls.cn}\n"
        )
