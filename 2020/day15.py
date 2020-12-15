if __name__ == "__main__":
    with open("input15") as file:
        bank = {int(x): [i+1] for i, x in enumerate(file.readline().split(","))}
    spoken = 0
    turn = len(bank)
    prev = list(bank.keys())[-1]
    while turn < 30000000:
        turn += 1
        if turn % 1000000 == 0:
            print(f"{turn // 1000000} / 30")
        if len(bank[prev]) < 2:
            spoken = 0
        else:
            spoken = bank[prev][-1] - bank[prev][-2]
        if spoken not in bank.keys():
            bank[spoken] = [turn]
        else:
            bank[spoken].append(turn)
            bank[spoken] = bank[spoken][-2:]
        prev = spoken
    print(f"turn {turn}: {spoken}")

