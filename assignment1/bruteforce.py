"""Determines the closest set of points from a file passed as a command
line argument using a brute force algorithm"""

from sys import argv
from shared import point_list_from_file, Point

# Takes a list of points, returns unsorted list of tuples containing
# two points and the distance between them for every pair of points/
# Example: [(4, 1), (5, 1)] => [(1.0, (4, 1), (5, 1))]
def closest_pair_brute(points):
    distances = []
    min_distance = float('inf')
    for idx, point1 in enumerate(points):
        for point2 in points[idx + 1:]:
            if point1 != point2:
                distance = Point.distance(point1, point2)
                min_distance = distance if distance < min_distance else min_distance
                distance_tuple = (distance, point1, point2)
                distances.append(distance_tuple)
    return format_point_list(distances, min_distance)

def format_point_list(points, min_distance):
    closest_points = [p for p in points if p[0] == min_distance]
    closest_points.sort(key=lambda point: point[1].x)
    closest_points.sort(key=lambda point: point[1].y)

    point_string = str(min_distance)
    for p in closest_points:
        point_string += "\n{0} {1} {2} {3}".format(
            p[1].x,
            p[1].y,
            p[2].x,
            p[2].y)
    return point_string

POINT_LIST = point_list_from_file(argv[1])
print closest_pair_brute(POINT_LIST)
