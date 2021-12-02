import numpy as np

if __name__ == "__main__":
    nx = 8
    nl = 7
    x = np.zeros((1 + 2 * nl, 1 + 2 * nl, nx + 2 * nl, nx + 2 * nl), dtype=int)
    with open("input17") as f:
        for i, l in enumerate(f):
            for j, c in enumerate(l):
                if c == "#":
                    x[nl, nl, i + nl, j + nl] = 1

    for l in range(nl):
        print(f"{l}: {x.sum()}")
        y = x.copy()
        for i in range(x.shape[0]):
            for j in range(x.shape[1]):
                for k in range(x.shape[2]):
                    for w in range(x.shape[3]):
                        n = y[i - 1 : i + 2, j - 1 : j + 2, k - 1 : k + 2, w - 1 : w + 2].sum() - y[i, j, k, w]
                        if y[i, j, k, w]:
                            if n not in [2, 3]:
                                x[i, j, k, w] = 0
                        else:
                            if n == 3:
                                x[i, j, k, w] = 1
    print(f"{nl}: {x.sum()}")
