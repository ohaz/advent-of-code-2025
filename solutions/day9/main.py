import os
import math

from shapely import Polygon, prepare
try:
    from tqdm import tqdm
except ImportError:
    tqdm = lambda x: x

def get_example_input():
    s = """7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3"""
    return s.splitlines()

def get_input():
    with open('solutions/day9/input.txt') as f:
        return [x.strip() for x in f.readlines()]

def task1():
    corners = [(int(line.split(',')[0]), int(line.split(',')[1])) for line in get_input()]
    largest = -1
    for i, c1 in enumerate(corners[:-1]):
        for j, c2 in enumerate(corners[i+1:]):
            largest = max(largest, abs(c2[0] - c1[0] - 1) * abs(c2[1] - c1[1] - 1))
    return largest

def generate_edges_for(corners):
    edges = []
    for c1, c2 in zip(corners, corners[1:] + [corners[0]]):
        diff_x = c2[0] - c1[0]
        diff_y = c2[1] - c1[1]
        step = (int(math.copysign(1, diff_x)) , 0) if diff_x != 0 else (0, int(math.copysign(1, diff_y)))
        current_point = c1
        while current_point != c2:
            edges.append(current_point)
            current_point = (current_point[0] + step[0], current_point[1] + step[1])
    return edges

def task2():
    corners = [(int(line.split(',')[0]), int(line.split(',')[1])) for line in get_input()]
    

    largest = -1

    polygon = Polygon(corners)
    prepare(polygon)

    for i, c1 in enumerate(tqdm(corners[:-1])):
        for c2 in corners[i+1:]:
            rect = Polygon([(c1[0], c1[1]), (c2[0], c1[1]), (c2[0], c2[1]), (c1[0], c2[1])])
            if polygon.contains(rect):
                largest = max(largest, abs(c2[0] - c1[0] - 1) * abs(c2[1] - c1[1] - 1))

    #full_edges_outside = generate_edges_for(corners)

    #for i, c1 in enumerate(tqdm(corners[:-1])):
    #    for j, c2 in enumerate(corners[i+1:]):
    #        for borderpiece in full_edges_outside:
    #            if (borderpiece[0] < max([c1[0], c2[0]]) and borderpiece[0] > min([c1[0], c2[0]])) and (borderpiece[1] < max([c1[1], c2[1]]) and borderpiece[1] > min([c1[1], c2[1]])):
    #                break
    #        else:
    #            largest = max(largest, abs(c2[0] - c1[0] - 1) * abs(c2[1] - c1[1] - 1))
    return largest