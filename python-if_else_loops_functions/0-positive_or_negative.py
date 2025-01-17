#!/usr/bin/python3
import random

while True:
    number = random.randint(-10, 10)
        print(f"{number} is positive")
    elif number == 0:
        print(f"{number} is zero")
    else:
        print(f"{number} is negative")
    
    if number == 0:
        break

