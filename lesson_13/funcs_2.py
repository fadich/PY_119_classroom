from typing import Any


def upper(s: Any):
    return str(s).upper()


names = [
    "Gandalf",
    "Frodo",
    "Bilbo",
    1,
    upper,
    None,
]

# 1.1
names_upper = []
for name in names:
    names_upper.append(upper(name))
print(names_upper)

# 1.2
names_upper = [upper(name) for name in names]
print(names_upper)

# 1.3
names_upper = list(map(upper, names))  # [n for n in map(upper, names)]
print(names_upper)

# 2.1
print("2.1")
names_lower = [str(name).lower() for name in names]
print(names_lower)

# 2.2
print("2.2")
names_lower = list(map(lambda s: str(s).lower(), names))
print(names_lower)


def my_sum(a, b):
    return a + b


print("####### my_sum - def")
print(my_sum(3, 6))
print(my_sum)

print("####### my_sum - lambda")

my_sum_lambda = lambda a, b: a + b
# def my_sum_lambda(a, b):
#     return a + b

print(my_sum_lambda(4, 8))
