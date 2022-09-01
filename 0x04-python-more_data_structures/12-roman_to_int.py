#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or isinstance(roman_string, str) is False:
        return 0
    roman_num = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
            }
    reverse_num = roman_string[::-1]
    maxchar = 'I'
    sum = 0
    for i in reverse_num:
        if roman_num[i] >= roman_num[maxchar]:
            maxchar = i
            sum += roman_num[i]
        else:
            sum -= roman_num[i]
    return sum
