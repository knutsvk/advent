def get_input():
    with open("input18") as file:
        lines = [l.strip() for l in file]
    return lines


def compute_without_parantheses(line):
    syms = line.split(" ")
    x = int(syms[0])
    for i in range(1, len(syms), 2):
        if syms[i] == "+":
            x += int(syms[i + 1])
        else:
            x *= int(syms[i + 1])
    return str(x)


def compute_new_rules_without_parantheses(line):
    syms = line.split(" ")
    new_line = f"({syms[0]}"
    for i in range(1, len(syms), 2):
        if syms[i] == "+":
            new_line += f"+{syms[i+1]}"
        else:
            new_line += f")*({syms[i+1]}"
    new_line += ")"
    return str(eval(new_line))


def task1():
    lines = get_input()
    res = 0
    for line in lines:
        for i in range(line.count("(")):
            close_index = line.index(")")
            open_index = line.rindex("(", 0, close_index)
            line = (
                line[:open_index]
                + compute_without_parantheses(line[open_index + 1 : close_index])
                + line[close_index + 1 :]
            )
        res += int(compute_without_parantheses(line))
    print(res)


def task2():
    lines = get_input()
    res = 0
    for line in lines:
        for i in range(line.count("(")):
            close_index = line.index(")")
            open_index = line.rindex("(", 0, close_index)
            line = (
                line[:open_index]
                + compute_new_rules_without_parantheses(line[open_index + 1 : close_index])
                + line[close_index + 1 :]
            )
        res += int(compute_new_rules_without_parantheses(line))
    print(res)


if __name__ == "__main__":
    task1()
    task2()
