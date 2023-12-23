import json
from typing import Any

types = {
    # Python : JavaScript
    "None": "null",
    "bool": "true/false",
    "int": "number",
    "float": "number",
    "str": "string",
    "list": "Array",
    # "set": "Array",
    "tuple": "Array",
    "dict": "Object",
}


def repr_json(value: Any):
    return repr(json.dumps(value))


print(repr_json(None))
print(repr_json(True))
print(repr_json(False))
print(repr_json(13))
print(repr_json(100.5))
print(repr_json("my line"))
print(repr_json('my line'))
print(repr_json("""my line"""))
print(repr_json([1, 2, 3]))
print(repr_json((4, 5, 6)))
print(repr_json(tuple({7, 8, 9, })))
print(repr_json({1: 2, "b": [1, 2, 3]}))

json_value = {
    1: 2,
    "b": [
        1,
        2,
        3,
    ],
}

print(json_value)

# Create JSON
with open("my_json.json", "w") as file:
    file.write(json.dumps(json_value))


# Read JSON
with open("my_json.json", "r") as file:
    file_content = file.read()

print(repr(file_content))
python_value = json.loads(file_content)

print(type(python_value))
print(python_value)

a = json.loads("1.0")
with open("my_json.json", "r") as file:
    a = json.load(file)
    # a = json.loads(file.read())

print(repr(a))
print(type(a))


a = []
a = [1, 2, 3, 4]
a = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

a[0][2]

a = [
    "123",
    "456",
    "789",
]
a[0][2]

a = [
    [
        [1, 2, 3],
    ]
]
a[0][0][2]


a = {
    "a": 1,
    "2": 3,
}

print(a.items())

a = [
    [
        [
            [
                [1, 2, 3]
            ]
        ]
    ]
]


users = [
    {
        "username": "gandalf",
        "score": 123,
    },
    {
        "username": "Frodo",
        "score": 1123,
    },
]
