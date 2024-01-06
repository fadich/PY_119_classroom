import random


@retry
def broken_division_calculator(a, b):
    if random.random() < 0.85:
        b = 0

    return a / b


result = broken_division_calculator(1, 2)
print(result)
