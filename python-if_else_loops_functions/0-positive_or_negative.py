#!/usr/bin/python3
import random
number = random.randint(-10, 10)
<<<<<<< HEAD
=======
print(f"The number is: {number}")
>>>>>>> ba6b86b2a5768da855d47fdebc085ccd3286dedb
if number > 0:
    print("{} is positive".format(number))
elif number == 0:
    print("{} is zero".format(number))
else:
    print("{} is negative".format(number))
