import numpy as np


def get_wire(path):
    wire = [(0, 0, 0)]
    wire_length = 0
    for instruction in path:
        x_last = wire[-1][0]
        y_last = wire[-1][1]
        direction = instruction[0]
        distance = int(instruction[1:])
        wire_length += distance
        if direction == "R":
            wire.append((x_last + distance, y_last, wire_length))
        elif direction == "L":
            wire.append((x_last - distance, y_last, wire_length))
        elif direction == "U":
            wire.append((x_last, y_last + distance, wire_length))
        elif direction == "D":
            wire.append((x_last, y_last - distance, wire_length))
    return wire


def manhattan_intersection(segment1, segment2):
    x1, y1, l1 = segment1[0]
    x2, y2, _ = segment1[1]
    x3, y3, l3 = segment2[0]
    x4, y4, _ = segment2[1]
    if x1 == x2 and y3 == y4:  # segment 1 vertical, segment 2 horizontal
        if min(x3, x4) <= x1 <= max(x3, x4) and min(y1, y2) <= y3 <= max(y1, y2):
            return l3 + x1 - min(x3, 4) + l1 + y3 - min(y1, y2)
    if y1 == y2 and x3 == x4:  # segment 1 horizontal, segment 2 vertical
        if min(x1, x2) <= x3 <= max(x1, x2) and min(y3, y4) <= y1 <= max(y3, y4):
            return l1 + x3 - min(x1, x2) + l3 + y1 - min(y3, y4)
    return 2e200


path1, path2 = np.loadtxt("input3", dtype=str, delimiter=",")
wire1 = get_wire(path1)
wire2 = get_wire(path2)

minimum_signal_delay = 1e200
for segment1 in zip(wire1[:-1], wire1[1:]):
    for segment2 in zip(wire2[:-1], wire2[1:]):
        minimum_signal_delay = min(minimum_signal_delay, manhattan_intersection(segment1, segment2))
print(minimum_signal_delay)
