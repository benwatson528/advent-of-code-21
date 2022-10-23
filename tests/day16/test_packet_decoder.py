import os
from pathlib import Path

from main.day16.packet_decoder import solve


def test_id_4_simple():
    assert solve("D2FE28")[0] == 6


def test_2_sub_packets():
    assert solve("38006F45291200")[0] == 9


def test_3_sub_packets():
    assert solve("EE00D40C823060")[0] == 14


# The set of non-worked examples at the bottom of the page
def test_examples_1():
    assert solve("8A004A801A8002F478")[0] == 16


def test_examples_2():
    assert solve("620080001611562C8802118E34")[0] == 12


def test_examples_3():
    assert solve("C0015000016115A2E0802F182340")[0] == 23


def test_examples_4():
    assert solve("A0016C880162017C3686B18A3D4780")[0] == 31


def test_part_1_real():
    assert solve(read_input("data/input.txt"))[0] == 886


def test_operators_sum():
    assert solve("C200B40A82")[1] == 3


def test_operators_product():
    assert solve("04005AC33890")[1] == 54


def test_operators_minimum():
    assert solve("880086C3E88112")[1] == 7


def test_operators_maximum():
    assert solve("CE00C43D881120")[1] == 9


def test_operators_less_than():
    assert solve("D8005AC2A8F0")[1] == 1


def test_operators_greater_than():
    assert solve("F600BC2D8F")[1] == 0


def test_operators_equality():
    assert solve("9C005AC2F8F0")[1] == 0


def test_operators_sum_and_equality():
    assert solve("9C0141080250320F1802104A08")[1] == 1


def test_part_2_real():
    assert solve(read_input("data/input.txt"))[1] == 184487454837


def read_input(file_name):
    with open(os.path.join(Path(__file__).parent.absolute(), file_name)) as f:
        return f.readline().strip('\n')
