from enum import Enum
from matplotlib import pyplot as plt
import numpy as np

symbol = {'#': 0, '.': 1, 'E': 2, 'G': 3}


class Fighter(object):

    def __init__(self, team, position):
        self.team = team
        self.position = position
        self.hitpoints = 200

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)

    def __lt__(self, other):
        assert self.position != other.position
        if self.position[0] == other.position[0]:
            return self.position[1] <= other.position[1]
        else:
            return self.position[0] <= other.position[0]

    def isenemy(self, other):
        return self.team != other.team

    def isadjacent(self, other):
        return (abs(self.position[0] - other.position[0]) +
                abs(self.position[1] - other-position[1])) == 1

    def open_squares(self, grid):
        ret = []
        for pos in [(self.position[0], self.position[1]+1), \
                    (self.position[0]-1, self.position[1]), \
                    (self.position[0]+1, self.position[1]), \
                    (self.position[0], self.position[1]-1)]
        if grid[pos] == symbol['.']:
            ret.append(pos)
        return ret

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


if __name__ == "__main__":
    battle, fighters= scan_area("input_test")
    for fighter in fighters:
        print(fighter)
    while(True):
        # New round 
        fighters.sort()
        fid = 0
        while(fid < len(fighters)):
            # New fighter
            fighter = fighters[fid]
            targets = [other for other in fighters if fighter.isenemy(other)]
            open_squares_by_target = []
            for target in targets: 
                open_squares_by_target.extend(target.open_squares(grid))
            adjacents = [target for target in targets if fighter.isadjacent(other)]
            if not adjacents:
                if open_squares_by_target: 
                    #move 
            if adjacents: 
                # attack
            fid += 1
        break
    #plt.imshow(battle)
    #plt.show()
