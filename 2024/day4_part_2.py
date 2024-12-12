#!/usr/bin/env python3
import sys

def main():
    puzzle = init()
    counter = 0
    for y in range(1, len(puzzle) - 1):
        for x in range(1, len(puzzle[y]) - 1):
            if puzzle[y][x] == 'A':
                counter += int(mas_match([line[x - 1 : x + 2] for line in puzzle[y - 1 : y + 2]]))
    print(counter)

def init():
    puzzle = sys.stdin.readlines()
    line_length = len(puzzle[0])
    return [' ' + line + ' ' for line in [' ' * line_length] + puzzle + [' ' * line_length]]

def mas_match(puzzle_part):
    top_left = puzzle_part[0][0]
    top_right = puzzle_part[0][2]
    bottom_left = puzzle_part[2][0]
    bottom_right = puzzle_part[2][2]
    return (
        (top_left == 'M' and top_right == 'M' and bottom_left == 'S' and bottom_right == 'S') or
        (top_left == 'S' and top_right == 'S' and bottom_left == 'M' and bottom_right == 'M') or
        (top_left == 'M' and bottom_left == 'M' and top_right == 'S' and bottom_right == 'S') or
        (top_left == 'S' and bottom_left == 'S' and top_right == 'M' and bottom_right == 'M')
    )

if __name__ == '__main__':
    main()
