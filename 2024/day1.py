#!/usr/bin/env python3
import sys

def main():
    numbers = [int(x) for x in sys.stdin.read().split()]
    left_list = numbers[::2]
    right_list = numbers[1::2]
    print(part_one(left_list, right_list), part_two(left_list, right_list))

def part_one(left_list, right_list):
    return sum([abs(item1 - item2) for item1, item2 in zip(sorted(left_list), sorted(right_list))])

def part_two(left_list, right_list):
    occurences = dict((x, right_list.count(x)) for x in set(right_list))
    return sum([x * occurences.get(x, 0) for x in left_list])

if __name__ == '__main__':
    main()
