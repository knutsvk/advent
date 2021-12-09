import numpy as np


def get_data(filename):
    with open(filename) as file:
        return np.array([[int(c) for c in line.strip()] for line in file])


def process(data):
    basins = []
    for i in range(data.shape[0]):
        for j in range(data.shape[1]):
            if not (
                (i > 0 and data[i - 1, j] <= data[i, j])
                or (i < data.shape[0] - 1 and data[i + 1, j] <= data[i, j])
                or (j > 0 and data[i, j - 1] <= data[i, j])
                or (j < data.shape[1] - 1 and data[i, j + 1] <= data[i, j])
            ):
                basins.append([(i, j)])
    task1 = sum([data[basin[0]] for basin in basins]) + len(basins)
    for basin in basins:
        for (i, j) in basin:
            if i > 0 and data[i, j] <= data[i - 1, j] < 9 and (i - 1, j) not in basin:
                basin.append((i - 1, j))
            if i < data.shape[0] - 1 and data[i, j] <= data[i + 1, j] < 9 and (i + 1, j) not in basin:
                basin.append((i + 1, j))
            if j > 0 and data[i, j] <= data[i, j - 1] < 9 and (i, j - 1) not in basin:
                basin.append((i, j - 1))
            if j < data.shape[1] - 1 and data[i, j] <= data[i, j + 1] < 9 and (i, j + 1) not in basin:
                basin.append((i, j + 1))
    sizes = sorted([len(basin) for basin in basins])
    task2 = sizes[-3] * sizes[-2] * sizes[-1]
    return task1, task2


example_data = get_data("example9")
input_data = get_data("input9")

print(process(example_data))
print(process(input_data))
