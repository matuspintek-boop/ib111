

def flatten(arr: list[list[int]]) -> list[int]:
    result = []
    for sublist in arr:
        for elem in sublist:
            result.append(elem)
    return result


def sort_nested(arr: list[list[int]]) -> list[list[int]]:
    flattened = flatten(arr)
    flattened.sort()

    result = []
    index = 0
    for nested in arr:
        sublist = []
        for _ in range(len(nested)):
            sublist.append(flattened[index])
            index += 1
        result.append(sublist)
    return result
