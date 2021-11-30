from collections import defaultdict
import numpy as np


def get_input():
    data = []
    with open("input") as inputfile:
        for line in inputfile:
            line = line.replace("[", "")
            line = line.replace("]", "")
            line = line.replace("#", "")
            line = line.replace(":", " ")
            line = line.replace("-", " ")
            line = line.split()
            month = int(line[1])
            day = int(line[2])
            hour = int(line[3])
            minute = int(line[4])
            if line[-1] == "asleep":
                event = 0
            elif line[-1] == "up":
                event = 1
            else:
                event = int(line[6])
            data.append([event, month, day, hour, minute])
    return sorted(data, key=lambda x: (x[1], x[2], x[3], x[4]))


def sleepiest_guard_1(log):
    guards = defaultdict(int)
    guard = -1
    fellasleep = 0
    for i, event in enumerate(log):
        if event[0] == 0:
            fellasleep = event[4]
            # print("Event %d (%02d/%02d %02d:%02d) guard %d fell asleep."
            #        % (i, event[1], event[2], event[3], event[4], guard))
        elif event[0] == 1:
            guards[guard] += event[4] - fellasleep
            # print("Event %d (%02d/%02d %02d:%02d) guard %d woke up after %d minutes."
            #        % (i, event[1], event[2], event[3], event[4], guard, event[4] - fellasleep))
        else:
            guard = event[0]
            # print("Event %d (%02d/%02d %02d:%02d) guard %d arrives."
            #        % (i, event[1], event[2], event[3], event[4], guard))

    sleepiest = (-1, -1)
    for key, value in guards.items():
        if value > sleepiest[1]:
            sleepiest = (key, value)

    minutes_asleep = np.zeros(60, dtype=int)
    sleepiest_minute = 0
    guard = log[0][0]
    fellasleep = 0
    for event in log:
        if event[0] == 0:
            fellasleep = event[4]
        elif event[0] == 1:
            if guard == sleepiest[0]:
                minutes_asleep[fellasleep : event[4]] += 1
        else:
            guard = event[0]
    sleepiest_minute = minutes_asleep.argmax()

    assert minutes_asleep.sum() == sleepiest[1]

    return sleepiest[0] * sleepiest_minute


def sleepiest_guard_2(log):
    guards = []
    for event in log:
        if (event[0] > 1) and (event[0] not in guards):
            guards.append(event[0])

    minutes_asleep = np.zeros((60, len(guards)), dtype=int)
    guard = -1
    fellasleep = 0
    for i, event in enumerate(log):
        if event[0] == 0:
            fellasleep = event[4]
        elif event[0] == 1:
            minutes_asleep[fellasleep : event[4], guards.index(guard)] += 1
        else:
            guard = event[0]

    sleepiest_guard_and_minute = np.unravel_index(minutes_asleep.argmax(), minutes_asleep.shape)
    sleepiest_minute = sleepiest_guard_and_minute[0]
    sleepiest_guard = guards[sleepiest_guard_and_minute[1]]
    print(sleepiest_guard, sleepiest_minute)

    return sleepiest_guard * sleepiest_minute


if __name__ == "__main__":
    log = get_input()
    print(sleepiest_guard_1(log))
    print(sleepiest_guard_2(log))
