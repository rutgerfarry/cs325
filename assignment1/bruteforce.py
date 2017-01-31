"""Determines the closest set of points from a file passed as a command
line argument"""

from sys import argv
from shared import point_list_from_file, Point

# Takes a list of points, returns unsorted list of tuples containing
# two points and the distance between them for every pair of points/
# Example: [(4, 1), (5, 1)] => [(1.0, (4, 1), (5, 1))]
def bruteforce(point_list):
    distances = []
    for point1 in point_list:
        for point2 in point_list:
            if point1 != point2:
                distance_tuple = (Point.distance(point1, point2), point1, point2)
                distances.append(distance_tuple)
    return distances

POINT_LIST = point_list_from_file(argv[1])
print bruteforce(POINT_LIST)
