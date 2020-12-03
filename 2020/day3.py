def check_slope(down, right):
    num_trees = 0
    with open("input3") as file:
        lines = file.read().splitlines()
    for row, line in enumerate(lines[::down]):
        col = (row * right) % len(line)
        if line[col] == '#':
            num_trees += 1
    return num_trees


def task1():
    print(check_slope(1, 3))


def task2():
    slopes = [(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)]
    ans = 1
    for slope in slopes:
        print(check_slope(slope[0], slope[1]))
        ans *= check_slope(slope[0], slope[1])
    print(ans)


if __name__ == "__main__":
    task1()
    task2()
