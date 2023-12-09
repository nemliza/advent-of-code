#!/usr/bin/env python3
import math, sys

def main():
    lines = sys.stdin.readlines()
    races1 = zip(*([int(i) for i in line.split(': ')[1].split()] for line in lines))
    race2 = [int(line.split(': ')[1].replace(' ', '')) for line in lines]
    print(math.prod(winning_races_count(race) for race in races1), winning_races_count(race2))

def winning_races_count(race):
    d = math.sqrt(race[0] ** 2 - 4 * race[1])
    return math.ceil((race[0] + d) / 2) - math.floor((race[0] - d) / 2) - 1

if __name__ == '__main__':
    main()
