"""Determines the closest set of points from a file passed as a command
line argument using a divide and conquer algorithm"""

from sys import argv
from shared import point_list_from_file, Point

def closest_pair_dnc(points):
    if len(points) == 3:
        dist1 = Point.distance(points[0], points[1])
        dist2 = Point.distance(points[1], points[2])
        return min(dist1, dist2)

    elif len(points) == 2:
        return Point.distance(points[0], points[1])

    elif len(points) <= 1:
        print 'One or zero points given, distance is zero'
        return 0

    # Split into left and right halves
    sorted_points = sorted(points, key=lambda point: point.x)
    print sorted_points
    median = len(sorted_points) / 2
    left = sorted_points[:median]
    right = sorted_points[median:]

    closest_pair = min(closest_pair_dnc(left), closest_pair_dnc(right))

    return closest_pair

POINT_LIST = point_list_from_file(argv[1])
print closest_pair_dnc(POINT_LIST)
