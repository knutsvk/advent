from matplotlib import pyplot as plt
import numpy as np
from scipy.sparse import coo_matrix


def process(filename):
    points = set()
    folds = []
    with open(filename) as file:
        for line in file:
            if line[0].isdigit():
                points.add(tuple(int(c) for c in line.strip().split(",")))
            elif line.startswith("fold"):
                folds.append((line.split("=")[0][-1], int(line.split("=")[1])))
    for i, fold in enumerate(folds):
        old_points = set()
        new_points = set()
        for point in points:
            if fold[0] == "x" and point[0] > fold[1]:
                new_points.add((fold[1] * 2 - point[0], point[1]))
                old_points.add(point)
            if fold[0] == "y" and point[1] > fold[1]:
                new_points.add((point[0], fold[1] * 2 - point[1]))
                old_points.add(point)
        for old, new in zip(old_points, new_points):
            points.add(new)
            points.remove(old)
        if i == 0:
            print(len(points))
    plt.spy(coo_matrix((np.ones(len(points)), ([p[1] for p in points], [p[0] for p in points]))))
    plt.show()


process("input13")
