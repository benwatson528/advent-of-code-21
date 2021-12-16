def solve(h) -> int:
    b = convert_to_binary(h)
    literals = []
    parse_packet(b, 0, literals)
    return sum(literals)


def parse_packet(b, start_idx, literals):
    packet_version = int(b[start_idx:start_idx + 3], 2)
    type_id = int(b[start_idx + 3:start_idx + 6], 2)
    if type_id == 4:
        return process_id_4(b, start_idx + 6, literals)
    else:
        return process_operator(b, start_idx + 6, literals)


def process_id_4(b, start_idx, literals):
    groups = []
    for i in range(start_idx, len(b), 5):
        groups.extend(b[i + 1:i + 5])
        if b[i] == '0':
            literals.append(int(''.join(groups), 2))
            return i + 5 + 3  # 3 0's after


def process_operator(b, start_idx, literals):
    length_type_id = b[start_idx]
    if length_type_id == '0':
        total_subpackets_length = int(''.join(b[start_idx + 1:start_idx + 15 + 1]), 2)
        idx = start_idx + 1 + 15 # This is where we start
        while idx < start_idx + 1 + 15 + total_subpackets_length:
            idx = parse_packet(b, idx, literals)
        return idx
    else:
        num_subpackets = int(''.join(b[start_idx + 1:start_idx + 11 + 1]), 2)
        for _ in range(num_subpackets):
            idx = parse_packet(b, start_idx + 1 + idx, literals)
    return idx


def convert_to_binary(h):
    return h.replace('0', '0000') \
        .replace('1', '0001') \
        .replace('2', '0010') \
        .replace('3', '0011') \
        .replace('4', '0100') \
        .replace('5', '0101') \
        .replace('6', '0110') \
        .replace('7', '0111') \
        .replace('8', '1000') \
        .replace('9', '1001') \
        .replace('A', '1010') \
        .replace('B', '1011') \
        .replace('C', '1100') \
        .replace('D', '1101') \
        .replace('E', '1110') \
        .replace('F', '1111')
