LO = 248345
HI = 746315


def valid(password: int) -> bool:
    pw = str(password)
    if len(pw) != 6:
        return False
    if "".join(sorted(pw)) != pw:
        return False
    if (
        any([c1 != c2 == c3 != c4 for c1, c2, c3, c4 in zip(pw[0:4], pw[1:5], pw[2:6], pw[3:7])])
        or pw[0] == pw[1] != pw[2]
        or pw[3] != pw[4] == pw[5]
    ):
        return True
    return False


if __name__ == "__main__":
    valid_passwords = [pw for pw in range(LO, HI + 1) if valid(pw)]
    for pw in valid_passwords:
        print(pw)
    print(len(valid_passwords))
