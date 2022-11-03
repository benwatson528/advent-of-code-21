import itertools

from day19.Coord import Coord

DIRECTIONS = [[1, 1, 1], [1, -1,  1], [1, -1, -1], [1,  1, -1], [-1,  1,  1], [-1, -1,  1], [-1, -1, -1], [-1,  1, -1]]

def solve(scanners) -> int:
    for scanner in scanners:
        for rotated in rotate(scanner):
            print()


def rotate(scanner):
    all_rotations = []

    for direction in DIRECTIONS:
        rotated_1 = []
        rotated_2 = []
        rotated_3 = []
        for coord in scanner:
            c_1 = coord.x * direction[0]
            c_2 = coord.y * direction[1]
            c_3 = coord.z * direction[2]
            rotated_1.append(Coord(c_1, c_2, c_3))
            rotated_2.append(Coord(c_2, c_1, c_3))
            rotated_3.append(Coord(c_3, c_2, c_1))
            rotated_3.append(Coord(c_1, c_3, c_2))
        print()

    all_rotations.append(rotated)


    return all_rotations # list of lists

