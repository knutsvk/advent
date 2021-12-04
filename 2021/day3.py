import numpy as np

with open("input3") as f:
    xs = sorted([l.strip() for l in f])
e = "".join(str(x) for x in [np.median([int(x[i]) for x in xs]).astype(int) for i in range(len(xs[0]))])
g = "".join(str(int(not int(x))) for x in e)
print(int(g, 2) * int(e, 2))

os = xs.copy()
for i in range(len(xs[0])):
    common = os[len(os) // 2][i]
    os = [o for o in os if o[i] == common]
    if len(os) == 1:
        o = os[0]
        break
cs = xs.copy()
for i in range(len(xs[0])):
    common = cs[len(cs) // 2][i]
    cs = [c for c in cs if c[i] != common]
    if len(cs) == 1:
        c = cs[0]
        break
print(int(o, 2) * int(c, 2))
