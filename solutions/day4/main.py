import os

def get_example_input():
    s = """..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@."""
    return s.splitlines()

def get_input():
    with open('solutions/day4/input.txt') as f:
        return [x.strip() for x in f.readlines()]

def transform_input(input_data):
    row_size = len(input_data[0])
    input_data.append('.' * row_size)
    input_data.insert(0, '.' * row_size)
    for index in range(len(input_data)):
        row = input_data[index]
        input_data[index] = '.' + row + '.'
    return input_data

def find_valid_positions(grid):
    valid_positions = []
    for row_index, row in enumerate(grid):
        for col_index, col in enumerate(row):
            if col != '@':
                continue
            # Check adjacent cells
            adjacent = [
                grid[row_index - 1][col_index - 1], grid[row_index - 1][col_index], grid[row_index - 1][col_index + 1],
                grid[row_index][col_index - 1], grid[row_index][col_index + 1],
                grid[row_index + 1][col_index - 1], grid[row_index + 1][col_index], grid[row_index + 1][col_index + 1]
            ]
            if adjacent.count('@') < 4:
                valid_positions.append((row_index, col_index))
    return valid_positions

def task1():
    grid = transform_input(get_input())
    valid_positions = find_valid_positions(grid)
    return len(valid_positions)

def task2():
    grid = transform_input(get_input())
    count = 0
    while True:
        valid_positions = find_valid_positions(grid)
        if not valid_positions:
            break
        for row_index, col_index in valid_positions:
            grid[row_index] = grid[row_index][:col_index] + '.' + grid[row_index][col_index + 1:]
            count += 1
    return count