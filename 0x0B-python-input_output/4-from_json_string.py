#!/usr/bin/python3
# 6-from_json_string.py
import json


def from_json_string(my_str):
    try:
        python_object = json.loads(my_str)
        return python_object
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None
