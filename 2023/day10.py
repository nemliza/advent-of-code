#!/usr/bin/env python3
import sys

directions = {
    '|': {(-1, 0), (1, 0)},
    '-': {(0, -1), (0, 1)},
    'L': {(-1, 0), (0, 1)},
    'J': {(-1, 0), (0, -1)},
    '7': {(1, 0), (0, -1)},
    'F': {(1, 0), (0, 1)}
}

def main():
    m = [line.rstrip() for line in sys.stdin.readlines()]
    start = find_start(m)
    set_start_tile(m, *start)
    path = find_path(m, *start)
    area = path_area(m, path)
    print(len(path) // 2, area)

def find_start(m):
    return [(i, line.index('S')) for i, line in enumerate(m) if 'S' in line][0]

def find_path(m, row, col):
    path = [(row, col)]
    last_row = None
    start_row = row
    start_col = col
    while row != start_row or col != start_col or last_row == None:
        for d in directions[m[row][col]]:
            next_row = row + d[0]
            next_col = col + d[1]
            if next_row != last_row or next_col != last_col:
                path.append((row, col))
                last_row = row
                last_col = col
                row = next_row
                col = next_col
                break
    return path

def set_start_tile(m, row, col):
    start_dirs = set()
    if row >= 1 and m[row - 1][col] in '|7F':
        start_dirs.add((-1, 0))
    if row < len(m) - 1 and m[row + 1][col] in '|LJ':
        start_dirs.add((1, 0))
    if col >= 1 and m[row][col - 1] in '-LF':
        start_dirs.add((0, -1))
    if col < len(m[row]) - 1 and m[row][col + 1] in '-J7':
        start_dirs.add((0, 1))
    m[row] = m[row].replace('S', list(directions.keys())[list(directions.values()).index(start_dirs)])

def path_area(m, path):
    area = 0
    inside = lower_edge = False
    for row, line in enumerate(m):
        for col, tile in enumerate(line):
            if (row, col) in path:
                match tile:
                    case 'L':
                        lower_edge = True
                    case '|':
                        inside = not inside
                    case 'J':
                        if not lower_edge:
                            inside = not inside
                        lower_edge = False
                    case '7':
                        if lower_edge:
                            inside = not inside
                        lower_edge = False
            elif inside:
                area += 1
    return area

if __name__ == '__main__':
    main()
