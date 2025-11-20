def subsets(original: set[int]) -> list[set[int]]:
    result: list[set[int]] = [set()]
    subsets_rec(list(original), result)
    return result


def subsets_rec(original: list[int],
                result: list[set[int]]) -> None:
    if not original:
        return
    curr_num = original.pop()
    to_add: list[set[int]] = []
    for curr_set in result:
        to_add.append(curr_set | {curr_num})
    result.extend(to_add)
    subsets_rec(original, result)
