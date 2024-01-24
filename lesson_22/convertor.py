from typing import Any


class Convertor:

    def __init__(self, value: Any):
        self.value = value

    @classmethod
    def get_unit_from_name(cls) -> str:
        ...

    @classmethod
    def get_unit_to_name(cls) -> str:
        ...

    def convert(self) -> Any:
        ...


class CelsiusToKelvinConvertor(Convertor):

    @classmethod
    def get_unit_from_name(cls) -> str:
        return "C"

    @classmethod
    def get_unit_to_name(cls) -> str:
        return "K"

    def convert(self) -> Any:
        return float(self.value) + 273.15


if __name__ == "__main__":
    c2k = CelsiusToKelvinConvertor(
        value=input("Value: "),
    )

    print(
        f"{c2k.value}{c2k.get_unit_from_name()} -> "
        f"{c2k.convert()}{c2k.get_unit_to_name()}",
    )
