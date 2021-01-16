
from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):

    @classmethod
    def generate(cls, data):
        simple_report = super().generate(data)
        qtd_produtos = cls.get_produtos_por_empresa(data)
        empresas = "\nProdutos Estocados por empresa: \n"
        for empresa in qtd_produtos.items():
            empresas += f"- {empresa[0]}: {empresa[1]}\n"
        complete_report = simple_report + empresas
        return complete_report
