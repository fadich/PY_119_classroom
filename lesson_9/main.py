from dt import datetime
from random import random

from export_all import *
import export_all


try:
    import bbbbbb
except ImportError:
    print("ImportError")

try:
    from weather.client import get_weather
except SyntaxError:
    print("SyntaxError")


print(datetime.now())

print(a)
print(b)
print(random)
print(my_func)
print(export_all.my_func)
