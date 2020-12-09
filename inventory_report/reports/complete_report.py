from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    @classmethod
    def generate(cls, data):
        simple_report = super().generate(data)
        companies = super().interate_over_data(data=data)["companies_stock"]
        amend_log = "Produtos Estocados por empresa: \n"
        for name, qnt in companies.items():
            amend_log += f"- {name}: {qnt}\n"
        complete_report = simple_report + "\n" + amend_log
        return complete_report
