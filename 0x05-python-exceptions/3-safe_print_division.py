#!/usr/bin/python3

def safe_print_division(a, b):
    try:
        div = a / b
    except ZeroDivisionError:
        div = None
        print("Error: Division by zero")
    except TypeError:
        div = None
        print("Error: Invalid types for division")
    return div

result = safe_print_division(4, 2)
print("Inside result:", result)
