#!/usr/bin/python3
import sys
import json

def add_arguments_to_list_and_save(arguments, filename):
    try:
        with open(filename, "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = []

    data.extend(arguments)

    with open(filename, "w") as file:
        json.dump(data, file)

if __name__ == "__main__":
    try:
        add_arguments_to_list_and_save(sys.argv[1:], "add_item.json")
    except Exception as e:
        print(f"An error occurred: {e}")
