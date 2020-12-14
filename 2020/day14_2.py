from copy import deepcopy
import numpy as np

def get_masks(instruction):
    mask = np.ones(36, dtype=bool)
    bitmasks = [['0'], ['1']] if instruction[0] == 'X' else [[instruction[0]]]
    if instruction[0] == '0':
        mask[0] = False
    for i, char in enumerate(instruction):
        if i == 0:
            continue
        if char == '0':
            mask[i] = False
            for bitmask in bitmasks:
                bitmask.append('0')
        elif char == '1':
            for bitmask in bitmasks:
                bitmask.append('1')
        else:
            bitmasks = bitmasks + deepcopy(bitmasks)
            for b, bitmask in enumerate(bitmasks):
                if b < len(bitmasks) // 2:
                    bitmask.append('0')
                else:
                    bitmask.append('1')
    return mask, [np.array(bitmask) for bitmask in bitmasks]



memory = {}
with open("input14") as file:
    instructions = file.read().splitlines()
for instruction in instructions:
    if instruction[:4] == "mask":
        mask, bitmasks = get_masks(instruction.split('= ')[1])
    else:
        address = np.zeros(36, dtype=int)
        pos = bin(int(instruction.split('[')[1].split(']')[0]))[2:]
        val = int(instruction.split('= ')[1])
        for i, bit in enumerate(pos):
            address[36-len(pos)+i] = bit
        for bitmask in bitmasks:
            address[mask] = bitmask[mask]
            memory[int("".join([str(x) for x in address]), 2)] = val
print(sum(val for val in memory.values()))

