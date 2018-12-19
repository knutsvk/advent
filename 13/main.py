import numpy as np
import sys


DIRSYMS  = ['^', '<', 'v', '>']


class State(object):
    def __init__(self, grid, carts):
        self.grid = grid
        self.carts = carts


    def __str__(self):
        # Add cart symbol to grid before printing
        backup_symbols = [''] * len(carts)
        for c, cart in enumerate(self.carts):
            backup_symbols[c] = self.grid[tuple(cart.position)]
            self.grid[tuple(cart.position)] = cart.direction

        ret = ""
        for l, line in enumerate(self.grid): 
            for c, char in enumerate(line):
                ret += char
            ret += "\n"
        ret += "\n"

        # Remove cart symbols from grid again
        for c, cart in enumerate(self.carts):
            self.grid[tuple(cart.position)] = backup_symbols[c]
        return ret


    def move(self, cart_index):
        cart = self.carts[cart_index]
        new_pos = cart.position[:]
        # Find out what new position is 
        if cart.direction == '^':
            new_pos[0] -= 1
        elif cart.direction == 'v':
            new_pos[0] += 1
        elif cart.direction == '<':
            new_pos[1] -= 1
        elif cart.direction == '>':
            new_pos[1] += 1

        # Was there already a different cart there? 
        for other_cart in self.carts:
            if other_cart.position == new_pos:
                # CRASH
                neighbours_in_array = cart_index - carts.index(other_cart) == 1
                carts.remove(other_cart)
                carts.remove(cart)
                return [new_pos, neighbours_in_array]

        cart.position = new_pos

        # What did we move to?
        covering = self.grid[tuple(cart.position)]
        if covering == '\\':
            # Corner
            if cart.direction == '^':
                cart.direction = '<'
            elif cart.direction == '<':
                cart.direction = '^'
            elif cart.direction == 'v':
                cart.direction = '>'
            elif cart.direction == '>':
                cart.direction = 'v'
        elif covering == '/':
            # Corner
            if cart.direction == '^':
                cart.direction = '>'
            elif cart.direction == '<': 
                cart.direction = 'v'
            elif cart.direction == 'v': 
                cart.direction = '<'
            elif cart.direction == '>': 
                cart.direction = '^'
        elif covering == '+':
            # Junction
            if cart.last_turn == '>': 
                cart.last_turn = '<'
                if cart.direction == '>': 
                    cart.direction = '^'
                else:
                    cart.direction = DIRSYMS[DIRSYMS.index(cart.direction) + 1]
            elif cart.last_turn == '<':
                cart.last_turn = '|'
            elif cart.last_turn == '|':
                cart.last_turn = '>'
                if cart.direction == '^':
                    cart.direction = '>'
                else:
                    cart.direction = DIRSYMS[DIRSYMS.index(cart.direction) - 1]
        return [[], False]


    def simulate(self, animate=False):
        step = 1
        n = len(self.carts)
        while(n > 1):
            i = 0
            self.carts.sort()
            while(i < len(self.carts)):
                crash, neighbours = state.move(i)
                if(crash): 
                    print("Crash at (%d,%d)" % tuple(crash))
                    if neighbours: 
                        i -= 1
                else: 
                    i += 1
            if(animate):
                print(state)
            n = len(carts)
            step += 1
        if n == 1:
            return self.carts[0].position

# End of class State


class Cart(object):
    def __init__(self, position, direction):
        self.position = position
        self.direction = direction
        self.last_turn = '>'


    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)


    def __lt__(self, other):
        assert self.position != other.position
        if self.position[0] == other.position[0]:
            return self.position[1] <= other.position[1]
        else:
            return self.position[0] <= other.position[0]

# End of class Cart


def get_input():
    with open("input") as input_test3file: 
        rows = 0
        cols = 0
        for line in input_test3file: 
            rows += 1
            cols = max(cols, len(line))
    data = np.zeros((rows, cols-1), dtype=str)
    with open("input") as input_test3file:
        for i, line in enumerate(input_test3file): 
            for j, char in enumerate(line): 
                if j == cols-1:
                    continue
                data[i,j] = char
    return data


def find_carts(grid):
    carts = []
    for (i, j), point in np.ndenumerate(grid):
        if point in DIRSYMS:
            carts.append(Cart(position=[i,j], direction=point))
            if point in ['v', '^']:
                grid[i,j] = '|'
            else:
                grid[i,j] = '-'
    return carts


if __name__ == "__main__":
    animate = False
    grid = get_input()
    carts = find_carts(grid)
    state = State(grid, carts)
    if(animate): 
        print(state)
    print(state.simulate(animate))
