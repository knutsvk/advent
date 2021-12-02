if __name__ == "__main__":
    pos = [0, 0, 0]
    with open("input2") as file:
        for i, l in enumerate(file):
            dir, n = l.split(" ")
            if dir == "down":
                pos[2] -= int(n)
            elif dir == "up":
                pos[2] += int(n)
            elif dir == "forward":
                pos[0] += int(n)
                pos[1] += int(n) * pos[2]
    print(pos[0] * pos[1])
