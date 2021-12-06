with open("input6") as f:
    x = [int(c) for c in f.readline().split(",")]


def count_fish(n):
    fish = [len([a for a in x if a == age]) for age in range(9)]
    for d in range(n):
        fish.append(fish.pop(0))
        fish[6] += fish[8]
    return sum(fish)


print(count_fish(80), count_fish(256))
