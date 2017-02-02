"""Determines the closest set of points from a file passed as a command
line argument using a naive divide and conquer algorithm"""

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
    points.sort(key=lambda point: point.x)

    middle_index = len(points) / 2
    median = points[middle_index].x
    left_set = points[:middle_index]
    right_set = points[middle_index:]

    closest_pair = min(closest_pair_dnc(left_set), closest_pair_dnc(right_set))

    left_bound = median - closest_pair
    right_bound = median + closest_pair

    middle_set = [p for p in points if left_bound <= p.x <= right_bound]
    middle_set.sort(key=lambda point: point.y)

    print "points: {0}".format(points)
    print "median: {0}".format(median)
    print "closest_pair: {0}".format(closest_pair)
    print "left_bound: {0}".format(left_bound)
    print "right_bound: {0}".format(right_bound)
    print "middle_set: {0}".format(middle_set)

    return closest_pair

def closest_cross_pair(points, distance):
    return None


POINT_LIST = point_list_from_file(argv[1])
print closest_pair_dnc(POINT_LIST)
