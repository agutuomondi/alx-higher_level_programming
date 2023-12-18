#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    new_list = []

    for x, y in zip(my_list_1[:list_length], my_list_2[:list_length]):
        try:
            div = x / y
        except TypeError:
            print("wrong type")
            div = 0
        except ZeroDivisionError:
            print("division by 0")
            div = 0
        except Exception as e:
            print("An unexpected error occurred:", e)
            div = 0
        finally:
            new_list.append(div)

    return new_list
