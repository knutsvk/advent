with open("input6") as f:
    x = [int(x) for x in f.readline().split(",")]
    fish = {age: len([a for a in x if a == age]) for age in range(9)}

for d in range(256):
    if d == 80:
        print(sum(x for x in fish.values()))
    new_fish = {}
    for a in range(7, -1, -1):
        new_fish[a] = fish[a + 1]
    new_fish[8] = fish[0]
    new_fish[6] += fish[0]
    fish = new_fish
print(sum(x for x in fish.values()))
