from inventory_report.reports.simple_report import SimpleReport


class CompleteReport:
    @classmethod
    def get_complete_list(cls):
        list_companies = []
        single_list = []
        list_repeticions = []
        counter = 0
        cls.initial_str = "Produtos Estocados por empresa: \n"
        for value in cls.stock:
            list_companies.append(value["nome_da_empresa"])
        for company in list_companies:
            frequency = list_companies.count(company)
            if company not in single_list:
                single_list.append(company)
                list_repeticions.append(frequency)

        for company in single_list:
            cls.initial_str += f"- {company}: {list_repeticions[counter]}\n"
            counter += 1

    @classmethod
    def generate(cls, stock):
        cls.stock = stock
        cls.get_complete_list()
        simple_response = SimpleReport.generate(stock)
        return (f"{simple_response}\n{cls.initial_str}")
