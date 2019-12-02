import numpy as np


def compute(array):
    pos = 0
    n = len(array)
    while array[pos] != 99:
        if array[pos] == 1:
            array[array[pos+3]] = array[array[pos+1]] + array[array[pos+2]]
        elif array[pos] == 2:
            array[array[pos+3]] = array[array[pos+1]] * array[array[pos+2]]
        pos += 4
    return array


if __name__ == "__main__":
    data = np.loadtxt("input", dtype=int, delimiter=",")
    data[1] = 12
    data[2] = 2
    output = compute(data)
    print(output)
