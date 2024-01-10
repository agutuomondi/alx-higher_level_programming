#!/usr/bin/python3
import json


def save_to_json_file(my_obj, filename):
    try:
        with open(filename, "w") as f:
            json.dump(my_obj, f)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
