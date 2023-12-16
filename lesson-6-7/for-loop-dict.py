import random

from lesson_7 import a

i = 0
while i < len(a):
    print(a[i])
    i += 1

print()

for element in a:
    print(element)

print()

for i in range(0, 10):
    print(i)


print("###")

"""
a = []
while len(a) < 10:
    number_a = random.randint(1, 10)
    a.append(number_a)
"""

a = []
for _ in range(10):
    number_a = random.randint(1, 10)
    a.append(number_a)

print(a)

a = [random.randint(1, 10) for _ in range(10)]


####
print("$" * 80)

b = []
for i in range(0, 10):
    if i % 2 == 0:
        b.append(id(i))

print(b)

b = [id(x) if x < 5 else ... for x in range(10) if x % 2 == 0]
print(b)

print("+" * 80)


l = [random.randint(1, 10) for _ in range(10)]
print(l, type(l))

s = {random.randint(1, 10) for _ in range(10)}
print(s, type(s))

g = tuple(random.randint(1, 10) for _ in range(10))
print(g, type(g))

s = set()

print("=" * 80)
d = {
    "names": "Gandalf",
    "age": 999,
    "hair_color": "white",
    "avatar": ...,
}
print(d, type(d))
print(d["names"])

d = dict(
    name="Gandalf",
    age=999,
)

products = {
    "smartphone_1": {
        "camera": 1,
        "color": "red",
    },
    "smartphone_2": {
        "camera": 3,
        "color": "black",
    },
}
print(products)
print(products["smartphone_2"])
print(products["smartphone_2"]["color"])
