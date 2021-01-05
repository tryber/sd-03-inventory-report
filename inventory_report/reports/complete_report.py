from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    @classmethod
    def generate(cls, prod):
        minorReport = super().generate(prod)
        companies = super().company_counter(cls, prod)
        company_str = [
            f"- {company}: {quantity}"
            for company, quantity in companies.items()
        ]
        separator = "\n"
        return f"""{minorReport}
Produtos Estocados por empresa: \n{separator.join(company_str)}
"""
