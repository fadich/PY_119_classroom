import json
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
    TEMP_KEL = "K"

    @classmethod
    def get_unit_from_name(cls) -> str:
        return "C"

    @classmethod
    def get_unit_to_name(cls) -> str:
        return cls.TEMP_KEL

    def convert(self) -> Any:
        return float(self.value) + 273.15


class KelvinToCelsiusConvertor(Convertor):
    TEMP_KEL = "K"

    @classmethod
    def get_unit_from_name(cls) -> str:
        return cls.TEMP_KEL

    @classmethod
    def get_unit_to_name(cls) -> str:
        return "C"

    def convert(self) -> Any:
        return float(self.value) - 273.15


class JsonObjToValuesConvertor(Convertor):

    @classmethod
    def get_unit_from_name(cls) -> str:
        return "json object"

    @classmethod
    def get_unit_to_name(cls) -> str:
        return "values"

    def convert(self) -> Any:
        return json.loads(self.value).values()


class UAHToUSDConvertor(Convertor):

    @classmethod
    def get_unit_from_name(cls) -> str:
        return "UAH"

    @classmethod
    def get_unit_to_name(cls) -> str:
        return "USD"

    def convert(self) -> Any:
        return float(self.value) / 39.5


def create_convertor(name: str) -> Convertor:
    if name == "c2k":
        return CelsiusToKelvinConvertor(value=value)
    if name == "k2c":
        return KelvinToCelsiusConvertor(value=value)
    if name == "j2v":
        return JsonObjToValuesConvertor(value=value)
    if name == "u2s":
        return UAHToUSDConvertor(value=value)

    raise NotImplementedError(f"There is not such convertor <{name}>")


if __name__ == "__main__":
    name = input("Convertor name: ")
    value = input("Value: ")

    convertor: Convertor = create_convertor(name)

    print(
        f"{convertor.value}{convertor.get_unit_from_name()} -> "
        f"{convertor.convert()}{convertor.get_unit_to_name()}",
    )
