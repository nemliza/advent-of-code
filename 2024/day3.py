#!/usr/bin/env python3
import sys, re

def main():
    code = sys.stdin.read()
    print(sum([int(item[0]) * int(item[1]) for item in re.findall('mul\(([0-9]+),([0-9]+)\)', code)]))
    occurences = re.findall('mul\(([0-9]+),([0-9]+)\)|(do[n\'t]*\(\))', code)
    counter = 0
    count_switch = True
    for item in occurences:
        if item[2] == 'do()':
            count_switch = True
        elif item[2] == 'don\'t()':
            count_switch = False
        elif count_switch:
            counter += int(item[0]) * int(item[1])
    print(counter)

if __name__ == '__main__':
    main()
