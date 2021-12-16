import os
from pathlib import Path

from main.day16.packet_decoder import solve


# a single packet with a number
def test_id_4_simple():
    assert solve("D2FE28") == 2021


# # 2 sub-packets
# def test_length_id_0_simple():
#     assert solve("38006F45291200") == 30
#
#
# def test_real():
#     assert solve(read_input("data/input.txt")) == 0


def read_input(file_name):
    with open(os.path.join(Path(__file__).parent.absolute(), file_name)) as f:
        return f.readline().strip('\n')
