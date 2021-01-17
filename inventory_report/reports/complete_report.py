from inventory_report.reports.simple_report import SimpleReport


class CompleteReport:
    @classmethod
    def get_more_products(cls):
        complete_list = []
        single_list = []
        repeat_list = []
        counter = 0
        cls.initial_str = "Produtos Estocados por empresa: \n"
        for value in cls.stock:
            complete_list.append(value["nome_da_empresa"])
        for company in complete_list:
            frenquency = complete_list.count(company)
            if company not in single_list:
                single_list.append(company)
                repeat_list.append(frenquency)
        for company in single_list:
            cls.initial_str += f"- {company}: {repeat_list[counter]}\n"
            counter += 1

    @classmethod
    def generate(cls, stock):
        cls.stock = stock
        cls.get_more_products()
        single_response = SimpleReport.generate(stock)
        return (f"{single_response}\n{cls.initial_str}")
