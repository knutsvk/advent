from copy import deepcopy


def run(instructions):
    acc = 0
    previous_instructions = []
    line = 0
    while line < len(instructions):
        if line in previous_instructions:
            return False, acc
        previous_instructions.append(line)
        instruction = instructions[line]
        if instruction[0] == 'acc':
            acc += instruction[1]
        elif instruction[0] == 'jmp':
            line += instruction[1] - 1
        line += 1
    return True, acc


if __name__ == "__main__":
    with open("input8") as file:
        data = [(line.split(' ')[0], int(line.split(' ')[1])) for line in file.read().splitlines()]
    print(run(data)[1])

    for i, instruction in enumerate(data):
        tmp_data = deepcopy(data)
        if instruction[0] == 'nop':
            tmp_data[i] = ('jmp', data[i][1])
        elif instruction[0] == 'jmp':
            tmp_data[i] = ('nop', data[i][1])
        else:
            continue
        result = run(tmp_data)
        if result[0]:
            print(result[1])
            break
