import numpy as np


def get_data(filename):
    with open(filename) as file:
        lines = file.read().splitlines()
        data = np.nan * np.ones((len(lines), len(lines[0])))
        for i, row in enumerate(lines):
            for j, col in enumerate(row):
                if col == "L":
                    data[i, j] = 0
        return data


def task1():
    data = get_data("input11")
    sums = np.zeros_like(data)
    something_changed = True
    while something_changed:
        something_changed = False
        for i, row in enumerate(data):
            for j, col in enumerate(row):
                if not np.isnan(col):
                    row_start = i if i == 0 else i - 1
                    row_end = i + 1 if i == len(data) else i + 2
                    col_start = j if j == 0 else j - 1
                    col_end = j + 1 if j == len(row) else j + 2
                    sums[i, j] = (
                        np.sum(np.nan_to_num(data[row_start:row_end, col_start:col_end], copy=True)) - data[i, j]
                    )
        for i, row in enumerate(data):
            for j, col in enumerate(row):
                if not np.isnan(col):
                    if data[i, j] == 0 and sums[i, j] == 0:
                        data[i, j] = 1
                        something_changed = True
                    elif data[i, j] == 1 and sums[i, j] >= 4:
                        data[i, j] = 0
                        something_changed = True
    print(np.sum(np.nan_to_num(data, copy=True)))


def task2():
    data = get_data("input11")
    visible = np.zeros_like(data)
    something_changed = True
    while something_changed:
        something_changed = False
        for i, row in enumerate(data):
            for j, col in enumerate(row):
                if not np.isnan(col):
                    north = next((x for x in data[:i, j][::-1] if not np.isnan(x)), 0)
                    nedim = min(data[:i, j + 1 :].shape)
                    north_east = next(
                        (
                            x
                            for x in np.fliplr(data[i - nedim : i, j + 1 : j + 1 + nedim]).diagonal()[::-1]
                            if not np.isnan(x)
                        ),
                        0,
                    )
                    east = next((x for x in data[i, j + 1 :] if not np.isnan(x)), 0)
                    sedim = min(data[i + 1 :, j + 1 :].shape)
                    south_east = next(
                        (x for x in data[i + 1 : i + 1 + sedim, j + 1 : j + 1 + sedim].diagonal() if not np.isnan(x)),
                        0,
                    )
                    south = next((x for x in data[i + 1 :, j] if not np.isnan(x)), 0)
                    swdim = min(data[i + 1 :, :j].shape)
                    south_west = next(
                        (
                            x
                            for x in np.fliplr(data[i + 1 : i + 1 + swdim, j - swdim : j]).diagonal()
                            if not np.isnan(x)
                        ),
                        0,
                    )
                    west = next((x for x in data[i, :j][::-1] if not np.isnan(x)), 0)
                    nwdim = min(data[:i, :j].shape)
                    north_west = next(
                        (x for x in data[i - nwdim : i, j - nwdim : j].diagonal()[::-1] if not np.isnan(x)),
                        0,
                    )
                    visible[i, j] = north + north_east + east + south_east + south + south_west + west + north_west
        for i, row in enumerate(data):
            for j, col in enumerate(row):
                if not np.isnan(col):
                    if data[i, j] == 0 and visible[i, j] == 0:
                        data[i, j] = 1
                        something_changed = True
                    elif data[i, j] == 1 and visible[i, j] >= 5:
                        data[i, j] = 0
                        something_changed = True
    print(np.sum(np.nan_to_num(data, copy=True)))


if __name__ == "__main__":
    task1()
    task2()
