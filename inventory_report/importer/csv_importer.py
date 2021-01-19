from inventory_report.importer.importer import Importer
import re
import csv


class CsvImporter(Importer):
    @classmethod
    def import_data(cls, filepath):
        if not re.search('.csv', filepath):
            raise ValueError('Arquivo inválido')
        try:
            with open(filepath, 'r', encoding='utf-8') as csv_file:
                data = csv.reader(csv_file, delimiter=",", quotechar='"')
                headers, *product_data = data
        except FileNotFoundError:
            raise FileNotFoundError('Arquivo não encontrado')
        else:
            product_list = []
            for products in product_data:
                product_list.append(
                    {header: products[index]
                        for index, header in enumerate(headers)}
                )
            return product_list
