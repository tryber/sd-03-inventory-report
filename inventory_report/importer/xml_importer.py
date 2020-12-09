from inventory_report.importer.importer import Importer
from os import path
from parsel import Selector


class XmlImporter(Importer):
    @classmethod
    def import_data(self, filepath):
        if path.splitext(filepath)[1] != '.xml':
            raise ValueError('Arquivo inválido')
        new_list = []
        with open(filepath) as file:
            content = Selector(text=file.read())
            data = content.css('record').getall()
            for item in data:
                new = Selector(item)
                new_list.append({
                    'id': new.css('id::text').get(),
                    'nome_do_produto': new.css('nome_do_produto::text').get(),
                    'nome_da_empresa': new.css('nome_da_empresa::text').get(),
                    'data_de_fabricacao': new.css(
                        'data_de_fabricacao::text').get(),
                    'data_de_validade': new.css(
                        'data_de_validade::text').get(),
                    'numero_de_serie': new.css('numero_de_serie::text').get(),
                    'instrucoes_de_armazenamento': new.css(
                        'instrucoes_de_armazenamento::text').get()
                })
        return new_list
