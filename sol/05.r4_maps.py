def image(f: dict[int, int], values: set[int]) -> set[int]:
    result = set()
    for x in values:
        if x in f:
            result.add(f[x])
    return result


def preimage(f: dict[int, int], values: set[int]) -> set[int]:
    result = set()
    for x in f.keys():
        if f[x] in values:
            result.add(x)
    return result


def compose(f: dict[int, int], g: dict[int, int]) -> dict[int, int]:
    result = {}
    for x in g.keys():
        result[x] = f[g[x]]
    return result


def kernel(f: dict[int, int]) -> set[tuple[int, int]]:
    result = set()
    for x in f.keys():
        for y in f.keys():
            if f[x] == f[y]:
                result.add((x, y))
    return result
