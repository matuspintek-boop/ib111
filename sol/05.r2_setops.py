def set_union(a: set[int], b: set[int]) -> set[int]:
    result = set()

    for x in a:
        result.add(x)
    for x in b:
        result.add(x)

    return result


def set_update(to_extend: set[int], other: set[int]) -> None:
    for x in other:
        to_extend.add(x)


def set_intersect(a: set[int], b: set[int]) -> set[int]:
    if len(b) < len(a):
        a, b = b, a

    result = set()

    for x in a:
        if x in b:
            result.add(x)

    return result


def set_keep(to_reduce: set[int], other: set[int]) -> None:
    for x in to_reduce.copy():
        if x not in other:
            to_reduce.remove(x)
