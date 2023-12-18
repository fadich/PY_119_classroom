print("lesson_9.py before import")

from weather.client import get_weather

print("lesson_9.py after import")

# from time import time
# import sys
# from pprint import pprint
#
# pprint(sys.path)
# print(f"TIME: {time()}")


def read_date():
    while True:  # 1
        user_input = input("Enter Date: ")
        if user_input:
            break
        print("Invalid date")

    return user_input


date = read_date()  # 1
weather = get_weather(date)  # 2
print(f"Weather for {date} is {weather}")  # 3
