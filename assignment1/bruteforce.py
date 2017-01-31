"""Determines the closest set of points from a file passed as a command
line argument"""

from sys import argv
from shared import point_list_from_file, distance

POINT_LIST = point_list_from_file(argv[1])

for point1 in POINT_LIST:
    for point2 in POINT_LIST:
        if point1 != point2:
            print distance(point1, point2)

print POINT_LIST
