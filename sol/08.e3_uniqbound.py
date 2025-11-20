def lower_bound(num_list: list[int], num: int) -> int | None:
    if len(num_list) == 0 or num < num_list[0]:
        return None

    left = 0
    right = len(num_list) - 1

    while left != right:
        mid = (left + right + 1) // 2

        if num_list[mid] > num:
            right = mid - 1
        else:
            left = mid

    return num_list[left]
