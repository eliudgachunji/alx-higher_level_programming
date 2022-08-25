#!/usr/bin/python3

if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv
    n = len(argv)
    if n != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        quit(1)
    a = int(argv[1])
    b = int(argv[3])
    ops = argv[2]
    funcs = {"+": add, "-": sub, "*": mul, "/": div}
    if ops not in list(funcs.keys()):
        print("Unknown operator. Available operators: +, -, * and /")
        quit(1)
print("{} {} {} = {}".format(a, ops, b, funcs[ops](a, b)))
