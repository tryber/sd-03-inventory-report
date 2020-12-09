from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):

    @classmethod
    def generate(cls, data):
        simple_report = super().generate(data)
        companies = cls.get_companies_dict(data)
        companies_list = "\nProdutos Estocados por empresa: \n"
        for company in companies.items():
            companies_list += f"- {company[0]}: {company[1]}\n"
        complete_report = simple_report + companies_list
        return complete_report
