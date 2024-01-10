#!/usr/bin/python3
def read_file(filename=""):
    try:
        with open(filename, encoding="utf-8") as f:
            print(f.read(), end="")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
