import re
import sys

class CostMatrix(object):
    def __init__(self, matrix_string):
        # Remove non-alphanumerics and split into list
        matrix_string = re.sub(r'[^\w\*-]+', '', matrix_string)
        self.matrix = [char for char in matrix_string]

        if len(self.matrix) != 36:
            sys.exit("Error: cost file should be 6x6")

        self.first_row = self.matrix[0:6]
        self.first_col = self.matrix[0::6]

        # Transform list from 1x36 -> 6x6
        self.matrix = [self.matrix[i:i + 6] for i in range(0, 36, 6)]

    @classmethod
    def from_file(cls, filename):
        f = open(filename, 'r').read()
        cost_matrix = CostMatrix(f)
        return cost_matrix

    def cost_for(self, char1, char2):
        i = self.first_row.index(char1)
        j = self.first_col.index(char2)
        return int(self.matrix[i][j])

# Returns a list of tuples containing two strings representing gene sequences
# e.g. [("ACTG", "GGCC")]
def load_sequences_from_file(filename):
    f = open(filename, 'r').read()
    # Split on newlines, remove empty strings, create sequence tuples
    sequences = f.split('\n')
    sequences = [x for x in sequences if len(x) > 0]
    sequences = [(x.split(',')[0], x.split(',')[1]) for x in sequences]
    return sequences

def print_dynamic_table(table):
    flat_table = [el for sub_list in table for el in sub_list]
    longest_element = len(str(max(flat_table)))
    for sub_list in table:
        line = ''
        for el in sub_list:
            padding = longest_element - len(str(el)) + 1
            line += ''.join(' ' * padding + str(el))
        print line
