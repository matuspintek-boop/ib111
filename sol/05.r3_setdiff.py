def set_difference(a: set[int], b: set[int]) -> set[int]:
    result = set()
    for x in a:
        if x not in b:
            result.add(x)
    return result


def set_remove(to_reduce: set[int], other: set[int]) -> None:
    for x in other:
        if x in to_reduce:
            to_reduce.remove(x)


def set_symmetric_diff(a: set[int], b: set[int]) -> set[int]:
    result = set()
    for x in a:
        if x not in b:
            result.add(x)
    for x in b:
        if x not in a:
            result.add(x)
    return result


def set_symmetric_inplace(to_change: set[int],
                          other: set[int]) -> None:
    for x in other:
        if x in to_change:
            to_change.remove(x)
        else:
            to_change.add(x)
