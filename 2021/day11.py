import numpy as np


def get_data(filename):
    with open(filename) as file:
        return np.array([[int(c) for c in line.strip()] for line in file])


def process(data):
    flashes = 0
    step = 0
    while True:
        data += 1
        something_changed = True
        while something_changed:
            something_changed = False
            tmp = data.copy()
            for i in range(data.shape[0]):
                for j in range(data.shape[1]):
                    if 9 < tmp[i, j] < 20:
                        xmin = max(i - 1, 0)
                        xmax = min(i + 2, data.shape[0] + 1)
                        ymin = max(j - 1, 0)
                        ymax = min(j + 2, data.shape[1] + 1)
                        data[xmin:xmax, ymin:ymax] += 1
                        data[i, j] = 20
                        something_changed = True
        for i in range(data.shape[0]):
            for j in range(data.shape[1]):
                if data[i, j] > 10:
                    flashes += 1
                    data[i, j] = 0
        step += 1
        if step == 100:
            print(flashes)
        if np.count_nonzero(data) == 0:
            return step


example_data = get_data("example11")
input_data = get_data("input11")

print(process(example_data))
print(process(input_data))
