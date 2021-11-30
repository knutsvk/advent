from matplotlib import pyplot as plt
import numpy as np


class Point(object):
    def __init__(self, position, velocity):
        self.position = position
        self.velocity = velocity

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)

    def future_position(self, time):
        x = self.position[0] + time * self.velocity[0]
        y = self.position[1] + time * self.velocity[1]
        return [x, y]


# End of class Point


def compute_entropy(points):
    centre = np.mean(points, axis=0)
    return np.linalg.norm(points - centre)


def get_input():
    """
    position=< 8, -2> velocity=< 0,  1>
    position=<15,  0> velocity=<-2,  0>
    """
    points = []
    with open("input") as inputfile:
        for line in inputfile:
            line = line.replace("position", "")
            line = line.replace("velocity", "")
            line = line.replace("<", "")
            line = line.replace(">", "")
            line = line.replace("=", "")
            line = line.replace(",", " ")
            line = line.split()
            x = int(line[0])
            y = int(line[1])
            u = int(line[2])
            v = int(line[3])
            points.append(Point([x, y], [u, v]))
    return points


if __name__ == "__main__":
    points = get_input()
    positions = np.zeros((len(points), 2), dtype=int)
    time = 0
    old_entropy = 1.0e40
    while True:
        for p, point in enumerate(points):
            positions[p] = point.future_position(time)
        new_entropy = compute_entropy(positions)
        if new_entropy > old_entropy:
            time -= 1
            for p, point in enumerate(points):
                positions[p] = point.future_position(time)
            print(time, new_entropy)
            plt.close("all")
            plt.scatter(positions[:, 0], positions[:, 1])
            plt.gca().invert_yaxis()
            plt.show()
            break
        else:
            time += 1
            old_entropy = new_entropy
        if time % 1000 == 0:
            print(time, new_entropy)
