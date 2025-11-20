def selectsort(num_list: list[int]) -> None:
    for i in range(len(num_list)):
        min_idx = i
        for j in range(i + 1, len(num_list)):
            if num_list[min_idx] > num_list[j]:
                min_idx = j
        num_list[i], num_list[min_idx] \
            = num_list[min_idx], num_list[i]
