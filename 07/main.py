import numpy as np


def connect_arcs(data):
    graph = {}
    end_vertex = ''
    for line in data:
        if line[0] in graph.keys():
            graph[line[0]].append(line[1])
        else:
            graph[line[0]] = [line[1]]
        if line[1] not in graph.keys():
            graph[line[1]] = []
            end_vertex = line[1]
    return graph, end_vertex


def smallest_available_step(graph):
    counter = []
    for vertex, destinations in graph.items():
        for dest in destinations:
            if dest not in counter:
                counter.append(dest)
    available = []
    for vertex in graph: 
        if vertex in graph and vertex not in counter:
            available.append(vertex)
    return sorted(available)[0]


if __name__ == "__main__":
    data = np.loadtxt("input", dtype=str)
    data = np.array([data[:,1], data[:,7]]).T
    graph, end_vertex = connect_arcs(data)
    n = len(graph)
    result = ''
    while(len(result) < n):
        next_step = smallest_available_step(graph)
        result += next_step
        del graph[next_step]
    print(result)
