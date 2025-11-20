def cartesian(a, b):
    out = []
    for x in a:
        for y in b:
            out.append((x, y))
    return out
