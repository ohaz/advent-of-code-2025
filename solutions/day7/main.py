import os
from collections import defaultdict

def get_example_input():
    s = """.......S.......
...............
.......^.......
...............
......^.^......
...............
.....^.^.^.....
...............
....^.^...^....
...............
...^.^...^.^...
...............
..^...^.....^..
...............
.^.^.^.^.^...^.
..............."""
    return s.splitlines()

def get_input():
    with open('solutions/day7/input.txt') as f:
        return [x.strip() for x in f.readlines()]

def task1():
    grid = get_input()
    splits = 0
    positions = [(0, grid[0].index('S'))]
    while (any([pos for pos in positions if pos[0] + 1 < len(grid)])):
        new_positions = []
        for pos in positions:
            new_position = (pos[0] + 1, pos[1])
            if grid[new_position[0]][new_position[1]] == "^":
                new_positions.append((new_position[0], new_position[1] - 1))
                new_positions.append((new_position[0], new_position[1] + 1))
                splits += 1
            else:
                new_positions.append(new_position)
        positions = list(set(new_positions))
            
    return splits

def add_position(new_positions, x, y, modifier=1):
    for index, pos in enumerate(new_positions):
        if pos[0] == x and pos[1] == y:
            new_positions[index] = (pos[0], pos[1], pos[2] + modifier)
            break
    else:
        new_positions.append((x,y,modifier))

def task2():
    grid = get_input()
    splits = 1
    positions = [(0, grid[0].index('S'), 1)]
    while (any([pos for pos in positions if pos[0] + 1 < len(grid)])):
        new_positions = []
        for pos in positions:
            new_position = (pos[0] + 1, pos[1], pos[2])
            if grid[new_position[0]][new_position[1]] == "^":
                add_position(new_positions, new_position[0], new_position[1] - 1, new_position[2])
                add_position(new_positions, new_position[0], new_position[1] + 1, new_position[2])
                splits += 1
            else:
                add_position(new_positions, new_position[0], new_position[1], new_position[2])
        positions = new_positions
    count = 0
    for pos in positions:
        count += pos[2]
            
    return count