import numpy as np


def connect_arcs(data):
    graph = {}
    for line in data:
        if line[0] in graph.keys():
            graph[line[0]].append(line[1])
        else:
            graph[line[0]] = [line[1]]
        if line[1] not in graph.keys():
            graph[line[1]] = []
    return graph


def available_steps(graph):
    counter = []
    for vertex, destinations in graph.items():
        for dest in destinations:
            if dest not in counter:
                counter.append(dest)
    available = []
    for vertex in graph:
        if vertex in graph and vertex not in counter:
            available.append(vertex)
    return sorted(available)


def task1(graph):
    n = len(graph)
    result = ""
    while len(result) < n:
        next_step = available_steps(graph)[0]
        result += next_step
        print(available_steps(graph), result)
        del graph[next_step]
    return result


def workload(letter, delay):
    return ord(letter) - 64 + delay


def task2(graph, num_workers=5, delay=60):
    n = len(graph)
    result = ""
    time = 0
    workers = np.zeros(num_workers, dtype=int)
    avail = available_steps(graph)
    tasks = np.zeros(num_workers, dtype=str)
    while len(result) < n or workers.sum() > 0:
        for i in range(len(workers)):
            avail.sort()
            if workers[i] == 1:
                workers[i] = 0
                result += tasks[i]
                del graph[tasks[i]]
                tasks[i] = ""
                avail = available_steps(graph)
                j = 0
                while j < len(avail):
                    if avail[j] in tasks:
                        del avail[j]
                    else:
                        j += 1
            elif workers[i] > 1:
                workers[i] -= 1
            if tasks[i] == "" and avail:
                tasks[i] = avail[0]
                del avail[0]
                workers[i] += workload(tasks[i], delay)
        if num_workers == 2:
            print("%d\t%s (%d)\t%s (%d)\t%s" % (time, tasks[0], workers[0], tasks[1], workers[1], result))
        else:
            print(
                "%d\t%s (%d)\t%s (%d)\t%s (%d)\t%s (%d)\t%s (%d)\t%s\t%s"
                % (
                    time,
                    tasks[0],
                    workers[0],
                    tasks[1],
                    workers[1],
                    tasks[2],
                    workers[2],
                    tasks[3],
                    workers[3],
                    tasks[4],
                    workers[4],
                    result,
                    available_steps(graph),
                )
            )
        time += 1

    return time - 1


if __name__ == "__main__":
    data = np.loadtxt("input", dtype=str)
    data = np.array([data[:, 1], data[:, 7]]).T
    graph = connect_arcs(data)
    print(task1(graph))
    graph = connect_arcs(data)
    print(task2(graph, num_workers=5, delay=60))
