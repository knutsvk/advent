from math import ceil
import numpy as np


def get_data(filename):
    with open(filename) as f:
        data = [int(c) for c in f.readline().split(",")]
    return data


def process(data, f):
    sumf = lambda i: sum([f(x, i) for x in data])
    lowest = sumf(0)
    for i in range(1, max(data) + 1):
        new_sum = sumf(i)
        if new_sum > lowest:
            return lowest
        lowest = new_sum


example_data = get_data("example7")
input_data = get_data("input7")

print(process(example_data, lambda x, i: abs(x - i)))
print(process(input_data, lambda x, i: abs(x - i)))
print(process(example_data, lambda x, i: abs(x - i) * (abs(x - i) + 1) // 2))
print(process(input_data, lambda x, i: abs(x - i) * (abs(x - i) + 1) // 2))


def task1(data):
    return sum([abs(x - np.median(data).astype(int)) for x in data])


def task2(data):
    i = ceil(np.mean(data))
    return min([sum([abs(x - i + d) * (abs(x - i + d) + 1) // 2 for x in data]) for d in [0, 1]])


# print(task1(example_data))
# print(task1(input_data))
# print(task2(example_data))
# print(task2(input_data))
