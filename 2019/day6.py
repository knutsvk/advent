from anytree import Node, RenderTree
import numpy as np


def find_children(parent, data):
    result = {}
    for orbit in data: 
        orbitee = orbit.partition(")")[0]
        orbiter = orbit.partition(")")[2]
        if orbitee == parent: 
             result[orbiter] = find_children(orbiter, data)
    return result


def count_orbits(tree, depth):
    result = 0
    for _, val in tree.items(): 
        result += depth
        result += count_orbits(val, depth+1)
    return result


def search(tree, person):
    for key, val in tree.items():
        if key == person:
            return [key]
        else: 
            tmp = search(val, person)
            if tmp: 
                return [key] + tmp
    return []


if __name__ == "__main__":
    data = list(np.loadtxt("input6", dtype=str))
    tree = {"COM": find_children("COM", data)}
    print("task 1: %d" % count_orbits(tree, 0))

    knut = search(tree, "YOU")
    nick = search(tree, "SAN")
    same_path = [x for (x, y) in zip(knut, nick) if x == y]
    print("task 2: %d" % (len(knut) + len(nick) - 2 * (len(same_path) + 1)))

