__all__ = [
    "generate_csv_report",
    "generate_txt_report",
    "generate_json_report",
    "generate_yaml_report",
]


import csv

from typing import (
    Any,
    Dict,
    Sequence,
)


def generate_csv_report(
    data: Sequence[Dict[str, Any]],
    filepath: str,
):
    if not data:
        raise ValueError("Data is empty")

    headers = data[0].keys()

    with open(filepath, mode="w") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=headers,
            quoting=csv.QUOTE_ALL
        )

        writer.writeheader()

        for row in data:
            writer.writerow(row)


def generate_txt_report(
    data: Sequence[Dict[str, Any]],
    filepath: str,
):
    with open(filepath, "w") as file:
        for item in data:
            for key, value in item.items():
                file.write(f"{key}: {value}\n")
            file.write("\n")


def generate_json_report(
    data: Sequence[Dict[str, Any]],
    filepath: str,
):
    raise NotImplementedError("JSON format does not supported yet")


def generate_yaml_report(
    data: Sequence[Dict[str, Any]],
    filepath: str,
):
    raise NotImplementedError("YAML format does not supported yet")


generate_yml_report = generate_yaml_report
