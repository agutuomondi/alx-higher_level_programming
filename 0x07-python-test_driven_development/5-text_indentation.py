#!/usr/bin/python3
def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    indentation = 0
    for char in text:
        print(char, end="")
        if char in ".?:":
            print("\n\n", end="")
            indentation = 0
        elif char == '\n':
            indentation = 0
        elif char == ' ':
            indentation += 1
        else:
            indentation = 0
    print()
