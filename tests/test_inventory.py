from inventory_report.inventory.inventory import Inventory


def test_validar_importerdata_importar_um_arquivo_csv_simples():
    expect = (
                "Data de fabricação mais antiga: 2019-09-06\n"
                "Data de validade mais próxima: 2022-09-17\n"
                "Empresa com maior quantidade de produtos estocados: "
                "Target Corporation\n"
    )
    report = Inventory.import_data('inventory_report/data/inventory.csv',
                                   'simples')
    print(report)
    assert expect in report


def test_validar_importerdata_importar_um_arquivo_csv_completo():
    expect = (
                "Data de fabricação mais antiga: 2019-09-06\n"
                "Data de validade mais próxima: 2022-09-17\n"
                "Empresa com maior quantidade de produtos estocados: "
                "Target Corporation\n\n"

                "Produtos Estocados por empresa: \n"
                "- Target Corporation: 4\n"
                "- Galena Biopharma: 2\n"
                "- Cantrell Drug Company: 2\n"
                "- Moore Medical LLC: 1\n"
                "- REMEDYREPACK: 1\n"
    )
    report = Inventory.import_data('inventory_report/data/inventory.csv',
                                   'completo')
    print(report)
    assert report in expect


def test_validar_importerdata_importar_um_arquivo_json_simples():
    expect = (
                "Data de fabricação mais antiga: 2019-09-06\n"
                "Data de validade mais próxima: 2022-09-17\n"
                "Empresa com maior quantidade de produtos estocados: "
                "Target Corporation\n"
    )
    report = Inventory.import_data('inventory_report/data/inventory.json',
                                   'simples')
    print(report)
    assert report in expect


def test_validar_importerdata_importar_um_arquivo_json_completo():
    expect = (
                "Data de fabricação mais antiga: 2019-09-06\n"
                "Data de validade mais próxima: 2022-09-17\n"
                "Empresa com maior quantidade de produtos estocados: "
                "Target Corporation\n\n"

                "Produtos Estocados por empresa: \n"
                "- Target Corporation: 4\n"
                "- Galena Biopharma: 2\n"
                "- Cantrell Drug Company: 2\n"
                "- Moore Medical LLC: 1\n"
                "- REMEDYREPACK: 1\n"
    )
    report = Inventory.import_data('inventory_report/data/inventory.json',
                                   'completo')
    print(report)
    assert expect in report


def test_validar_importerdata_importar_um_arquivo_xml_simples():
    expect = (
                "Data de fabricação mais antiga: 2019-09-06\n"
                "Data de validade mais próxima: 2022-09-17\n"
                "Empresa com maior quantidade de produtos estocados: "
                "Target Corporation\n"
    )
    report = Inventory.import_data('inventory_report/data/inventory.xml',
                                   'simples')
    print(report)
    assert expect in report


def test_validar_importerdata_importar_um_arquivo_xml_completo():
    expect = (
                "Data de fabricação mais antiga: 2019-09-06\n"
                "Data de validade mais próxima: 2022-09-17\n"
                "Empresa com maior quantidade de produtos estocados: "
                "Target Corporation\n\n"

                "Produtos Estocados por empresa: \n"
                "- Target Corporation: 4\n"
                "- Galena Biopharma: 2\n"
                "- Cantrell Drug Company: 2\n"
                "- Moore Medical LLC: 1\n"
                "- REMEDYREPACK: 1\n"
    )
    report = Inventory.import_data('inventory_report/data/inventory.xml',
                                   'completo')
    print(report)
    assert expect in report
