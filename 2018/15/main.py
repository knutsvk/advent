from enum import Enum
from matplotlib import pyplot as plt
import numpy as np
import sys

symbol = {'#': 0, '.': 1, 'E': 2, 'G': 3}


class Fighter(object):

    def __init__(self, team, position):
        self.team = team
        self.position = position
        self.hitpoints = 200

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)

    def __lt__(self, other):
        return self.position < other.position

    def isenemy(self, other):
        return self.team != other.team

    def isadjacent(self, other):
        return (abs(self.position[0] - other.position[0]) +
                abs(self.position[1] - other.position[1])) == 1

# End of class Fighter


def scan_area(filename):
    fighters = []
    with open(filename) as openfile: 
        rows = 0
        cols = 0
        for line in openfile:
            rows += 1
            cols = len(line)
    battle = np.zeros((rows, cols-1), dtype=int)
    with open(filename) as openfile:
        for i, line in enumerate(openfile): 
            for j, char in enumerate(line): 
                if j == cols-1:
                    continue
                if char in ['E', 'G']:
                    fighters.append(Fighter(char, (i,j)))
                battle[i,j] = symbol[char]
    return battle, fighters


def opensquares(position, battle):
    neighbours = [(position[0] , position[1]+1),\
                  (position[0]-1, position[1]  ),\
                  (position[0]+1, position[1]  ),\
                  (position[0]  , position[1]-1)] 
    return [pos for pos in neighbours if battle[pos] == symbol['.']]


def findpaths(paths, end, battle, nearest):
    if len(paths[0]) > nearest:
        return []
    check_further = []
    keepers = []
    pathid = 0
    for path in paths:
        possible_moves = opensquares(path[-1], battle)
        for new_square in possible_moves: 
            if new_square in path: 
                continue
            else:
                new_path = path + [new_square]
                if new_square == end:
                    keepers.append(new_path)
                else:
                    check_further.append(new_path)
    if keepers: 
        return keepers
    elif check_further:
        return findpaths(check_further, end, battle, nearest)
    else: 
        return []


if __name__ == "__main__":
    # Read input, get initial battle map and list of fighters
    battle, fighters= scan_area("input_test5")

    # Commence battle!
    somebody_has_won = False
    round = 0
    while(not somebody_has_won):
        # New round 
        fighters.sort()
        fid = 0

        print("After round %d: " % round)
        print(battle)
        for fighter in fighters:
            print(fighter)
        print()

        while(fid < len(fighters)):
            # New fighter
            fighter = fighters[fid]

            # Find enemies 
            targets = [other for other in fighters if fighter.isenemy(other)]
            if not targets:
                somebody_has_won = True
                break

            # Check which (if any) enemies which are adjacent to fighter
            adjacents = [target for target in targets if fighter.isadjacent(target)]

            if not adjacents:
                # Try to move to an enemy

                # Find open squares next to targets
                target_squares = []
                for target in targets: 
                    target_squares.extend(opensquares(target.position, battle))

                if target_squares: 
                    # Find nearest reachable paths 
                    paths = []
                    nearest = sum(battle.shape)-2
                    for square in target_squares:
                        paths.extend(findpaths([[fighter.position]], square, battle, nearest))
                        if paths:
                            nearest = min(nearest, len(paths[-1]))
                    paths = [path[1:] for path in paths if len(path) == nearest]
                    if paths:
                        # What is the nearest reachable goal? 
                        goal = min([path[-1] for path in paths])
                        paths = [path for path in paths if path[-1] == goal]

                        # Find where to move to
                        moveto = min([path[0] for path in paths])

                        # Move!
                        battle[fighter.position] = symbol['.']
                        fighter.position = moveto
                        battle[moveto] = symbol[fighter.team]

            # Check which (if any) enemies which are adjacent to fighter
            adjacents = [target for target in targets if fighter.isadjacent(target)]

            if adjacents: 
                weakest = adjacents[0]
                for enemy in adjacents: 
                    if enemy.hitpoints < weakest.hitpoints: 
                        weakest = enemy
                weakest.hitpoints -= 3
                if weakest.hitpoints <= 0:
                    battle[weakest.position] = symbol['.']
                    if fighters.index(weakest) < fid + 1:
                        fid -= 1
                    fighters.remove(weakest)

            fid += 1
        round += 1

    hpsum = sum([fighter.hitpoints for fighter in fighters])
    outcome = (round -1) * hpsum
    print("Task 1: %d * %d = %d" % (round - 1, hpsum, outcome))
    #plt.imshow(battle)
    #plt.show()
