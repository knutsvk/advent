import numpy as np

if __name__ == "__main__":
    data = list(np.loadtxt("input1", dtype=int))
    n = len(data)
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j + 1, n):
                if data[i] + data[j] + data[k] == 2020:
                    print(data[i] * data[j] * data[k])
