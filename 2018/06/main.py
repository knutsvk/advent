from matplotlib import pyplot as plt
import numpy as np


def manhattan_distance(i1, j1, i2, j2):
    return abs(i1 - i2) + abs(j1 - j2)


def fill_grid(grid, data):
    """
    Label each grid point with nearest place and distance to it, and sum of distances
    grid[i,j,0]: Manhattan distance to nearest place
    grid[i,j,1]: Identifier of nearest place
    grid[i,j,2]: Sum of distance to all points
    """
    for (i, j), val in np.ndenumerate(grid[:, :, 0]):
        shortest_distance = 10000
        total_distance = 0
        for key, (ip, jp) in enumerate(data):
            distance = manhattan_distance(i, j, ip, jp)
            if distance == shortest_distance:
                # Ambiguous
                nearest_point = -1
            elif distance < shortest_distance:
                nearest_point = key
                shortest_distance = distance
            total_distance += distance
        grid[i, j, 0] = shortest_distance
        grid[i, j, 1] = nearest_point
        grid[i, j, 2] = int(total_distance < 10000)
    return grid


def largest_area(grid, data):
    largest_area = 0
    for i in range(len(data)):
        my_area = grid[:, :, 1] == i
        if (
            my_area[0, :].any()
            or my_area[:, 0].any()
            or my_area[my_area.shape[0] - 1, :].any()
            or my_area[:, my_area.shape[1] - 1].any()
        ):
            continue
        else:
            if my_area.sum() > largest_area:
                largest_area = my_area.sum()
    return largest_area


if __name__ == "__main__":
    data = np.loadtxt("input", dtype=int, delimiter=",")
    data -= data.min(axis=0)

    grid = -np.ones((*data.max(axis=0) + 1, 3), dtype=int)
    for key, (i, j) in enumerate(data):
        grid[i, j, 0] = 0
        grid[i, j, 1] = key

    # Four subplots, unpack the axes array immediately
    plt.close("all")
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, sharey=True)

    # Plot the special points
    ax1.imshow(grid[:, :, 0].T)

    # Do the actual work
    fill_grid(grid, data)

    # Plot distance from nearest special point
    ax2.imshow(grid[:, :, 0].T)
    # Catchment area of each special point
    ax3.imshow(grid[:, :, 1].T)
    # Special points within total distance of all points
    ax4.imshow(grid[:, :, 2].T)
    plt.show()

    print(largest_area(grid, data), grid[:, :, 2].sum())
