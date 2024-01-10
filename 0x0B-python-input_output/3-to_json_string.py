#!/usr/bin/python3
import json


def to_json_string(my_obj):
    try:
        json_string = json.dumps(my_obj)
        return json_string
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
