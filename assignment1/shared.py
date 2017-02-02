import math

class Point(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return "({0}, {1})".format(self.x, self.y)

    def __repr__(self):
        return "({0}, {1})".format(self.x, self.y)

    @staticmethod
    def distance(point1, point2):
        return math.sqrt((point1.x - point2.x)**2 + (point1.y - point2.y)**2)

# Converts a string representing a point to a Point instance
def point_from_string(point_string):
    point_list = point_string.split(' ')
    if len(point_list) != 2:
        return

    point_list = map(float, point_list)
    point = Point(point_list[0], point_list[1])
    return point

# Opens file containing newline-delimited list of points and
# returns a list of Points.
def point_list_from_file(filename):
    point_file = open(filename, 'r').read()
    points = map(point_from_string, point_file.split('\n'))
    return filter(None, points)
