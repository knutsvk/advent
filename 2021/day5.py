import numpy as np

with open("input5") as f:
    lines = [[int(x) for p in line.strip().split("->") for x in p.strip().split(",")] for line in f]


def count_points_with_at_least_two_overlaps(count_diagonals: bool) -> int:
    n = np.max(lines) + 1
    arr = np.zeros((n, n), dtype=int)
    for line in lines:
        if line[0] == line[2]:
            beg = min(line[1], line[3])
            end = max(line[1], line[3]) + 1
            arr[beg:end, line[0]] += 1
        elif line[1] == line[3]:
            beg = min(line[0], line[2])
            end = max(line[0], line[2]) + 1
            arr[line[1], beg:end] += 1
        elif count_diagonals:
            sign_x = 1 if line[2] > line[0] else -1
            sign_y = 1 if line[3] > line[1] else -1
            for i in range(abs(line[2] - line[0]) + 1):
                arr[line[1] + i * sign_y, line[0] + i * sign_x] += 1
    return (arr > 1).sum()


print([count_points_with_at_least_two_overlaps(count_diagonals) for count_diagonals in [False, True]])
