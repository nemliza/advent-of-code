#!/usr/bin/env python3
import sys

def main():
    reports = [report[::-1] if report[0] > report[-1] else report for report in [list(map(int, line.split())) for line in sys.stdin.readlines()]]
    print(part_one(reports), part_two(reports))

def part_one(reports):
    return [safety_check(report) for report in reports].count(True)
    
def part_two(reports):
    return [dampener_check(report) for report in reports].count(True)
    
def dampener_check(report):
    return any([safety_check(report[:i] + report[i + 1:]) for i in range(len(report))])

def safety_check(report):
    return all(True if 1 <= item - report[i] <= 3 else False for i, item in enumerate(report[1:]))

if __name__ == '__main__':
    main()
