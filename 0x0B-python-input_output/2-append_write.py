#!/usr/bin/python3
def append_write(filename="", text=""):
    try:
        with open(filename, "a", encoding="utf-8") as f:
            num_characters_appended = f.write(text)
            return num_characters_appended
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return 0
    except Exception as e:
        print(f"An error occurred: {e}")
        return 0
