
def is_float(line: str) -> bool:
    try:
        print("try")
        float(line)  # ERROR
    except:
        print("ERROR!")
        return False
    else:
        print("else")
    finally:
        print("finally")

    print("No error")
    return True


print("+123.10.5")
print(is_float("+123.10.5"))
print("=======")
print("123")
print(is_float("123"))

# file = open()
# try:
#     file.write("abc")
# finally:
#     file.close()


"""
print("=======")
try:
    1 / 0
finally:
    print("Finally")

"""

print("=======")
try:
    a = 1 / 0
except ZeroDivisionError as exception:
    print("ZeroDivisionError")
except ArithmeticError as e:
    print("ArithmeticError", e)
except Exception:
    print("Exception")

print("=====")


def make_error():
    raise FileNotFoundError("Hello from make_error()")


try:
    make_error()
except FileNotFoundError:
    print()

print("Last line")
