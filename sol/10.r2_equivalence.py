Pair = tuple[int, int]


def partition2pairs(partition: list[set[int]]) -> set[Pair]:
    result = set()
    for subset in partition:
        for elem1 in subset:
            for elem2 in subset:
                result.add((elem1, elem2))
    return result


def pairs2partition(pairs: set[Pair]) -> list[set[int]]:
    partitions: dict[int, set[int]] = {}
    for (a, b) in pairs:
        partitions[a] = partitions.get(a, {a}) | {b}

    all_elements = set(partitions.keys())
    result: list[set[int]] = []
    for element, partition in partitions.items():
        if element not in all_elements:
            continue
        result.append(partition)
        for elem in partition:
            all_elements.remove(elem)

    return result
