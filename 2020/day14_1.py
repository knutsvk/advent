import numpy as np


memory = {}
mask = np.zeros(36, dtype=bool)
bitmask = np.zeros(36, dtype=int)
with open("input14") as file:
    instructions = file.read().splitlines()
for instruction in instructions:
    if instruction[:4] == "mask":
        new_mask = instruction.split('= ')[1]
        for i, char in enumerate(new_mask):
            if char == 'X':
                mask[i] = False
            else:
                mask[i] = True
                bitmask[i] = int(char)
    else:
        value = np.zeros(36, dtype=int)
        pos = int(instruction.split('[')[1].split(']')[0])
        val = bin(int(instruction.split('= ')[1]))[2:]
        for i, bit in enumerate(val):
            value[36-len(val)+i] = bit
        value[mask] = bitmask[mask]
        memory[pos] = int("".join([str(x) for x in value]), 2)
print(sum(val for val in memory.values()))

