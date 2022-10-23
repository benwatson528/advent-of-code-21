import os
from pathlib import Path

from main.day16.packet_decoder import solve


# A single packet with a literal value
def test_id_4_simple():
    assert solve("D2FE28") == 6


def test_2_sub_packets():
    assert solve("38006F45291200") == 9


# 3 sub-packets
def test_3_sub_packets():
    assert solve("EE00D40C823060") == 14


# The set of non-worked examples at the bottom of the page
def test_examples_1():
    assert solve("8A004A801A8002F478") == 16


def test_examples_2():
    assert solve("620080001611562C8802118E34") == 12


def test_examples_3():
    assert solve("C0015000016115A2E0802F182340") == 23


def test_examples_4():
    assert solve("A0016C880162017C3686B18A3D4780") == 31


def test_real():
    assert solve(read_input("data/input.txt")) == 886


def read_input(file_name):
    with open(os.path.join(Path(__file__).parent.absolute(), file_name)) as f:
        return f.readline().strip('\n')
