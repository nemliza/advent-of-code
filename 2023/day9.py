#!/usr/bin/env python3
import sys

def main():
    lines = [[int(num) for num in line.split()] for line in sys.stdin.readlines()]
    print(*(sum(x) for x in (zip(*(prediction(line) for line in lines)))))

def prediction(seq):
    first = []
    last = []
    par = 1
    while len(seq) > 1:
        first.append(seq[0] * par)
        last.append(seq[-1])
        seq = [b - a for a, b in zip(seq[:-1], seq[1:])]
        par *= -1
    return sum(last), sum(first)

if __name__ == '__main__':
    main()
