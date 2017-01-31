import math

# Converts a string representing points to an int tuple, e.g. '4 1' => (4, 1).
def point_tuple_from_string(point_string):
    if len(point_string) < 3:
        return

    point_list = point_string.split(' ')
    point_tuple = tuple(map(int, point_list))
    return point_tuple

# Opens file containing newline-delimited list of points and
# returns a list of int tuples.
def point_list_from_file(filename):
    point_file = open(filename, 'r').read()
    point_tuples = map(point_tuple_from_string, point_file.split('\n'))
    return filter(None, point_tuples)

def distance(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)
