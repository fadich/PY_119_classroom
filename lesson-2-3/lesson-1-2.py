"""
This line no longer needed

print(type('\'PY_119 \n  the best!'))
"""

# 1 2 3 abc


print(3, 2, 1, "abc", sep=" ", end="\n")


print('02', 12, 2023, sep='-', end=' year')
print('-------------', end="\n\n\n\n\n")

print("1\t2")
print("1 2")

FIRST_NAME = ""

# i = u / r

first_name = "Gandalf"
last_name = "The Grey"

# 1
full_name = first_name + " " + last_name
print(full_name)

# 2
print(first_name, last_name, sep=" ")

# 3
print(first_name, last_name)

# 4.1
full_name = "{first_name} {last_name}"
print(full_name)

# 4.2
full_name = f"{first_name} {last_name}"
print(full_name)

# 5.1
full_name = "%s %s"
print(full_name)

# 5.2
full_name = "First names: %s; Last nam: %s." % (first_name, last_name)
print(full_name)

# 6.1
full_name = "His names is: {}. And surname: {}".format(first_name, last_name)
print(full_name)

# 6.2
full_name = "{1} {0}".format(last_name, first_name)
print(full_name)

# 6.3
full_name = "{1} {1} {0}".format(last_name, first_name)
print(full_name)

# 6.4
full_name = "{first_name} {last_name}".format(
    last_name=last_name,
    first_name="Gandalf"
)
print(full_name)

# 6.5
fullname_pattern = "{first_name} {last_name}"

...
...
...
...
...

fullname = fullname_pattern.format(
    first_name="Saruman",
    last_name="The White"
)
print(full_name)


pi = 3.14159
print("%.2f" % pi)
print(f"{pi:.2f}")
print("{0}".format(round(pi, 2)))
print("{:.2f}".format(pi))
print("{0:.2f}".format(pi))
print("{pi:.2f}".format(pi=pi))





