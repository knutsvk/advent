REQUIRED_ENTRIES = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]


def is_valid(key, value) -> bool:
    valid = False
    if key == "byr":
        valid = len(value) == 4 and 1920 <= int(value) <= 2002
    if key == "iyr":
        valid = len(value) == 4 and 2010 <= int(value) <= 2020
    if key == "eyr":
        valid = len(value) == 4 and 2020 <= int(value) <= 2030
    if key == "hgt":
        unit = value[-2:]
        if unit == "cm":
            valid = 150 <= int(value[:-2]) <= 193
        elif unit == "in":
            valid = 59 <= int(value[:-2]) <= 76
    if key == "hcl":
        valid = value[0] == "#" and len(value[1:]) == 6
    if key == "ecl":
        valid = value in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    if key == "pid":
        valid = len(value) == 9
    if not valid:
        print(f"invalid entry {key}:{value}")
    return valid


def read_passports():
    with open("input4") as file:
        passports = [{entry.split(":")[0]: entry.split(":")[1] for entry in passport.split(" ")} for passport in file.read().replace("\n", " ").split("  ")]
    return passports


def task1():
    passports = read_passports()
    num_valid_passports = 0
    for passport in passports:
        if all([entry in passport.keys() for entry in REQUIRED_ENTRIES]):
            num_valid_passports += 1
    print(num_valid_passports)


def task2():
    passports = read_passports()
    num_valid_passports = 0
    for passport in passports:
        if all([key in passport.keys() and is_valid(key, passport[key]) for key in REQUIRED_ENTRIES]):
            num_valid_passports += 1
    print(num_valid_passports)


if __name__ == "__main__":
    task1()
    task2()
