#!/usr/bin/env python3
import sys

def main():
    sum1 = 0
    sum2 = 0
    for line in sys.stdin:
        line = line.rstrip()
        sum1 += get_digit_1(line) * 10 + get_digit_1(line[::-1])
        sum2 += get_digit_2(line, range(0, len(line))) * 10 + \
                get_digit_2(line, range(len(line) - 1, -1, -1))
    print(sum1, sum2)
    
def get_digit_1(line):
    for char in line:
        if char.isdigit():
            return int(char)

def get_digit_2(line, range):
    for i in range:
        if line[i].isdigit():
            return int(line[i])
        digit = get_spelled_out_digit(line[i:])
        if digit:
            return digit
    return 0

def get_spelled_out_digit(str):
    for i, number in enumerate(['one', 'two', 'three', 'four', 'five', 'six',
        'seven', 'eight', 'nine']):
        if str.startswith(number):
            return i + 1

if __name__ == '__main__':
    main()
