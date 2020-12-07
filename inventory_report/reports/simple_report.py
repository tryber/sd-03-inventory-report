from datetime import datetime
from collections import Counter

dados = [
  {
    "id": 1,
    "nome_do_produto": "CALENDULA OFFICINALIS FLOWERING TOP, GERANIUM MACULATUM ROOT, SODIUM CHLORIDE, THUJA OCCIDENTALIS LEAFY TWIG, ZINC, and ECHINACEA ANGUSTIFOLIA",
    "nome_da_empresa": "Forces of Nature",
    "data_de_fabricacao": "2020-07-08",
    "data_de_validade": "2023-02-09",
    "numero_de_serie": "FR48 2002 7680 97V4 W6FO LEBT 081",
    "instrucoes_de_armazenamento": "in blandit ultrices enim lorem ipsum dolor sit amet consectetuer adipiscing elit proin interdum mauris non ligula pellentesque ultrices    phasellus"
  },
  {
    "id": 2,
    "nome_do_produto": "CALENDULA OFFICINALIS FLOWERING TOP, GERANIUM MACULATUM ROOT, SODIUM CHLORIDE, THUJA OCCIDENTALIS LEAFY TWIG, ZINC, and ECHINACEA ANGUSTIFOLIA",
    "nome_da_empresa": "ACME INC",
    "data_de_fabricacao": "2020-06-04",
    "data_de_validade": "2022-02-02",
    "numero_de_serie": "FR48 2002 7680 97V4 W6FO LEBT 081",
    "instrucoes_de_armazenamento": "in blandit ultrices enim lorem ipsum dolor sit amet consectetuer adipiscing elit proin interdum mauris non ligula pellentesque ultrices    phasellus"
  },
  {
    "id": 3,
    "nome_do_produto": "CALENDULA OFFICINALIS FLOWERING TOP, GERANIUM MACULATUM ROOT, SODIUM CHLORIDE, THUJA OCCIDENTALIS LEAFY TWIG, ZINC, and ECHINACEA ANGUSTIFOLIA",
    "nome_da_empresa": "Forces of Nature",
    "data_de_fabricacao": "2020-06-04",
    "data_de_validade": "2021-02-02",
    "numero_de_serie": "FR48 2002 7680 97V4 W6FO LEBT 081",
    "instrucoes_de_armazenamento": "in blandit ultrices enim lorem ipsum dolor sit amet consectetuer adipiscing elit proin interdum mauris non ligula pellentesque ultrices    phasellus"
  },
]

class SimpleReport:
    def __init__(self, data):
            self.data = data

    def generate(self):
        oldest_mfg_date = min([
            datetime.strptime(product["data_de_fabricacao"], "%Y-%m-%d").date()
            for product in self.data
        ])
        closest_exp_date = min([
            datetime.strptime(product["data_de_validade"], "%Y-%m-%d").date()
            for product in self.data
        ])
        company_name = Counter([
            product["nome_da_empresa"] for product in self.data
        ]).most_common(1)[0]

        return(
            f"""Data de fabricação mais antiga: {oldest_mfg_date}
                Data de validade mais próxima: {closest_exp_date}
                Empresa com maior quantidade de produtos estocados: {company_name[0]}
            """
        )


SimpleReport(dados).generate()