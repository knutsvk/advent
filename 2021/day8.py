def get_data(filename):
    with open(filename) as f:
        lines = []
        for line in f:
            patterns, code = line.split("|")
            patterns = ["".join(sorted(pattern)) for pattern in patterns.strip().split(" ")]
            code = ["".join(sorted(digit)) for digit in code.strip().split(" ")]
            lines.append({"patterns": patterns, "code": code})
    return lines


def task1(data):
    count = 0
    for line in data:
        for digit in line["code"]:
            if len(digit) in [2, 3, 4, 7]:
                count += 1
    return count


def task2(data):
    codes = []
    for i, line in enumerate(data):
        mapping = {}
        while len(mapping) < 10:
            for p in line["patterns"]:
                if p not in mapping.values():
                    if len(mapping) == 9:
                        for i in range(10):
                            if i not in mapping.keys():
                                mapping[i] = p
                    if len(p) == 2:
                        mapping[1] = p
                    elif len(p) == 3:
                        mapping[7] = p
                    elif len(p) == 4:
                        mapping[4] = p
                    elif len(p) == 7:
                        mapping[8] = p
                    elif len(p) == 6:
                        if 1 in mapping.keys():
                            if mapping[1][0] not in p or mapping[1][1] not in p:
                                mapping[6] = p
                        if 6 in mapping.keys() and mapping[6] != p and 4 in mapping.keys():
                            if (
                                mapping[4][0] not in p
                                or mapping[4][1] not in p
                                or mapping[4][2] not in p
                                or mapping[4][3] not in p
                            ):
                                mapping[0] = p
                        if 6 in mapping.keys() and mapping[6] != p and 0 in mapping.keys() and mapping[0] != p:
                            mapping[9] = p
                    elif len(p) == 5:
                        if 1 in mapping.keys():
                            if mapping[1][0] in p and mapping[1][1] in p:
                                mapping[3] = p
                        if 8 in mapping.keys() and 9 in mapping.keys():
                            missing_char = "".join(c for c in mapping[8] if c not in mapping[9])
                            if missing_char in p:
                                mapping[2] = p
        codes.append(
            int(
                "".join(
                    str(list(mapping.keys())[list(mapping.values()).index(d)]) if d in mapping.values() else ""
                    for d in line["code"]
                )
            )
        )
    return sum(codes)


input_data = get_data("input8")
print(task1(input_data))
print(task2(input_data))
