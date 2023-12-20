__all__ = [
    "get_weather",
]


print("-1 weather.py")
import random

from .example import *


print("0 weather.py")


def get_weather(date):
    number = random.randint(0, 1)
    if number == 0:
        return "Sunny"
    return "Raining"


print("1 weather.py")
