from inventory_report.reports.simple_report import SimpleReport, parse_list


class CompleteReport(SimpleReport):
    @staticmethod
    def generate(list):
        oldest = list[0]["data_de_fabricacao"]
        closest = list[0]["data_de_validade"]
        biggest_company = ""
        biggest_company_value = 0
        name_company = {}
        for product in list:
            closest, oldest = parse_list(
                product, closest, oldest, name_company
            )

        for company, quantity in name_company.items():
            if quantity > biggest_company_value:
                biggest_company_value = quantity
                biggest_company = company

        return (
            f"Data de fabricação mais antiga: {oldest}\n"
            + f"Data de validade mais próxima: {closest}\n"
            + "Empresa com maior quantidade de produtos "
            + f"estocados: {biggest_company}\n\n"
            + "Produtos Estocados por empresa: \n"
            + "\n".join(
                [
                    f"- {company}: {quantity}"
                    for company, quantity in name_company.items()
                ]
            )
            + "\n"
        )
