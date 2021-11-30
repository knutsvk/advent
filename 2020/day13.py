with open("input13") as file:
    ready = int(file.readline())
    buses = [(i, int(x)) for i, x in enumerate(file.readline().split(",")) if x != "x"]

mins_til_next = [bus[1] - ready % bus[1] for bus in buses]
next_bus = mins_til_next.index(min(mins_til_next))
print(buses[next_bus][1] * mins_til_next[next_bus])

t = 0
counter = buses[0][1]
del buses[0]
while buses:
    t += counter
    for bus in buses:
        if bus[1] - t % bus[1] == bus[0] % bus[1]:
            counter *= bus[1]
            buses.remove(bus)
print(t)
