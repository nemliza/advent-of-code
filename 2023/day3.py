#!/usr/bin/env python3
import sys, math

def main():
    sum1 = sum2 = 0
    lines = [line.rstrip() for line in sys.stdin.readlines()]

    cur_lines = [lines[0], lines[1]]
    for line in lines[2:]:
        cur_lines.append(line)
        sum1 += sum(line_sum(cur_lines))
        sum2 += sum(line_prod(cur_lines))
        cur_lines.pop(0)
    print(sum1, sum2)

def line_sum(lines):
    return [sum(symbol_numbers(lines, position)) for position in \
        [i for i, symbol in enumerate(lines[1]) if symbol in '#$%&*+-/=@']]
        
def line_prod(lines):
    return [math.prod(i) for i in (symbol_numbers(lines, position) for position in \
        [i for i, symbol in enumerate(lines[1]) if symbol == '*'])
        if len(i) > 1]

def symbol_numbers(lines, symbol_position):
    numbers = []
    get_number(numbers, lines[1], symbol_position - 1)
    get_number(numbers, lines[1], symbol_position + 1)
    for i in [0, 2]: 
        if not get_number(numbers, lines[i], symbol_position):
            get_number(numbers, lines[i], symbol_position - 1)
            get_number(numbers, lines[i], symbol_position + 1)
    return [i for i in numbers if i]
    
def get_number(numbers, line, position):
    if line[position].isdigit():
        start = end = position
        while start >= 0 and line[start].isdigit():
            start -= 1
        while end < len(line) and line[end].isdigit():
            end += 1
        numbers.append(int(line[start + 1 : end]))
        return True
    else:
        return False

if __name__ == '__main__':
    main()
