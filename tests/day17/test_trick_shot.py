import re

from day17.Bounds import Bounds
from main.day17.trick_shot import solve


def test_simple():
    assert solve(parse_input("target area: x=20..30, y=-10..-5")) == 45


def test_real():
    assert solve(parse_input("target area: x=128..160, y=-142..-88")) == 10011


def parse_input(x):
    vals = re.findall(r'[-+]?(?:\d{1,3}(?:,\d{3})+|\d+)(?:\.\d+)?', x)
    return Bounds(int(vals[0]), int(vals[1]), int(vals[2]), int(vals[3]))
