#!/usr/bin/env python3
import sys

def main():
    puzzle = init()
    word_list = []
    for y in range(0, len(puzzle) - 3):
        for x in range(0, len(puzzle[y]) - 3):
            word_list.append(puzzle[y][x] + puzzle[y][x + 1] + puzzle[y][x + 2] + puzzle[y][x + 3])
            word_list.append(puzzle[y][x] + puzzle[y + 1][x] + puzzle[y + 2][x] + puzzle[y + 3][x])
            word_list.append(puzzle[y][x] + puzzle[y + 1][x + 1] + puzzle[y + 2][x + 2] + puzzle[y + 3][x + 3])
            word_list.append(puzzle[y + 3][x] + puzzle[y + 2][x + 1] + puzzle[y + 1][x + 2] + puzzle[y][x + 3])
    print(word_list.count('XMAS') + word_list.count('SAMX'))

def init():
    puzzle = sys.stdin.readlines()
    line_length = len(puzzle[0])
    return [line + '   ' for line in puzzle + [' ' * line_length] * 3]

if __name__ == '__main__':
    main()
