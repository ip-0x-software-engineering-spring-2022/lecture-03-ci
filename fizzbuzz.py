"""
This is an implementation of famous fizzbuzz problem
We do this just for demonstration
"""

import argparse


def fizzbuzz(i):
    if i % 15 == 0:
        print("fizzbuzz")
    elif i % 5 == 0:
        print("buzz")
    elif i % 3 == 0:
        print("fizz")
    else:
        print(str(i))

if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('number', type=int)
    cli = ap.parse_args()

    for i in range(1, cli.number + 1):
        fizzbuzz(i)
