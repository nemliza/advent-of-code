#!/usr/bin/env python3
import math, sys

def main():
    lines = sys.stdin.readlines()
    instructions = lines[0].rstrip()
    nodes = {k: v for k, v in (get_node(line) for line in lines[2:])}
    print(part_1(nodes, instructions), part_2(nodes, instructions))
    
def part_1(nodes, instructions):
    location = 'AAA'
    i = 0
    steps = 0
    while location != 'ZZZ':
        location = nodes[location][instructions[i]]
        i = ((i + 1) % len(instructions))
        steps += 1
    return steps

def part_2(nodes, instructions):
    locations = [k for k in nodes.keys() if k[2] == 'A']
    i = 0
    steps = [0] * len(locations)
    for j, location in enumerate(locations):
        while location[2] != 'Z':
            location = nodes[location][instructions[i]]
            i = ((i + 1) % len(instructions))
            steps[j] += 1
    return math.lcm(*steps)

def get_node(line):
    for char in '=,()':
        line = line.replace(char, '')
    s = line.split()
    return s[0], {'L': s[1], 'R':s[2]}

if __name__ == '__main__':
    main()
