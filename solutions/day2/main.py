import os

def get_example_input():
    s = """11-22,95-115,998-1012,1188511880-1188511890,222220-222224,
1698522-1698528,446443-446449,38593856-38593862,565653-565659,
824824821-824824827,2121212118-2121212124"""
    return s.replace("\n", "").replace("\r", "").split(",")

def get_input():
    with open('solutions/day2/input.txt') as f:
        return f.read().split(",")

def task1():
    invalids = 0
    for range_pair in get_input():
        values = range(int(range_pair.split("-")[0]), int(range_pair.split("-")[1]) + 1)
        for v in values:
            first_part, second_part = str(v)[:len(str(v))//2], str(v)[len(str(v))//2:]
            if first_part == second_part:
                invalids += v
    return invalids

def task2():
    invalids = 0
    for range_pair in get_input():
        values = range(int(range_pair.split("-")[0]), int(range_pair.split("-")[1]) + 1)
        for v in values:
            possible_patterns = []
            for i in range(1, len(str(v))):
                pattern, rest = str(v)[:i], str(v)[i:]
                if rest.replace(pattern, "") == "":
                    possible_patterns.append(pattern)
            if possible_patterns:
                invalids += v
    return invalids