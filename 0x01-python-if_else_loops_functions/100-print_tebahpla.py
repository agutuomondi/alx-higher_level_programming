#!/usr/bin/python3
for i in range(ord('z'), ord('a') - 1, -2):
    if i % 2 != 0:
        i = i - 32
    print("{}".format(chr(i)), end="")

