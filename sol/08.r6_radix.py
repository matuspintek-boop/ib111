
def radixsort(to_sort: list[int]) -> list[int]:
    if to_sort == []:
        return []

    max_digits = digit_count(max(to_sort))
    res = to_sort
    for i in range(max_digits):
        res = counting_sort_by_digit(res, i)
    return res


def counting_sort_by_digit(to_sort: list[int], curr_digit: int) -> \
        list[int]:
    bucket_size = [0 for i in range(10)]
    bucket_start = [0 for i in range(10)]
    bucket_index = [0 for i in range(10)]
    res = [0 for i in range(len(to_sort))]

    for num in to_sort:
        bucket_size[digit(num, curr_digit)] += 1

    for i in range(1, len(bucket_size)):
        bucket_start[i] = bucket_start[i - 1] + bucket_size[i - 1]

    for num in to_sort:
        d = digit(num, curr_digit)
        res[bucket_start[d] + bucket_index[d]] = num
        bucket_index[d] += 1

    return res


def digit(num: int, pos: int) -> int:
    return (num // (10 ** pos)) % 10


def digit_count(num: int) -> int:
    result = 0
    while num > 0:
        result += 1
        num //= 10
    return result
