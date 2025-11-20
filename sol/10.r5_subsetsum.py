

def subset_sum_rec(nums: list[int], total: int,
                   start: int) -> None | set[int]:
    if total == 0:
        return set()

    for i in range(start, len(nums)):
        num = nums[i]
        if num > total:
            return None

        result = subset_sum_rec(nums, total - num, i + 1)
        if result is not None:
            result.add(num)
            return result

    return None


def subset_sum(nums: set[nat1], total: nat1) -> None | set[int]:
    return subset_sum_rec(sorted(nums), total, 0)


def validate_sum(i_arg: to_test, f_result: to_test,
                 g_result: to_test) -> bool:
    if f_result is None or g_result is None:
        return f_result == g_result

    numbers, total = i_arg
    return (isinstance(g_result, set) and
            sum(f_result) == sum(g_result) and g_result <= numbers)
