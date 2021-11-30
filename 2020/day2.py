def task1():
    valid_passwords = 0
    with open("input2") as file:
        for i, line in enumerate(file):
            lower, rest = line.split(sep="-")
            lower = int(lower)
            upper, special_letter, password = rest.split(sep=" ")
            upper = int(upper)
            special_letter = special_letter[0]
            password = password[:-1]
            special_letter_occurrences = 0
            for letter in password:
                if letter == special_letter:
                    special_letter_occurrences += 1
            if lower <= special_letter_occurrences <= upper:
                valid_passwords += 1
    print(valid_passwords)


def task2():
    valid_passwords = 0
    with open("input2") as file:
        for i, line in enumerate(file):
            first_pos, rest = line.split(sep="-")
            first_pos = int(first_pos)
            second_pos, special_letter, password = rest.split(sep=" ")
            second_pos = int(second_pos)
            special_letter = special_letter[0]
            password = password[:-1]
            if sum([password[pos - 1] == special_letter for pos in [first_pos, second_pos]]) == 1:
                valid_passwords += 1
    print(valid_passwords)


if __name__ == "__main__":
    task1()
    task2()
