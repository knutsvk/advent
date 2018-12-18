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
    tasks = np.zeros(num_workers, dtype=str)
    while(len(result) < n or workers.sum() > 0):
        # TODO: Only add avail[0] to result when worker is FINISHED working on it (workload has
        # gone to zero). If not, other workers start too early. Also, allow worker to start working
        # on new letter in the same timestep that they went from workload 1 to 0... 
        avail = available_steps(graph)
        print(avail)
        for i, (worker, task) in enumerate(zip(workers, tasks)): 
            print("worker %d" % i)
            if task == '' and avail:
                tasks[i] = avail[0]
                workers[i] += workload(tasks[i], delay)
            if worker > 1:
                workers[i] -= 1
            elif worker == 1:
                workers[i] = 0
                result += tasks[i]
                del graph[tasks[i]]
                tasks[i] = ''
        print("%d\t%s (%d)\t%s (%d)\t%s" % (time, tasks[0], workers[0], tasks[1], workers[1], result))
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
