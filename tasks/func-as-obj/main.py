import os.path
import sys

from database import report_data
from report_builder import (
    Report,
    CsvReport,
    TxtReport,
    JsonReport,
    YamlReport,
)

import report_builder


def generate_report(filepath: str):
    """
    Generates a report and saves it to the specified file path,
    with the format determined by the file extension.

    :param filepath: The file path where the report will be saved.
    """

    basename, ext = os.path.splitext(filepath)
    ext = ext.lower().lstrip(".")

    if not ext:
        raise NotImplementedError("ext was not provided!!")

    # Option 1
    # report_generator_classes = {
    #     "csv": CsvReport,
    #     "txt": TxtReport,
    #     "json": JsonReport,
    #     "yml": YamlReport,
    #     "yaml": YamlReport,
    # }
    #
    # if ext not in report_generator_classes:
    #     raise NotImplementedError(f"Unsupported format: {ext}")
    #
    # report_generator = report_generators[ext]
    # report_generator(
    #     filepath=filepath,
    #     data=report_data,
    # )

    # Option 2

    kwargs = {
        "data": report_data,
        "filepath": filepath,
    }
    if ext == "csv":
        report: Report = CsvReport(**kwargs)
    elif ext == "txt":
        report: Report = TxtReport(**kwargs)
    elif ext == "json":
        report: Report = JsonReport(**kwargs)
    elif ext in ("yml", "yaml"):
        report: Report = YamlReport(**kwargs)
    else:
        raise NotImplementedError("Report format does not supported")

    report.generate()
    print(report.filepath)
    print(report.data)
    print(isinstance(report, Report))

    # Option 3
    # if hasattr(report_builder, f"generate_{ext}_report"):
    #     report_generator = getattr(report_builder, f"generate_{ext}_report")
    #     report_generator(
    #         filepath=filepath,
    #         data=report_data,
    #     )


def main(*args):
    try:
        filepath = input("Report filename (path): ")
        generate_report(filepath)
    except KeyboardInterrupt:
        pass
    except Exception as e:
        sys.stderr.write(f"{e}\n")
        sys.stderr.flush()
        return 255
    else:
        print(
            f"The file was successfully saved to\n"
            f"{os.path.abspath(filepath)}"
        )

    return 0


if __name__ == "__main__":
    sys.exit(main(*sys.argv))
