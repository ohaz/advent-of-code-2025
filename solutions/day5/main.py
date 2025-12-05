import os
try:
    from tqdm import tqdm
except ImportError:
    tqdm = lambda x: x

def get_example_input():
    s = """3-5
10-14
16-20
12-18

1
5
8
11
17
32"""
    return s.splitlines()

def get_input():
    with open('solutions/day5/input.txt') as f:
        return [x.strip() for x in f.readlines()]

def split(input_data):
    split_index = input_data.index('')
    rules = input_data[:split_index]
    numbers = input_data[split_index + 1:]
    return rules, numbers

def task1():
    fresh_rules, ingredients = split(get_input())
    ranges = [range(int(r.split('-')[0]), int(r.split('-')[1]) + 1) for r in fresh_rules]
    valid_numbers = [n for n in ingredients if any(int(n) in r for r in ranges)]
    return len(valid_numbers)

def task2():
    fresh_rules, _ = split(get_input())
    ranges = [range(int(r.split('-')[0]), int(r.split('-')[1]) + 1) for r in fresh_rules]
    ranges.sort(key=lambda r: r.start)

    merged_ranges = [ranges[0]]
    for r in ranges[1:]:
        for i, concat_range in enumerate(merged_ranges):
              if r.start <= concat_range.stop:
                new_range = range(concat_range.start, max(concat_range.stop, r.stop))
                merged_ranges[i] = new_range
                break
        else:
            merged_ranges.append(r)
    length = 0
    for r in merged_ranges:
        length += len(r)
    return length