from inventory_report.reports.simple_report import SimpleReport
from collections import Counter
from operator import itemgetter


class CompleteReport(SimpleReport):
    @classmethod
    def generate(cls, reports):
        simple_report = super().generate(reports)
        stocked_products = list(Counter(report["nome_da_empresa"] for report in reports).items())
        complete_report = f"""{simple_report}
Produtos Estocados por empresa: \n"""
        for product in stocked_products:
            company, quantity = product
            template = f"- {company}: {quantity}\n"
            complete_report += template
        return complete_report
