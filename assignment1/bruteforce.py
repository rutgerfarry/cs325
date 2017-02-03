"""Determines the closest set of points from a file passed as a command
line argument using a brute force algorithm"""

from sys import argv
from shared import point_list_from_file, Point

# Takes a list of points, returns unsorted list of tuples containing
# two points and the distance between them for every pair of points/
# Example: [(4, 1), (5, 1)] => [(1.0, (4, 1), (5, 1))]
def closest_pair_brute(points):
    distances = []
    for point1 in points:
        for point2 in points:
            if point1 != point2:
                distance_tuple = (Point.distance(point1, point2), point1, point2)
                distances.append(distance_tuple)
    return distances

POINT_LIST = point_list_from_file(argv[1])
print closest_pair_brute(POINT_LIST)
