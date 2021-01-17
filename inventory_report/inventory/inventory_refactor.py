# from inventory_report.reports.simple_report import SimpleReport
# from inventory_report.reports.complete_report import CompleteReport
# from inventory_report.importer.csv_importer import CsvImporter
# from inventory_report.importer.json_importer import JsonImporter
# from inventory_report.importer.xml_importer import XmlImporter


# class Inventory:
#     @classmethod
#     def get_type(cls, path):
#         data = []
#         if path.endswith(".csv"):
#             data = CsvImporter.import_data(path)
#         elif path.endswith(".csv"):
#             data = JsonImporter.import_data(path)
#         else:
#             data = XmlImporter.import_data(path)
#         return data

#     @classmethod
#     def import_data(cls, path, choice):
#         data = cls.csv_converter(path)
#         if choice == "simples":
#             return SimpleReport.generate(data)
#         else:
#             return CompleteReport.generate(data)
