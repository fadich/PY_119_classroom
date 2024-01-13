__all__ = [
    "Report",
    "CsvReport",
    "TxtReport",
    "JsonReport",
    "YamlReport",
]


import csv

from typing import (
    Any,
    Dict,
    Sequence,
)


class Report:

    def __init__(
        self,
        data: Sequence[Dict[str, Any]],
        filepath: str,
    ):
        self.data = data
        self.filepath = filepath

    def generate(self):
        raise NotImplementedError()


class CsvReport(Report):

    def generate(self):
        if not self.data:
            raise ValueError("Data is empty")

        headers = self.data[0].keys()

        with open(self.filepath, mode="w") as file:
            writer = csv.DictWriter(
                file,
                fieldnames=headers,
                quoting=csv.QUOTE_ALL
            )

            writer.writeheader()

            for row in self.data:
                writer.writerow(row)


class TxtReport(Report):

    def generate(self):
        with open(self.filepath, "w") as file:
            for item in self.data:
                for key, value in item.items():
                    file.write(f"{key}: {value}\n")
                file.write("\n")


class JsonReport(Report):
    pass


class YamlReport(Report):
    pass


# def generate_csv_report(
#     data: Sequence[Dict[str, Any]],
#     filepath: str,
# ):
#     if not data:
#         raise ValueError("Data is empty")
#
#     headers = data[0].keys()
#
#     with open(filepath, mode="w") as file:
#         writer = csv.DictWriter(
#             file,
#             fieldnames=headers,
#             quoting=csv.QUOTE_ALL
#         )
#
#         writer.writeheader()
#
#         for row in data:
#             writer.writerow(row)
#
#
# def generate_txt_report(
#     data: Sequence[Dict[str, Any]],
#     filepath: str,
# ):
#     with open(filepath, "w") as file:
#         for item in data:
#             for key, value in item.items():
#                 file.write(f"{key}: {value}\n")
#             file.write("\n")
#
#
# def generate_json_report(
#     data: Sequence[Dict[str, Any]],
#     filepath: str,
# ):
#     raise NotImplementedError("JSON format does not supported yet")
#
#
# def generate_yaml_report(
#     data: Sequence[Dict[str, Any]],
#     filepath: str,
# ):
#     raise NotImplementedError("YAML format does not supported yet")
#
#
# generate_yml_report = generate_yaml_report
