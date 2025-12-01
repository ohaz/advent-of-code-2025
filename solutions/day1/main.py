import operator
import os

def get_example_input():
    s = """L68
L30
R48
L5
R60
L55
L1
L99
R14
L82"""
    return s.splitlines()

def get_input():
    with open('solutions/day1/input.txt') as f:
        return [x.strip() for x in f.readlines()]

def task1():
    data = get_input()
    value = 50
    reached_zero = 0
    directions = {
        'L': operator.sub,
        'R': operator.add,
    }
    for line in data:
        direction = directions[line[0]]
        value = direction(value, int(line[1:])) % 100
        if (value < 0):
            value += 100
        if value == 0:
            reached_zero += 1
    return reached_zero

def task2():
    data = get_input()
    value = 50
    reached_zero = 0
    directions = {
        'L': operator.sub,
        'R': operator.add,
    }
    for line in data:
        direction = directions[line[0]]
        times = int(line[1:])
        for _ in range(times):
            value = direction(value, 1)
            if (value == 100):
                value = 0
            if (value < 0):
                value = 99
            if value == 0:
                reached_zero += 1
    return reached_zero