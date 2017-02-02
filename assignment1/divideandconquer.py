"""Determines the closest set of points from a file passed as a command
line argument using a naive divide and conquer algorithm"""

from sys import argv
from shared import point_list_from_file, Point

def closest_pair_dnc(points):
    # Recursive cases
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

    # Run recursive algorithm on left and right halves
    closest_pair = min(closest_pair_dnc(left_set), closest_pair_dnc(right_set))

    # Get middle set (technically a list)
    left_bound = median - closest_pair
    right_bound = median + closest_pair
    middle_set = [p for p in points if left_bound <= p.x <= right_bound]

    return closest_cross_pair(middle_set, closest_pair)

def closest_cross_pair(points, min_distance):
    points.sort(key=lambda point: point.y)
    for idx, point1 in enumerate(points):
        for point2 in points[idx + 1:]:
            if point2.y - point1.y > min_distance:
                break
            distance = Point.distance(point1, point2)
            min_distance = min(distance, min_distance)
    return min_distance

POINT_LIST = point_list_from_file(argv[1])
print closest_pair_dnc(POINT_LIST)
