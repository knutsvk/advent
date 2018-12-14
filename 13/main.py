from enum import Enum
import numpy as np
import sys


class Direction(Enum):
    UP = 0
    LEFT = 1
    DOWN = 2
    RIGHT = 3
    STRAIGHT = 4


dirsyms = {Direction.UP: '^', Direction.LEFT: '<', Direction.DOWN: 'v', Direction.RIGHT: '>'}


class Cart(object):
    def __init__(self, position, direction):
        self.position = position
        self.direction = direction
        if (self.direction == Direction.UP) or (self.direction == Direction.DOWN):
            self.covering = '|'
        elif (self.direction == Direction.LEFT) or (self.direction == Direction.RIGHT):
            self.covering = '-'
        else:
            print("WWAAAA")
            exit(1)
        self.last_turn = Direction.RIGHT


    def __lt__(self, other):
        assert self.position != other.position
        if self.position[0] == other.position[0]:
            return self.position[1] < other.position[1]
        else:
            return self.position[0] < other.position[0]

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)

    def move(self, grid, carts):
        # Return old position to normal
        old_pos = self.position
        old_sym = self.covering
        grid[old_pos] = old_sym

        new_pos = list(old_pos)
        # Find out what new position is 
        if self.direction == Direction.UP:
            new_pos[0] -= 1
        elif self.direction == Direction.DOWN: 
            new_pos[0] += 1
        elif self.direction == Direction.LEFT: 
            new_pos[1] -= 1
        elif self.direction == Direction.RIGHT: 
            new_pos[1] += 1
        self.position = tuple(new_pos)

        # What did we move to?
        self.covering = grid[self.position]
        if self.covering in ['^', '<', 'v', '>']: 
            # CRASH
            for cart in carts:
                if (cart.position == self.position) & (cart.direction != self.direction):
                    grid[self.position] = cart.covering
                    carts.remove(cart)
                    break
            return True
        elif self.covering == '\\':
            # Corner
            if self.direction == Direction.UP:
                self.direction = Direction.LEFT
            elif self.direction == Direction.LEFT: 
                self.direction = Direction.UP
            elif self.direction == Direction.DOWN: 
                self.direction = Direction.RIGHT
            elif self.direction == Direction.RIGHT: 
                self.direction = Direction.DOWN
        elif self.covering == '/':
            # Corner
            if self.direction == Direction.UP:
                self.direction = Direction.RIGHT
            elif self.direction == Direction.LEFT: 
                self.direction = Direction.DOWN
            elif self.direction == Direction.DOWN: 
                self.direction = Direction.LEFT
            elif self.direction == Direction.RIGHT: 
                self.direction = Direction.UP
        elif self.covering == '+':
            # Junction
            if self.last_turn == Direction.RIGHT: 
                self.last_turn = Direction.LEFT
                if self.direction == Direction.RIGHT: 
                    self.direction = Direction.UP
                else:
                    self.direction = Direction(self.direction.value + 1)
            elif self.last_turn == Direction.LEFT:
                self.last_turn = Direction.STRAIGHT
            elif self.last_turn == Direction.STRAIGHT: 
                self.last_turn = Direction.RIGHT
                if self.direction == Direction.UP:
                    self.direction = Direction.RIGHT
                else:
                    self.direction = Direction(self.direction.value - 1)

        # Place self on grid
        grid[self.position] = dirsyms[self.direction]



def get_input():
    with open("input_test2") as inputfile: 
        rows = 0
        cols = 0
        for line in inputfile: 
            rows += 1
            cols = max(cols, len(line))
    data = np.zeros((rows, cols-1), dtype=str)
    with open("input_test2") as inputfile:
        for i, line in enumerate(inputfile): 
            for j, char in enumerate(line): 
                if j == cols-1:
                    continue
                data[i,j] = char
    return data


def display(grid):
    sys.stdout.flush()
    for line in grid: 
        for char in line:
            print(char, end='')
        print()
    print()


def find_carts(grid):
    carts = []
    for (i, j), point in np.ndenumerate(grid):
        if point == '^':
            carts.append(Cart(position=(i,j), direction=Direction.UP))
        elif point == 'v': 
            carts.append(Cart(position=(i,j), direction=Direction.DOWN))
        elif point == '<': 
            carts.append(Cart(position=(i,j), direction=Direction.LEFT))
        elif point == '>': 
            carts.append(Cart(position=(i,j), direction=Direction.RIGHT))
    return carts


def find_crash(grid, carts):
    step = 1
    n = len(carts)
    while(n > 1 and step < 10):
        i = 0
        while(i < len(carts)):
            carts.sort()
            crash = carts[i].move(grid, carts)
            if(crash): 
                print("Crash! Removed two carts. ")
                carts.remove(carts[i])
            else: 
                i += 1
            display(grid)
        n = len(carts)
        print("After step ", step, ", ", n, " carts remaining")
        display(grid)
        step += 1
    return carts[0].position


if __name__ == "__main__":
    grid = get_input()
    carts = find_carts(grid)
    display(grid)
    print(find_crash(grid, carts))
