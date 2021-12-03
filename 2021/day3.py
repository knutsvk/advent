with open("example3") as file:
    xs = [l.strip() for l in file]
    xs_dec = [int(x, 2) for x in xs]
g = ""
e = ""
for i in range(len(xs[0])):
    common = sum(int(x[i]) for x in xs) >= len(xs) / 2
    g += str(int(not common))
    e += str(int(common))
print(g, e)
g = int(g, 2)
e = int(e, 2)
print(f"g: {g}, e: {e}, g * e: {g * e}")
ys = xs.copy()
for i in range(len(xs[0])):
    common = str(int(sum(int(y[i]) for y in ys) >= len(ys) / 2))
    ys = [y for y in ys if y[i] == common]
    if len(ys) == 1:
        break
o = ys[0]
ys = xs.copy()
for i in range(len(xs[0])):
    common = str(int(sum(int(y[i]) for y in ys) >= len(ys) / 2))
    ys = [y for y in ys if y[i] != common]
    if len(ys) == 1:
        break
c = ys[0]
print(o, c)
o = int(o, 2)
c = int(c, 2)
print(f"o: {o}, c: {c}, o * c: {o * c}")
