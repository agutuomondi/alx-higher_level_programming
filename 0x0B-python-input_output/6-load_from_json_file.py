#!/usr/bin/python3
import json


def load_from_json_file(filename):
    try:
        with open(filename) as f:
            json_object = json.load(f)
            return json_object
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return None
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON in file '{filename}': {e}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None
