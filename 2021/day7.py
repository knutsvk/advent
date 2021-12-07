def get_data(filename):
    with open(filename) as f:
        data = [int(c) for c in f.readline().split(",")]
    return data


def process(data, f):
    return min([sum([f(x, i) for x in data]) for i in range(max(data) + 1)])


example_data = get_data("example7")
input_data = get_data("input7")

print(process(example_data, lambda x, i: abs(x - i)))
print(process(input_data, lambda x, i: abs(x - i)))
print(process(example_data, lambda x, i: abs(x - i) * (abs(x - i) + 1) // 2))
print(process(input_data, lambda x, i: abs(x - i) * (abs(x - i) + 1) // 2))
