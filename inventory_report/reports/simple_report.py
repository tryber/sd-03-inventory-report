from datetime import datetime, date


class SimpleReport:
    @classmethod
    def get_manufactering_date(cls):
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
    def get_expire_date(cls):
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
    def get_more_products(cls):
        cls.cn = ''
        list_companies = []
        counter = 0
        for value in cls.stock:
            list_companies.append(value["nome_da_empresa"])
        for company in list_companies:
            frequency = list_companies.count(company)
            if frequency > counter:
                counter = frequency
                cls.cn = company

    @classmethod
    def generate(cls, stock):
        cls.stock = stock
        cls.get_manufactering_date()
        cls.get_expire_date()
        cls.get_more_products()
        return (
            f"Data de fabricação mais antiga: {cls.older}\n"
            f"Data de validade mais próxima: {cls.closer}\n"
            f"Empresa com maior quantidade de produtos estocados: {cls.cn}\n"
        )
