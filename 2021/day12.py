def get_data(filename):
    graph = {}
    with open(filename) as file:
        for line in file:
            start, end = line.strip().split("-")
            if start in graph.keys():
                graph[start].append(end)
            else:
                graph[start] = [end]
            if end in graph.keys():
                graph[end].append(start)
            else:
                graph[end] = [start]
        return graph


def find_paths(graph, path, node, extra_life=False):
    path = path + [node]
    if node == "end":
        return [path]
    paths = []
    for child in graph[node]:
        if child == "start":
            continue
        if child not in path or child.isupper():
            paths.extend(find_paths(graph, path, child, extra_life))
        elif extra_life:
            paths.extend(find_paths(graph, path, child, False))
    return paths


example_data = get_data("example12")
input_data = get_data("input12")

print(len(find_paths(example_data, [], "start")))
print(len(find_paths(input_data, [], "start")))
print(len(find_paths(example_data, [], "start", extra_life=True)))
print(len(find_paths(input_data, [], "start", extra_life=True)))
