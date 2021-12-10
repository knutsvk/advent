from collections import deque

PAIRS = {"(": ")", "[": "]", "{": "}", "<": ">"}
POINTS = {")": 3, "]": 57, "}": 1197, ">": 25137}
SCORES = {")": 1, "]": 2, "}": 3, ">": 4}


def get_data(filename):
    with open(filename) as file:
        return [line.strip() for line in file]


def process(data):
    x = 0
    y = []
    for line in data:
        broken = False
        expected_closers = deque()
        for c in line:
            if c in PAIRS.keys():
                expected_closers.append(PAIRS[c])
                continue
            elif c != expected_closers.pop():
                x += POINTS[c]
                broken = True
        if not broken:
            linescore = 0
            while expected_closers:
                linescore *= 5
                linescore += SCORES[expected_closers.pop()]
            y.append(linescore)
    y.sort()
    return x, y[len(y) // 2]


example_data = get_data("example10")
input_data = get_data("input10")

print(process(example_data))
print(process(input_data))
