
def r_func(n):
    print(f"1) N: {n}")
    if n <= 0:
        return n

    b = r_func(n - 1)
    print(f"2) N: {n}")

    return n + b


print(r_func(5))
