

# Read a valid number value
while True:
    line = input("Enter somthing: ")
    if line.isdigit():
        number = int(line)
        break
    print("Invalid number")
    # else:
    #     print("Invalid number")

# ...
print(number + 10)
print("out of while loop")

