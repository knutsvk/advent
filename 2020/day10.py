import numpy as np


def get_jolts(filename):
    with open(filename) as file:
        adapters = sorted([int(jolt) for jolt in file.read().splitlines()])
    return [0] + adapters + [max(adapters) + 3]


if __name__ == "__main__":
    jolts = get_jolts("input10")
    diffs = np.array([x-y for x,y in zip(jolts[1:], jolts[:-1])])
    print(sum(diffs == 1) * sum(diffs == 3))

    end_joltages = {0: 1}
    for i, jolt in enumerate(jolts[1:]):
        new_ends = 0
        for value, count in end_joltages.items():
            if jolt - value <= 3:
                new_ends += count
                continue
        end_joltages = {value: count for value, count in end_joltages.items() if jolt - value <= 3}
        end_joltages[jolt] = new_ends
    print(end_joltages[jolts[-1]])
