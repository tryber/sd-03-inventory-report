from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    @classmethod
    def generate(self, data):
        report = SimpleReport.generate(data)
        products_by_company = SimpleReport.group_list_by_key(
            data, "nome_da_empresa"
        )
        report += "\nProdutos Estocados por empresa: \n"
        for company, quantity in products_by_company.items():
            report += f"- {company}: {quantity}\n"
        return report
