"""Outputs a sample cost file"""

from random import randint

EMPTY_MATRIX = [
    ["*", "-", "A", "T", "G", "C"],
    ["-", "#", "#", "#", "#", "#"],
    ["A", "#", "#", "#", "#", "#"],
    ["T", "#", "#", "#", "#", "#"],
    ["G", "#", "#", "#", "#", "#"],
    ["C", "#", "#", "#", "#", "#"]
]

def random_cost_matrix(empty_matrix):
    matrix = []
    for submatrix in empty_matrix:
        matrix.append([replace_placeholder(x) for x in submatrix])
    return matrix

def replace_placeholder(x):
    if x == "#":
        return str(randint(0, 9))
    return x
