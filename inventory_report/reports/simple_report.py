from abc import ABC, abstractmethod
from datetime import datetime
from collections import Counter
from operator import itemgetter

class Report(ABC):
    @abstractmethod
    def generate(cls, reports):
        raise NotImplementedError

class SimpleReport(Report):
    @classmethod
    def generate(cls, reports):
        def oldest_fabrication_date_sort(report):
            fabrication_date = datetime.strptime(report["data_de_fabricacao"], '%Y-%m-%d')
            return fabrication_date

        def closest_validity_date_sort(report):
            validity_datetime = datetime.strptime(report["data_de_validade"], '%Y-%m-%d')
            current_datetime = datetime.now()
            datetime_difference = validity_datetime - current_datetime
            if(datetime_difference.total_seconds() < 0):
                return (1, datetime_difference)
            return (0, datetime_difference)

        oldest_fabrication_date = sorted(reports, key=oldest_fabrication_date_sort)[0]["data_de_fabricacao"]
        closest_validity_date = sorted(reports, key=closest_validity_date_sort)[0]["data_de_validade"]
        company_with_most_products = Counter(report["nome_da_empresa"] for report in reports).most_common(1)[0][0]

        return f"""Data de fabricação mais antiga: {oldest_fabrication_date}
Data de validade mais próxima: {closest_validity_date}
Empresa com maior quantidade de produtos estocados: {company_with_most_products}
"""

print(SimpleReport.generate([
  {
    "id": 1,
    "nome_do_produto": "CALENDULA OFFICINALIS FLOWERING TOP, GERANIUM MACULATUM ROOT, SODIUM CHLORIDE, THUJA OCCIDENTALIS LEAFY TWIG, ZINC, and ECHINACEA ANGUSTIFOLIA",
    "nome_da_empresa": "Forces of Nature",
    "data_de_fabricacao": "2020-07-04",
    "data_de_validade": "2023-02-09",
    "numero_de_serie": "FR48 2002 7680 97V4 W6FO LEBT 081",
    "instrucoes_de_armazenamento": "in blandit ultrices enim lorem ipsum dolor sit amet consectetuer adipiscing elit proin interdum mauris non ligula pellentesque ultrices    phasellus"
  },
    {
    "id": 1,
    "nome_do_produto": "CALENDULA OFFICINALIS FLOWERING TOP, GERANIUM MACULATUM ROOT, SODIUM CHLORIDE, THUJA OCCIDENTALIS LEAFY TWIG, ZINC, and ECHINACEA ANGUSTIFOLIA",
    "nome_da_empresa": "Forces of Nature",
    "data_de_fabricacao": "2020-07-03",
    "data_de_validade": "2023-02-07",
    "numero_de_serie": "FR48 2002 7680 97V4 W6FO LEBT 081",
    "instrucoes_de_armazenamento": "in blandit ultrices enim lorem ipsum dolor sit amet consectetuer adipiscing elit proin interdum mauris non ligula pellentesque ultrices    phasellus"
  },
]))
