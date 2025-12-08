import os
import math

class Box():
    def __init__(self, line: str):
        self.x, self.y, self.z = map(int, line.split(','))
        self.circuit = None
    
    def distance(self, other: 'Box') -> int:
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2 + (self.z - other.z) ** 2)

    def put_in_circuit(self, circuit):
        self.circuit = circuit

    def get_circuit(self):
        return self.circuit
    
    def __repr__(self):
        return f'Box({self.x}, {self.y}, {self.z})'

class Circuit():
    def __init__(self, box = None):
        self.boxes = []
        if box is not None:
            self.add_box(box)

    def add_box(self, box: Box):
        self.boxes.append(box)
        box.put_in_circuit(self)
    
    def size(self):
        return len(self.boxes)
    
    def merge(self, other):
        self.boxes.extend(other.boxes)
        for box in other.boxes:
            box.put_in_circuit(self)

def get_example_input():
    s = """162,817,812
57,618,57
906,360,560
592,479,940
352,342,300
466,668,158
542,29,236
431,825,988
739,650,466
52,470,668
216,146,977
819,987,18
117,168,530
805,96,715
346,949,466
970,615,88
941,993,340
862,61,35
984,92,344
425,690,689"""
    return 10, s.splitlines()

def get_input():
    with open('solutions/day8/input.txt') as f:
        return 1000, [x.strip() for x in f.readlines()]

def task1():
    amount, lines = get_input()
    boxes = [Box(line) for line in lines]
    distances = []
    for i in range(len(boxes)):
        for j in range(i + 1, len(boxes)):
            distances.append((boxes[i].distance(boxes[j]), boxes[i], boxes[j]))
    distances.sort(key=lambda x: x[0])

    circuits = [Circuit(box) for box in boxes]

    for distance in distances[:amount]:
        distance, box1, box2 = distance
        circuit1 = box1.get_circuit()
        circuit2 = box2.get_circuit()
        if (circuit1 is None) and (circuit2 is None):
            raise ValueError('Both boxes have no circuit!')
        elif (circuit1 is not None) and (circuit2 is None):
            circuit1.add_box(box2)
        elif (circuit1 is None) and (circuit2 is not None):
            circuit2.add_box(box1)
        elif circuit1 != circuit2:
            circuit1.merge(circuit2)
            circuits.remove(circuit2)
    
    lengths = [circuit.size() for circuit in circuits]
    lengths.sort(reverse=True)
    
    return lengths[0] * lengths[1] * lengths[2]

def task2():
    amount, lines = get_input()
    boxes = [Box(line) for line in lines]
    distances = []
    for i in range(len(boxes)):
        for j in range(i + 1, len(boxes)):
            distances.append((boxes[i].distance(boxes[j]), boxes[i], boxes[j]))
    distances.sort(key=lambda x: x[0])

    circuits = [Circuit(box) for box in boxes]

    for distance in distances:
        distance, box1, box2 = distance
        circuit1 = box1.get_circuit()
        circuit2 = box2.get_circuit()
        if (circuit1 is None) and (circuit2 is None):
            raise ValueError('Both boxes have no circuit!')
        elif (circuit1 is not None) and (circuit2 is None):
            circuit1.add_box(box2)
        elif (circuit1 is None) and (circuit2 is not None):
            circuit2.add_box(box1)
        elif circuit1 != circuit2:
            circuit1.merge(circuit2)
            circuits.remove(circuit2)
            if len(circuits) == 1:
                return box1.x * box2.x
    raise ValueError('Did not merge into single circuit!')
