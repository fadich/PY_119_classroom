
line = "A quick brown fox jumps over the lazy dog"

# while True:
#     a = file.read(3)
#     if not a:
#         break
#     print(a)


file = open("my_file.txt", "r")
try:
    file = open("my_file.txt", "r")
    print(repr(file.read()))
finally:
    print("Finally")
    file.close()

print("After try")

with open("my_file.txt", "r") as file:
    print(file.read())
    file.seek(0)
    print(file.read())
    file.seek(2)
    print(file.read())
    print(file.read())
    print(file.read())
    ...
    ...

print("after with")
print(file.read())
