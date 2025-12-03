import os

def get_example_input():
    s = """987654321111111
811111111111119
234234234234278
818181911112111"""
    return s.splitlines()

def get_input():
    with open('solutions/day3/input.txt') as f:
        return [x.strip() for x in f.readlines()]

def javascript_style_sum(a, b):
    return int(str(a) + str(b))

def task1():
    joltage = 0
    for bank in get_input():
        entries = [int(x) for x in bank]
        highest_index = entries.index(max(entries[:-1]))
        second_highest_index = entries.index(max(entries[highest_index+1:]))
        joltage += javascript_style_sum(entries[highest_index], entries[second_highest_index])
    return joltage

def find_best_starter(bank_slice, length):
    entries = [int(x) for x in bank_slice]
    highest_index = entries.index(max(entries[:-length]))
    return highest_index

def recurse(bank_slice, length):
    entries = [int(x) for x in bank_slice]
    required_entries = entries[:-length] if length > 0 else entries
    highest_index = entries.index(max(required_entries))
    value = str(entries[highest_index])
    if length > 0:
        value += recurse(bank_slice[highest_index+1:], length - 1)
    return value

def task2():
    REQUIRED_DIGITS = 12
    joltage = 0
    for bank in get_input():

        value = int(recurse(bank, REQUIRED_DIGITS - 1))
        joltage += value

    return joltage
