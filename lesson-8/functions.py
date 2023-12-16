
age = 999


def hello_gandalf(name: str, number: int = 3):
    """My function"""

    global age

    print(f"Age inside 1: {age}")
    age = 666
    print(f"Age inside 2: {age}")

    print(f"Hello, {name}", end="!" * number + "\n")


print(f"Age before: {age}")
hello_gandalf("abc")
print(f"Age after: {age}")


"""
hello_gandalf("Gandalf")

names = input("Name: ")
hello_gandalf(names, 60)

hello_gandalf("Frodo")
"""

print()
