"""Determines the closest set of points from a file passed as a command
line argument using a divide and conquer algorithm"""

from sys import argv
from shared import point_list_from_file, Point

def enhanced_closest_pair_dnc(x_sorted_points, y_sorted_points):
    # Recursive cases
    if len(x_sorted_points) == 3:
        dist1 = Point.distance(x_sorted_points[0], x_sorted_points[1])
        dist2 = Point.distance(x_sorted_points[1], x_sorted_points[2])
        return min(dist1, dist2)

    elif len(x_sorted_points) == 2:
        return Point.distance(x_sorted_points[0], x_sorted_points[1])

    elif len(x_sorted_points) <= 1:
        print 'One or zero points given, distance is zero'
        return 0

    # Split into left and right halves
    middle_index = len(x_sorted_points) / 2
    median = x_sorted_points[middle_index].x
    x_left_set = x_sorted_points[:middle_index]
    x_right_set = x_sorted_points[middle_index:]

    # Find intersection of halves and y-sorted lists
    y_left_set = [p for p in y_sorted_points if p in x_left_set]
    y_right_set = [p for p in y_sorted_points if p in x_right_set]

    # Run recursive algorithm on left and right halves
    closest_pair = min(
        enhanced_closest_pair_dnc(x_left_set, y_left_set),
        enhanced_closest_pair_dnc(x_right_set, y_right_set))

    # Get middle set (technically a list)
    left_bound = median - closest_pair
    right_bound = median + closest_pair
    middle_set = [p for p in y_sorted_points if left_bound <= p.x <= right_bound]

    return closest_cross_pair(middle_set, closest_pair)

def closest_cross_pair(points, min_distance):
    for idx, point1 in enumerate(points):
        for point2 in points[idx + 1:]:
            if point2.y - point1.y > min_distance:
                break
            distance = Point.distance(point1, point2)
            min_distance = min(distance, min_distance)
    return min_distance

def enhanced_closest_pair_dnc_main(points):
    x_sorted_points = sorted(points, key=lambda point: point.x)
    y_sorted_points = sorted(points, key=lambda point: point.y)

    return enhanced_closest_pair_dnc(
        x_sorted_points,
        y_sorted_points)

POINT_LIST = point_list_from_file(argv[1])
print enhanced_closest_pair_dnc_main(POINT_LIST)
