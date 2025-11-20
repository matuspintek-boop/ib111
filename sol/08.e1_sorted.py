def is_sorted(num_list: list[int]) -> bool:
    if len(num_list) <= 1:
        return True

    for i in range(len(num_list) - 1):
        if num_list[i] > num_list[i + 1]:
            return False

    return True
