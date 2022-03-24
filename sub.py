def sub(b, ax):
    r = []
    for i in range(len(b)):
        r.append((abs(b[i] - ax[i])))
    return r