from frange import frange  # TASK 1
from colorizer import colorizer  # TASK 2

with colorizer("green"):
    print(colorizer.__doc__)

with colorizer():
    for i in frange(0, 1, 0.1):
        print(i, end='  ')

with colorizer("red"):
    for i in frange(1, 2, 0.2):
        print(i, end='  ')

with colorizer(random_flag=True):
    for i in frange(2.5, 2.6, 0.01):
        print(i, end='  ')
