#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or a_dictionary == {}:
        return None
    keys = list(a_dictionary.keys())
    max = keys[0]
    for k in keys:
        max = k if a_dictionary[k] > a_dictionary[max] else max
    return
