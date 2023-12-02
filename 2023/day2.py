#!/usr/bin/env python3
import sys

def main():
    sum1 = 0
    sum2 = 0
    for line in sys.stdin:
        line = line_to_dict(line.rstrip())
        sum1 += value_if_possible(line)
        sum2 += max_number(line, 'red') * \
                max_number(line, 'green') * \
                max_number(line, 'blue')
    print(sum1, sum2)
    
def line_to_dict(line):
    dict = {}
    id, sets = line.split(': ')
    dict['id'] = int(id[5:])
    dict['sets'] = [{item[1]: int(item[0]) for item in
        [draw.split() for draw in set.split(', ')]}
        for set in sets.split('; ')]
    return dict

def value_if_possible(line):
    for set in line['sets']:
        if 'red' in set and set['red'] > 12 or \
           'green' in set and set['green'] > 13 or \
           'blue' in set and set['blue'] > 14:
            return 0
    return line['id']

def max_number(line, color):
    values = []
    for set in line['sets']:
        if color in set:
            values.append(set[color])
    return max(values)

if __name__ == '__main__':
    main()
