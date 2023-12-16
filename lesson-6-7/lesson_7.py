import random

a = []
b = []

while len(a) < 10:
    number_a = random.randint(1, 10)
    a.append(number_a)

while len(b) < 10:
    number_b = random.randint(1, 10)
    b.append(number_b)

c = list(set(a).difference(set(b)))
# print(c)
