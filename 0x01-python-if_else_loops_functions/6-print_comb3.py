#!/usr/bin/python3
if __name__ == "__main__":
    for i in range(0, 9):
        for j in range(i + 1, 10):
            print("{:d}{:d}".format(i, j), end=", " if i != 8 or j != 9 else "\n")
