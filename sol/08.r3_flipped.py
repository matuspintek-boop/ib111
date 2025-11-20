

def last_index(arr: list[int], idx: int) -> int:
    first = arr[idx]
    while idx < len(arr) - 1 and first == arr[idx + 1]:
        idx += 1
    return idx


def skip_run(arr: list[int], idx: int, step: int) -> int:
    first = arr[idx]
    while (idx + step < len(arr) and
           idx + step >= 0 and
           first == arr[idx + step]):
        idx += step
    return idx


def misplaced(arr: list[int]) -> list[int]:
    indices = []
    for i in range(1, len(arr)):
        if arr[i] < arr[i - 1]:
            indices.append(i)
    return indices


def is_almost_sorted_bad(arr: list[int]) -> bool:
    indices = misplaced(arr)

    if len(indices) == 0 or len(indices) > 2:
        return False

    if len(indices) == 2:
        first, second = indices[0] - 1, indices[1]
    else:
        first, second = indices[0] - 1, last_index(arr, indices[0])

    copy = arr.copy()
    copy[first], copy[second] = copy[second], copy[first]

    return len(misplaced(copy)) == 0


def is_almost_sorted(arr: list[int]) -> bool:
    indices = misplaced(arr)

    if len(indices) == 0 or len(indices) > 2:
        return False

    if len(indices) == 2:
        first, second = indices[0] - 1, indices[1]
    else:
        first, second = (skip_run(arr, indices[0] - 1, -1),
                         skip_run(arr, indices[0], 1))

    copy = arr.copy()
    copy[first], copy[second] = copy[second], copy[first]

    result = len(misplaced(copy)) == 0

    # reject inputs that trigger a bug in the previous reference
    # solution; TODO remove later
    if result:
        assert is_almost_sorted_bad(arr)
    return result


def swap(items: list[int], i: int, j: int) -> list[int]:
    items = items.copy()
    items[i], items[j] = items[j], items[i]
    return items
