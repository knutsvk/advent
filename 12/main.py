import sys


def get_input():
    """
    initial state: #..#.#..##......###...###

    ...## => #
    ..#.. => #
    """
    leftmost_plant = 0
    state = ""
    rules = {}
    with open("input") as inputfile: 
        for i, line in enumerate(inputfile):
            if i == 0:
                line = line.replace("initial state: ", '')
                state += line.rstrip()
            elif i == 1:
                continue
            else:
                line = line.replace('=>', '')
                line = line.split()
                rules[line[0]] = line[1]
    while state.find('#') <= 2:
        state = '.' + state
        leftmost_plant -= 1
    while state.rfind('#') >= len(state) - 3:
        state = state + '.'
    return state, leftmost_plant, rules


def count_living_plants(state, leftmost_plant):
    living_plants = 0
    for i, plant in enumerate(state):
        if plant == '#':
            living_plants += (i + leftmost_plant)
    return living_plants


if __name__ == "__main__":
    num_generations = 20
    if len(sys.argv) > 1:
        num_generations = int(sys.argv[1])
    old_state, leftmost_plant, rules = get_input()
    state = old_state
    generation = 0
    print("Gen\tShift\tSum")
    print("%d\t(%d)\t[%d]\t%s" %\
            (generation, leftmost_plant, count_living_plants(state, leftmost_plant), state))
    while generation < num_generations:
        for i in range(2,len(state)-2):
            tmp = list(state)
            tmp[i] = rules[old_state[i-2:i+3]]
            state = "".join(tmp)
        while state.find('#') != 3:
            if state.find('#') < 3: 
                state = '.' + state
                leftmost_plant -= 1
            else:
                state = state.replace('.', '', 1)
                leftmost_plant += 1
        while state.rfind('#') >= len(state) - 3:
            state = state + '.'
        generation += 1
        if state == old_state:
            shift = num_generations - generation
            leftmost_plant += shift
            print("Reached equilibrium at generation %d, just need to shift lefmostplant by %d." %\
                    (generation, shift))
            break
        old_state = state
        print("%d\t(%d)\t[%d]\t%s" %\
                (generation, leftmost_plant, count_living_plants(state, leftmost_plant), state))
    print("Answer: %d" % count_living_plants(state, leftmost_plant))
