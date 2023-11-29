#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number >= 0:
    lastdigit = number % 10
else:
    lastdigit = ((number * -1) % 10) * -1

message = "Last digit of %d is %d and is" % (number, lastdigit)

if lastdigit == 0:
    print(f"{thestring} and is 0")
elif lastdigit > 5:
    print(message, "greater than 5")
else:
    print(message, "less than 6 and not 0")

