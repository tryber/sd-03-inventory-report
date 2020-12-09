from xml.dom.minidom import parse
from inventory_report.importer.importer import Importer


class XmlImporter(Importer):
    @classmethod
    def getNodeText(cls, node):
        return node.firstChild.nodeValue

    @classmethod
    def import_data(cls, path):
        if not path.endswith(".xml"):
            raise ValueError("Arquivo inválido")
        list = []
        doc = parse(path)
        records = doc.getElementsByTagName("record")
        for record in records:
            id = cls.getNodeText(record.getElementsByTagName("id")[0])
            nome_do_produto = cls.getNodeText(
                record.getElementsByTagName("nome_do_produto")[0]
            )
            nome_da_empresa = cls.getNodeText(
                record.getElementsByTagName("nome_da_empresa")[0]
            )
            data_de_fabricacao = cls.getNodeText(
                record.getElementsByTagName("data_de_fabricacao")[0]
            )
            data_de_validade = cls.getNodeText(
                record.getElementsByTagName("data_de_validade")[0]
            )
            numero_de_serie = cls.getNodeText(
                record.getElementsByTagName("numero_de_serie")[0]
            )
            instrucoes_de_armazenamento = cls.getNodeText(
                record.getElementsByTagName("instrucoes_de_armazenamento")[0]
            )
            obj = {
                "id": id,
                "nome_do_produto": nome_do_produto,
                "nome_da_empresa": nome_da_empresa,
                "data_de_fabricacao": data_de_fabricacao,
                "data_de_validade": data_de_validade,
                "numero_de_serie": numero_de_serie,
                "instrucoes_de_armazenamento": instrucoes_de_armazenamento,
            }
            list.append(obj)
        return list
