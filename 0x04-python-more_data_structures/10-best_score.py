#!/usr/bin/python3

def best_score(my_dict):
    return max(my_dict.items(), key=lambda x: x[1])[0] if my_dict else None
