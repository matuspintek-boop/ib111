
def left_bound(array: list[int], target: int) -> int | None:
    lower, upper = 0, len(array)
    while lower < upper:
        mid = (lower + upper) // 2
        if target <= array[mid]:
            upper = mid
        else:
            lower = mid + 1

    assert lower == upper

    if lower < len(array) and array[lower] == target:
        return lower
    return None
