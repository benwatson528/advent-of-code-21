import math


def solve(h) -> (int, int):
    b = (bin(int(h, 16))[2:]).zfill(len(h) * 4)
    filled_b = b.zfill(len(b) + len(b) % 4)
    packet_versions = []
    _, ans = parse_packet(filled_b, 0, packet_versions)
    return sum(packet_versions), ans


def parse_packet(b, start_idx, packet_versions):
    packet_versions.append(int(b[start_idx:start_idx + 3], 2))
    type_id = int(b[start_idx + 3:start_idx + 6], 2)
    if type_id == 4:
        return process_id_4(b, start_idx + 6)
    else:
        return process_operator(b, start_idx + 6, packet_versions, type_id)


def process_id_4(b, start_idx):
    groups = []
    for i in range(start_idx, len(b), 5):
        groups.extend(b[i + 1:i + 5])
        if b[i] == '0':
            number = int(''.join(groups), 2)
            return i + 5, number


def process_operator(b, start_idx, packet_versions, type_id):
    length_type_id = b[start_idx]
    expression_args = []
    if length_type_id == '0':
        total_subpackets_length = int(''.join(b[start_idx + 1:start_idx + 15 + 1]), 2)
        idx = start_idx + 1 + 15
        while idx < start_idx + 1 + 15 + total_subpackets_length:
            idx, num = parse_packet(b, idx, packet_versions)
            expression_args.append(num)
    else:
        num_subpackets = int(''.join(b[start_idx + 1:start_idx + 11 + 1]), 2)
        idx = start_idx + 1 + 11
        for _ in range(num_subpackets):
            idx, num = parse_packet(b, idx, packet_versions)
            expression_args.append(num)

    return idx, evaluate_expression(expression_args, type_id)


def evaluate_expression(expression_args, type_id):
    if type_id == 0:
        return sum(expression_args)
    elif type_id == 1:
        return math.prod(expression_args)
    elif type_id == 2:
        return min(expression_args)
    elif type_id == 3:
        return max(expression_args)
    elif type_id == 5:
        return 1 if expression_args[0] > expression_args[1] else 0
    elif type_id == 6:
        return 1 if expression_args[0] < expression_args[1] else 0
    elif type_id == 7:
        return 1 if expression_args[0] == expression_args[1] else 0
    else:
        return 0
