#!/usr/bin/env python3
import sys

def main():
    m = [list(line.rstrip()) for line in sys.stdin.readlines()]
    space_list = get_spaces(m)
    print(sum(distances(m, space_list, 2)), sum(distances(m, space_list, int(1e6))))
    
def get_spaces(m):
    space_list = []
    for i in range(0, 2):
        space_list.append([row for row, line in enumerate(m) if len(set(line)) == 1])
        m = list(map(list, zip(*m)))
    return space_list

def distances(m, space_list, space_length):
    galaxies = galaxy_list(m, space_list, space_length)
    return [distance(g1, g2) for i, g1 in enumerate(galaxies) for g2 in galaxies[i + 1:]]

def distance(g1, g2):
    return abs(g1[0] - g2[0]) + abs(g1[1] - g2[1])

def galaxy_list(m, space_list, space_length):
    return [(row + len([x for x in space_list[0] if x < row]) * (space_length - 1),
        col + len([x for x in space_list[1] if x < col]) * (space_length - 1))
        for row, line in enumerate(m) for col, tile in enumerate(line)
        if tile == '#']
            
if __name__ == '__main__':
    main()
