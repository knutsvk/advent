ALPHABET = "abcdefghijklmnopqrstuvwxyz"


if __name__ == "__main__":
    with open("input6") as file:
        data = file.read()
    groups = data.replace('\n', ' ').split('  ')
    print(1, sum([len(set(list(group.replace(' ', '')))) for group in groups]))
    print(2, sum(len([letter for letter in ALPHABET if all([letter in person for person in group.split(' ')])]) for group in groups))
