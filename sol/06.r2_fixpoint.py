def apply_f_on_num(num: int) -> set[int]:
    return {num, num // 2, num // 7}


def fixpoint(starting_set: set[int]) -> int:
    next_set: set[int] = set()
    prev_set = starting_set.copy()
    result = 0

    while True:
        for num in prev_set:
            next_set.update(apply_f_on_num(num))
        if len(prev_set) == len(next_set):
            return result
        result += 1
        prev_set.update(next_set)
