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
    result = ''
    while(len(result) < n):
        next_step = available_steps(graph)[0]
        result += next_step
        del graph[next_step]
    return result


def workload(letter, delay):
    return ord(letter) - 64 + delay


def task2(graph, num_workers=5, delay=60):
    n = len(graph)
    result = ''
    time = 0
    workers = np.zeros(num_workers, dtype=int)
    while(len(result) < n or workers.sum() > 0):
        #print("%d\t%d\t%d\t%d\t%d\t%d\t%s" % (time, workers[0], workers[1], workers[2], workers[3], workers[4], result))
        print("%d\t%d\t%d\t%s" % (time, workers[0], workers[1], result))
        # TODO: Only add avail[0] to result when worker is FINISHED working on it (workload has
        # gone to zero). If not, other workers start too early. Also, allow worker to start working
        # on new letter in the same timestep that they went from workload 1 to 0... 
        avail = available_steps(graph)
        for w, worker in enumerate(workers): 
            if worker == 0 and avail:
                workers[w] += workload(avail[0], delay)
                result += avail[0]
                del graph[avail[0]]
                del avail[0]
            if worker > 0:
                workers[w] -= 1
        time += 1

    return time
        

if __name__ == "__main__":
    data = np.loadtxt("input_test", dtype=str)
    data = np.array([data[:,1], data[:,7]]).T
    graph = connect_arcs(data)
    print(task1(graph))
    graph = connect_arcs(data)
    print(task2(graph, num_workers=2, delay=0))
    # BHRTWCYSELPUVZAOIJKGMFQDXN
