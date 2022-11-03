import itertools
import os
import re
from pathlib import Path

from day19.Coord import Coord
from main.day19.beacon_scanner import solve


def test_simple():
    assert solve(read_input("data/test_input.txt")) == 79


def test_real():
    assert solve(read_input("data/input.txt")) == 0


def read_input(file_name):
    with open(os.path.join(Path(__file__).parent.absolute(), file_name)) as f:
        scanners = {}
        beacons = []
        scanner_no = -1
        for line in f:
            stripped = line.strip('\n')
            if len(stripped) == 0:
                scanners[scanner_no] = beacons
                beacons = []
            elif stripped.startswith("---"):
                scanner_no = int(re.findall(r'\d+', stripped)[0])
            else:
                split = stripped.split(",")
                coord = Coord(int(split[0]), int(split[1]), int(split[2]))
                beacons.append(coord)
        scanners[scanner_no] = beacons
        return scanners
