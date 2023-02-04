#!/usr/bin/python3
import random
number = random.randint(-100, 100)
print(f"The number is: {number}")
if number > 0:
    print("is positive")
elif number == 0:
    print(" is zero")
else:
    print(" is negative")


