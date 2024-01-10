#!/usr/bin/python3
def write_file(filename="", text=""):
    try:
        with open(filename, "w", encoding="utf-8") as f:
            num_characters_written = f.write(text)
            return num_characters_written
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return 0
    except Exception as e:
        print(f"An error occurred: {e}")
        return 0
