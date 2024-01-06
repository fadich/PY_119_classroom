import os.path
import sys

from database import report_data
# from report_builder import (
#     generate_csv_report,
#     generate_txt_report,
#     generate_json_report,
#     generate_yaml_report,
# )

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
    report_generators = {
        "csv": generate_csv_report,
        "txt": generate_txt_report,
        "json": generate_json_report,
        "yml": generate_yaml_report,
        "yaml": generate_yaml_report,
    }

    if ext not in report_generators:
        raise NotImplementedError(f"Unsupported format: {ext}")

    report_generator = report_generators[ext]
    report_generator(
        filepath=filepath,
        data=report_data,
    )

    # Option 2
    # if ext == "csv":
    #     generate_csv_report(**kwargs)
    # elif ext == "txt":
    #     generate_txt_report(**kwargs)
    # elif ext == "json":
    #     generate_json_report(**kwargs)
    # elif ext == "yaml":
    #     generate_yaml_report(**kwargs)
    # elif ext in ("yml", "yaml"):
    #     generate_yaml_report(**kwargs)

    # Option 3
    if hasattr(report_builder, f"generate_{ext}_report"):
        report_generator = getattr(report_builder, f"generate_{ext}_report")
        report_generator(
            filepath=filepath,
            data=report_data,
        )


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
