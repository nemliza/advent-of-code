#!/usr/bin/env python3
import sys, re

def main():
    lines = [line.rstrip() for line in sys.stdin.readlines()]
    sum1 = 0
    cards2 = [1] * len(lines)
    for i, line in enumerate(lines):
        p = get_winning_numbers(line)
        sum1 += int(2 ** (p - 1))
        for j in range(i + 1, i + p + 1):
            cards2[j] += cards2[i]            
    print(sum1, sum(cards2))
    
def get_winning_numbers(line):
    id, winning_numbers, own_numbers = re.split(': | \| ', line)
    winning_numbers = winning_numbers.split()
    own_numbers = own_numbers.split()
    return len([n for n in winning_numbers if n in own_numbers])

if __name__ == '__main__':
    main()
