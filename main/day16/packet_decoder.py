def solve(h) -> int:
    b = (bin(int(h, 16))[2:]).zfill(len(h) * 4)
    filled_b = b.zfill(len(b) + len(b) % 4)
    packet_versions = []
    parse_packet(filled_b, 0, packet_versions)
    return sum(packet_versions)


def parse_packet(b, start_idx, packet_versions):
    start = b[start_idx:]
    print(f"start = {start}")
    packet_versions.append(int(b[start_idx:start_idx + 3], 2))
    type_id = int(b[start_idx + 3:start_idx + 6], 2)
    if type_id == 4:
        return process_id_4(b, start_idx + 6)
    else:
        return process_operator(b, start_idx + 6, packet_versions)


def process_id_4(b, start_idx):
    groups = []
    for i in range(start_idx, len(b), 5):
        groups.extend(b[i + 1:i + 5])
        if b[i] == '0':
            number = int(''.join(groups), 2)
            print(f"number = {number}")
            return i + 5


def process_operator(b, start_idx, packet_versions):
    length_type_id = b[start_idx]
    if length_type_id == '0':
        total_subpackets_length = int(''.join(b[start_idx + 1:start_idx + 15 + 1]), 2)
        idx = start_idx + 1 + 15
        while idx < start_idx + 1 + 15 + total_subpackets_length:
            idx = parse_packet(b, idx, packet_versions)
        return idx
    else:
        num_subpackets = int(''.join(b[start_idx + 1:start_idx + 11 + 1]), 2)
        idx = start_idx + 1 + 11
        for _ in range(num_subpackets):
            idx = parse_packet(b, idx, packet_versions)
        return idx
