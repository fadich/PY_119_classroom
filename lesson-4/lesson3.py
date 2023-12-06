a = 5
b = 5

if a == b:
    print("equal")
    # c = a / 0
else:
    print("NO")

print("After condition")


print("=" * 20)

x1 = True
x2 = False


print(x1 and x2)

print(x1 or x2)

print(not x1)


is_monday = True
is_sunday = False
print(
    True
    or
    1 / 0
    or
    1 / 0
    or
    1 / 0
)
# ...

x1 and x2  # x1 * x2
x1 or x2  # x1 + x2

print("=" * 20)

a = 1
b = 1
c = 1
d = 0

print(bool(a and b or c or d))


# False
i = 0
f = 0.0
s = ""
n = None

user_input = None  # bool(False)
user_input = ""  # bool(False)
user_input = "My name is ..."
if user_input is not None:
    print("True")
else:
    print("False")

if ...:
    ...
elif ...:
    ...
else:
    ...

print("0" == False)
print(bool(0) is False)

print(1 is 2)

a = 3
b = 0
while a > b:
    print("Hello!")
    a -= 1
    break
else:
    print("ELSE!")
