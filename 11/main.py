import numpy as np


if __name__ == "__main__":
    serialnumber = 5235
    grid = np.zeros((300, 300))
    X, Y = np.meshgrid(np.arange(300)+1, np.arange(300)+1)
    grid = ((X + 10) * Y + serialnumber) * (X + 10)
    stringrid = grid.astype(str)
    for i in range(300):
        for j in range(300):
            grid[i,j] = int(stringrid[i,j][-3]) - 5
    best = [(0,0), 1, -100000]
    for k in range(1, 301):
        print("k = %d" % k)
        for i in range(300-k+1):
            for j in range(300-k+1):
                square = grid[i:i+k,j:j+k].sum()
                if square > best[2]:
                    best[0] = (j+1,i+1)
                    best[1] = k
                    best[2] = square
    print(best)
