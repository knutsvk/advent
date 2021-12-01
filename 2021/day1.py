import numpy as np

if __name__ == "__main__":
    depths = np.loadtxt("input1")
    diffs = depths[1:] - depths[:-1]
    print(sum(diffs > 0))
    windows = depths[:-2] + depths[1:-1] + depths[2:]
    diffs = windows[1:] - windows[:-1]
    print(sum(diffs > 0))
