from ib111 import week_08  # noqa


# Implementujte čistou funkci ‹frequency_sort›, která podle
# frekvencí výskytu seřadí hodnoty v seznamu ‹values›. Hodnoty se
# stejnou frekvencí výskytu nechť jsou seřazeny vzestupně podle
# hodnoty samotné. Výsledný seznam bude obsahovat každou hodnotu
# právě jednou.

def frequency_sort(values: list[int]) -> list[int]:

    # data, dict with key = number of appearences, value = number
    data_lists: dict[int, list[int]] = {}

    # oposite data to data_lists, key is number, value its count of appearences
    data: dict[int, int] = {}

    output: list[int] = []

    for value in values:
        if value in data:
            data[value] += 1
        else:
            data[value] = 1

    for number, appearences in data.items():
        if appearences not in data_lists:
            data_lists[appearences] = [number]
        else:
            data_lists[appearences].append(number)

    # counts of number appearences (how many items does
    # number have) incline sorted
    sorted_count_of_appearences: list[int] = sorted(data_lists.keys())

    for i in range(len(sorted_count_of_appearences) - 1, -1, -1):
        key = sorted_count_of_appearences[i]
        data_lists[key].sort()
        for number in data_lists[key]:
            output.append(number)

    return output


def main() -> None:
    assert frequency_sort([]) == []
    assert frequency_sort([1]) == [1]
    assert frequency_sort([1, 3, 2, 4]) == [1, 2, 3, 4]
    assert frequency_sort([5, 6, 2, 5, 3, 3, 6, 5, 5, 6, 5]) == [5, 6, 3, 2]
    assert frequency_sort([1, 1, 2, 2, 2, 3, 3, 3, 3, 3, 5, 5,
                           5, 4, 4, 4, 4, 4, 4]) == [4, 3, 2, 5, 1]
    records = [1, 2, 2, 2, 3, 3]
    assert frequency_sort(records) == [2, 3, 1]
    assert records == [1, 2, 2, 2, 3, 3]


if __name__ == "__main__":
    main()
