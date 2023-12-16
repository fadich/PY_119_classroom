# print("".join(line))

c = [3, 5, 6]
b = [2, c, 5]
a = [1, "2", 3, 5.2, b]
# print(a[1:5:2])

print(a.index(5.2))
a.insert(3, "Frodo")
print(a)

print(a[5][1][0])

print("===" * 20)

a[3] = "Gimli"
print(a)

b[2] = "Aragorn"
print(a)
print(b)

b[1] = "Saruman"
print(a)
print(b)
print(c)

# del b
del a[5]
del b
c = [2, 2, 2]
print(a)
# print(b)
print(c)

a = [1, 2, 3]
b = [4, 5, 6]

print("EXT")
print(a, b)

c = [*a, *b]
# del a[1]  <==>  a.remove(1)

print(a, b, c[::-1])
print(c, c[:])

d = [5, 2, 3, 6, 1]
print(d)
# d.sort()
# print(d)

print(sorted("da"))
print(d)

print("===" * 20)

a = (3, 1, 2)
b = tuple(sorted(a))

print(a, b)

a = (1, 2, 3)
b = (4, 5, 6)
c = (*a, *b)

a += b
print(a)

a = 1
a = 1.0
a = "1"
a = [1]
a = (1, )

a = []  # a = list()
a = ()  # a = tuple()
a = ""  # str()


a = ()


print("SET " * 20)

a = set()
print(a)

a = {1, 2, 3}
print(a)

a.add(4)
print(a)

a.add(2)
print(a)

print(list(set([1, 1, 2, 3, 3, 4])))


gandalf = {"Pink Floyd", "Led Zeppelin", "Metallica", "Black Sabbath", "AC/DC"}
frodo = {"Asking Alexandria", "Metallica", "Disturbed", "AC/DC"}

print("intersection", gandalf.intersection(frodo))
print("intersection", gandalf & frodo)

print("difference", gandalf.difference(frodo))
print("difference", frodo.difference(gandalf))
print("difference", gandalf - frodo)
print("difference", frodo - gandalf)

print("union", gandalf.union(frodo))
print("union", gandalf | frodo)

print({1, 2, 9}.issubset({1, 3, 4, 2}))



