import os
import operator
from functools import reduce
import re

class Operation():

    def __init__(self, operator=None):
        self.operands = []
        self.operator = operator
    
    def add_operand(self, operand):
        self.operands.append(int(operand))
    
    def add_operator(self, operator):
        self.operator = operator
    
    def __str__(self):
        return f'{str(self.operator)} on {[str(x) for x in self.operands]}'
    
    def __repr__(self):
        return str(self)
    
    def run(self):
        return reduce(self.operator, self.operands)

def get_example_input():
    s = """123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  """
    return s.splitlines()

def get_input():
    with open('solutions/day6/input.txt') as f:
        return [x for x in f.readlines()]

r = re.compile(r'\s*([^\s]+)\s*')

operator_translation = {
    "*": operator.mul,
    "+": operator.add,
}

def task1():
    data = get_input()
    operators = r.findall(data[-1])
    operations = [Operation(operator_translation[op]) for op in operators]
    for line in data[:-1]:
        operands = r.findall(line)
        for i, operand in enumerate(operands):
            operations[i].add_operand(operand)
    result = 0
    for operation in operations:
        result += operation.run()
    return result

def find_ends_of_calculations(string):
    indices = []
    for i, c in enumerate(string[1:]):
        if c != ' ':
            indices.append(i)
    indices.append(len(string))
    return indices

def task2():
    data = get_input()
    operators = data[-1]
    operands = data[:-1]
    ops = []
    ends = find_ends_of_calculations(operators)
    cursor = 0
    for end in ends:
        ops.append([])
        for operand_row in operands:
            ops[-1].append(operand_row[cursor:end])
        cursor = end + 1
    operations = [Operation(operator_translation[x]) for x in r.findall(data[-1])]
    for op_index, op in enumerate(ops):
        for i in range(len(op[0])):
            new_number = int(''.join([op[x][-(i+1)] for x in range(len(op)) if i < len(op[x])]))
            operations[op_index].add_operand(new_number)
    final_sum = 0
    for current_op in operations:
        value = current_op.run()
        final_sum += value
    return final_sum