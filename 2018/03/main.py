import numpy as np


def cleanup(input_data):
    output_data = np.zeros((len(input_data), 5), dtype=int)
    for i, line in enumerate(input_data):
        elfid = int(line[0].replace('#', ''))
        left, top = [int(x) for x in line[2].replace(',', ' ').replace(':', '').split()]
        width, height = [int(x) for x in line[3].replace('x', ' ').split()]
        output_data[i,0] = elfid
        output_data[i,1] = left
        output_data[i,2] = top
        output_data[i,3] = width
        output_data[i,4] = height
    return output_data


def overlapping_area(input_data):
    maxwidth = (input_data[:,1] + input_data[:,3]).max()
    maxheight = (input_data[:,2] + input_data[:,4]).max()
    grid = np.zeros((maxheight+1, maxwidth+1, 2), dtype=int)
    ok_elf = np.ones(len(input_data), dtype=bool)
    for elf in input_data:
        for i in range(elf[1], elf[1] + elf[3]):
            for j in range(elf[2], elf[2] + elf[4]):
                if grid[i,j,0] == 0:
                    # we are the first patch here
                    grid[i,j,0] = -1
                    grid[i,j,1] = elf[0]
                else:
                    # there is already somebody here
                    ok_elf[elf[0]-1] = False
                    ok_elf[grid[i,j,1]-1] = False
                    if grid[i,j,0] == -1:
                        grid[i,j,0] = 1
    for i, elf in enumerate(ok_elf): 
        if elf == True:
            nonoverlapping_id = i + 1
    return (grid[:,:,0] > 0).sum(), nonoverlapping_id


if __name__ == "__main__":
    data = np.genfromtxt("input", dtype=str, comments=None, deletechars=":#")
    data = cleanup(data)
    print(overlapping_area(data))
