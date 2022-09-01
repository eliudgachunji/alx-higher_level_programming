#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    dictionary = sorted(a_dictionary.keys())
    for x in dictionary:
        print("{}: {}".format(x, a_dictionary.get(x)))
