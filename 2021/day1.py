import numpy as np

if __name__ == "__main__":
    d = np.loadtxt("input1")
    print(sum(d[1:] > d[:-1]), sum(d[3:] > d[:-3]))
